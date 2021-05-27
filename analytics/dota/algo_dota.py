import json

import requests
from time import sleep

from django.http import HttpResponse

from analytics.dota.counter import Counter
from analytics.dota.error import DotaError
from main.models import DotaResult

LIMIT = 20
TEMPLATE = "Вы играете на {} роли \n" \
           "{} \n" \
           "Вы стараетесь в играх на {} от возможных 100% \n" \
           "Процент участия в командных убийствах равен {}"


def dota_start_analysing(request):
    user = request.user
    steam_id = user.talantuser.steam_id

    dota = DotaAnalysing(steam_id, user.talantuser.dota_result)
    data = dota.start()

    return HttpResponse(data, content_type='application/json')

class DotaAnalysing:
    def __init__(self, steam_id, db_entry: DotaResult):
        self.db = db_entry
        self.index = 0
        self.side = ""
        self.party = 0
        self.info_about_game = {}
        self.steam_id = steam_id - 76561197960265728
        self.game = []
        self.game_solo = []
        self.game_party = []

    def start(self, flag=True):
        self.get_games_id(flag)
        info = self.analysis()

        self.db.result = True
        self.db.result_num = info["score"]
        self.db.result_str = info["text_score"]
        self.db.result_big_str = TEMPLATE.format(info["role"], info["comparing_skill"],
                                                 info["benefit"], info["frequency_fight"])
        self.db.result_json = json.dumps(info)
        self.db.save()

        return json.dumps(info)

    def analysis(self):
        party = Counter()
        solo = Counter()

        for id_game, slot in self.game:
            try:
                self.party = 0
                self.side = self.check_dire_radiant(slot)
                self.info_about_game = self.get_response_matches(id_game)

                role_weight = self.count_roles(self.side)
                pk_weight = self.count_kill_participating()
                comparing_weight = self.count_comparing()
                fantasy_weigth = self.count_fantasy()

                if self.party > 1:
                    self.game_party.append(id_game)
                    party.role += role_weight
                    party.pk_weight += pk_weight
                    party.num += 1
                    party.comparing += comparing_weight
                    party.fantasy += fantasy_weigth
                else:
                    self.game_solo.append(id_game)
                    solo.role += role_weight
                    solo.pk_weight += pk_weight
                    solo.num += 1
                    solo.comparing += comparing_weight
                    solo.fantasy += fantasy_weigth
            except:
                pass

        print(solo.num, party.num)
        if solo.num == 0 and party.num == 0:
            self.db.error = "Матчи были сыграны давно, невозможно сделать подробный анализ"
            self.db.result = False
            self.db.save()
            raise DotaError("Матчи были сыграны давно, невозможно сделать подробный анализ")

        party_pk = party.count_pk()
        solo_pk = solo.count_pk()
        party_role = party.count_role()
        solo_role = solo.count_role()
        party_quality = party.count_quality()
        solo_quality = solo.count_quality()

        return self.get_final_res(party_role, party_quality, party_pk, solo_role, solo_quality, solo_pk,
                                  solo.check_is_empty(), party.check_is_empty())

    def get_final_res(self, a, b, c, d, e, f, solo_empty, party_empty):
        print(a, b, c, d, e, f)
        if solo_empty:
            score = round((0.4 * a + 0.225 * (b[0] + b[1]) + 0.15 * c) / 0.75, 2)
            return {"score": score,
                    "text_score": self.get_text_score(score),
                    "role": "Core" if round(a, 2) <= 60 else "Support",
                    "comparing_skill": self.get_comparing_text(round(b[0], 2)),
                    "benefit": round(b[1], 2),
                    "frequency_fight": round(c, 2)}
        if party_empty:
            score = round((0.9 * (0.4 * d + 0.225 * (e[0] + e[1]) + 0.15 * f)) / 0.75, 2)
            return {"score": score,
                    "text_score": self.get_text_score(score),
                    "role": "Core" if round(d, 2) <= 60 else "Support",
                    "comparing_skill": self.get_comparing_text(round(e[0], 2)),
                    "benefit": round(e[1], 2),
                    "frequency_fight": round(f, 2)}

        score = round((0.55 * (0.4 * a + 0.225 * (b[0] + b[1]) + 0.15 * c) + 0.45 * 0.9 * (
                0.4 * d + 0.225 * (e[0] + e[1]) + 0.15 * f) / 0.75), 2)
        return {"score": score,
                "text_score": self.get_text_score(score),
                "role": "Core" if round((a + d), 2) <= 60 else "Support",
                "comparing_skill": self.get_comparing_text(round((b[0] + e[0]) / 2, 2)),
                "benefit": round((b[1] + e[1]) / 2, 2),
                "frequency_fight": round((f + c) / 2, 2)}

    def count_fantasy(self):
        weight = {"kills": 0.3,
                  "deaths": -0.3,
                  "assists": 0.15,
                  "last_hits": 0.003,
                  "gold_per_min": 0.002,
                  "tower_kills": 1,
                  "roshan_kills": 1,
                  "denies": 0.003,
                  "obs_placed": 0.5,
                  "sentry_uses": 0.5,
                  "camps_stacked": 0.5,
                  "rune_pickups": 0.25,
                  "stuns": 0.05}

        point = 0
        me = self.info_about_game["players"][self.index]
        keys = weight.keys()

        for x in keys:
            point += me[x] * weight[x]

        return point

    def count_kill_participating(self):
        me = self.info_about_game["players"][self.index]
        return (me["kills"] + me["assists"]) / self.info_about_game[f"{self.side}_score"]

    def count_comparing(self):
        me = self.info_about_game["players"][self.index]["benchmarks"]
        count = 0
        for i in me:
            count += me[i]["pct"]
        return count

    def count_roles(self, side):
        weight = 0
        lane = 0
        gold_per_min = 0
        players = self.info_about_game["players"]

        for i in range(len(players)):
            if players[i]["account_id"] == self.steam_id:
                self.index = i
                party_id = players[i]["party_id"]

                if "lane_role" not in players[i]:
                    self.db.error = "Недостаточно наиграно матчей в этом патче"
                    self.db.result = False
                    self.db.save()
                    raise DotaError("Недостаточно наиграно матчей в этом патче")

                lane = players[i]["lane_role"]
                gold_per_min = players[i]["gold_per_min"]

        for i in range(len(players)):
            if players[i]["party_id"] == party_id:
                self.party += 1

            if players[i]["lane_role"] == lane and players[i]["account_id"] != self.steam_id \
                    and side == self.check_dire_radiant(players[i]["player_slot"]):
                if players[i]["gold_per_min"] > gold_per_min and lane == 1:
                    weight += 1
                elif players[i]["gold_per_min"] > gold_per_min and lane == 3:
                    weight += 0.8
                elif players[i]["gold_per_min"] <= gold_per_min and lane == 1:
                    weight += 0.4
                elif players[i]["gold_per_min"] <= gold_per_min and lane == 3:
                    weight += 0.6

        if weight == 0:
            weight += 0.2

        return weight

    def get_games_id(self, send_request):
        self.refresh_players()
        games = self.get_response_players("matches", limit=LIMIT, game_mode=22)
        if len(games) == 0:
            self.db.error = "Вы не играете в доту или закрыт аккаунт"
            self.db.result = False
            self.db.save()
            raise DotaError("Вы не играете в доту или закрыт аккаунт")
        elif len(games) < LIMIT:
            self.db.error = "Недостаточно игр"
            self.db.result = False
            self.db.save()
            raise DotaError("Недостаточно игр")

        for x in range(LIMIT):
            if send_request:
                self.post_matches(games[x]["match_id"])
                print("DONE!", x)
            self.game.append([games[x]["match_id"], games[x]["player_slot"]])

        if send_request:
            sleep(30)

    def get_comparing_text(self, n):
        text = "Ваши показатели {}, чем показатели других игроков на {}% на вашем рейтинге"
        if n < 50:
            return text.format("хуже", round(50 - n, 2))
        else:
            return text.format("лучше", round(n - 50, 2))

    def get_text_score(self, n):
        text = "В игре Dota 2 у вас {} командная работа"
        if n < 55:
            return text.format("плохая")
        elif 55 <= n < 72:
            return text.format("средняя")
        elif 72 <= n < 83:
            return text.format("хорошая")
        elif 83 <= n:
            return text.format("отличная")

    def check_dire_radiant(self, num):
        return "radiant" if num in range(0, 128) else "dire"

    def refresh_players(self):
        x = requests.post(f"https://api.opendota.com/api/players/{self.steam_id}/refresh")
        sleep(5)

    def post_matches(self, matches_id):
        x = requests.post(f"https://api.opendota.com/api/request/{matches_id}")

    def get_response_matches(self, matches_id):
        return requests.get(f"https://api.opendota.com/api/matches/{matches_id}").json()

    def get_response_players(self, type, **params):
        return requests.get(f"https://api.opendota.com/api/players/{self.steam_id}/{type}", params=params).json()