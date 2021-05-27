import copy
import json
import requests
from analytics.overwatch import helper
from analytics.overwatch.error import OverwatchError
from main.models import OverwatchResult

TEMPLATE = "Ваши ТОП-3 персонажи:  \n" \
           "Ваш средний урон за 10 минут - {}   \n" \
           "Ваш уровень игры на роли DAMAGE: {} \n" \
           "Ваш уровень игры на роли SUPPORT: {} \n" \
           "Ваш уровень игры на роли TANK: {} \n" \


def overvatch_start_analysing(request):
    user = request.user
    battle_tag = user.talantuser.blizzard_battletag

    overwatch = Overwatch(battle_tag, user.talantuser.overwatch_result)


class Overwatch:
    def __init__(self, nickname, db_entry: OverwatchResult):
        self.db = db_entry
        self.nickname = nickname
        self.url = 'https://public-api.tracker.gg/v2/overwatch/standard/profile/battlenet/'
        self.main_stats = {
            "allDamageDoneAvgPer10Min": 0,
            "barrierDamageDoneAvgPer10Min": 0,
            "deathsAvgPer10Min": 0,
            "eliminationsAvgPer10Min": 0,
            "finalBlowsAvgPer10Min": 0,
            "healingDoneAvgPer10Min": 0,
            "heroDamageDoneAvgPer10Min": 0,
            "objectiveKillsAvgPer10Min": 0,
            "objectiveTimeAvgPer10Min": 0,
            "soloKillsAvgPer10Min": 0,
            "timeSpentOnFireAvgPer10Min": 0
        }
        with open('mean_overwatch_data2.json', 'r') as r:
            self.mean_stats = json.loads(r.read())

        with open('avg_over_responce2.json', 'r') as r:
            self.avg_responce = json.loads(r.read())
        self.role_coefs = helper.over_role_coefs
        self.hero_roles = helper.over_hero_roles

    def get_pro_stats(self):
        with open('1.txt', 'r') as r:
            names = r.read().split('\n')
        print(len(names))
        mean_data = {'tank': self.main_stats.copy(), 'damage': self.main_stats.copy(),
                     'support': self.main_stats.copy(), 'normal': self.main_stats.copy(), }
        for role in mean_data:
            mean_data[role]['count'] = 0
        c = 0
        for name in names:
            print(c)
            try:
                stats = self.get_stats(name)
                role = stats['best_role']
                for key in mean_data[role]:
                    if key in stats:
                        mean_data[role][key] += stats[key]
                mean_data[role]['count'] += 1
                role = 'normal'
                for key in mean_data[role]:
                    if key in stats:
                        mean_data[role][key] += stats[key]
                mean_data[role]['count'] += 1
                c += 1
            except Exception as e:
                print(e)
            if c % 5 == 0:
                with open('mean_overwatch_data_reserve2.txt', 'w') as write:
                    write.write(str(mean_data) + str(c))

        print(mean_data)
        for role in mean_data:
            for key in mean_data[role]:
                mean_data[role][key] /= mean_data[role]['count']
        print(mean_data)

        with open('mean_overwatch_data2.json', 'w') as write:
            write.write(str(mean_data) + str(c))

    def count_mean(self):
        with open('1.txt', 'r') as r:
            names = r.read().split('\n')
        print(len(names))

        avg = {'normal': self.main_stats.copy(), 'damage': self.main_stats.copy(),
               'support': self.main_stats.copy(), 'tank': self.main_stats.copy()}
        c = 0
        for name in names[:]:
            print(c)
            try:
                stats = self.get_stats(name)
                for role in avg:
                    if 'count' in stats[role] and stats[role]['count'] > 0:
                        if not 'count' in avg[role]:
                            avg[role]['count'] = 0
                        avg[role]['count'] += 1
                        for key in avg[role]:
                            if key != 'count':
                                avg[role][key] += stats[role][key]
                c += 1

                if (c - 1) % 20 == 0:
                    with open("avg_over_responce_reserve2.json", "w") as write_file:
                        json.dump(avg, write_file)
            except Exception as e:
                print(e)
        for role in avg:

            for key in avg[role]:
                if 'count' in avg[role] and avg[role]['count'] > 0:
                    avg[role][key] /= avg[role]['count']

        with open("avg_over_responce2.json", "w") as write_file:
            json.dump(avg, write_file)

    def get_stats(self):
        url = f'https://ow-api.com/v1/stats/pc/eu/{self.nickname}/complete'
        response = requests.get(url)
        data = response.json()
        parsed = self.parse_data(data)
        processed = self.process_data(copy.deepcopy(parsed))
        if data['gamesWon'] == 0:
            self.db.result = False
            self.db.error = "Вы не играете в эту игру"
            self.db.save()
            raise OverwatchError("Вы не играете в эту игру")
        for role in parsed:
            if 'score' in processed[role]:
                parsed[role]['score'] = processed[role]['score']
                val = parsed[role]['score']
                rate = ''
                if 400 < val < 525:
                    rate = ['хорошая', "хороший"]
                elif 300 < val < 400:
                    rate = ['средняя', "средний"]
                elif val < 300:
                    rate = ['плохая', "плохой"]
                elif 525 < val < 580:
                    rate = ['отличная', "отличный"]

                parsed[role]['rating'] = rate

        parsed['roles'] = []
        for role in ['damage', 'support', 'tank']:
            parsed['roles'].append({'role': role, 'score': parsed[role]['score'], 'rating': parsed[role]['rating']})
            parsed.pop(role)
        return_dict = {'player': parsed, 'avg': copy.deepcopy(self.avg_responce).pop('normal')}

        info = return_dict

        self.db.result = True
        self.db.result_num = round(info["player"]["normal"]["score"], 2)
        heroes = [x[0] for x in sorted(list(info["player"]["heroTimes"].items()), key=lambda i: i[1], reverse=True)[:3]]
        self.db.result_big_str = TEMPLATE.format(", ".join(heroes),
                                                 info["player"]["normal"]["allDamageDoneAvgPer10Min"],
                                                 info["player"]["roles"][0]["rating"][1],
                                                 info["player"]["roles"][1]["rating"][1],
                                                 info["player"]["roles"][2]["rating"][1])
        self.db.result_str = f"В игре Overwatch у вас {info['player']['normal']['rating'][0]} командная работа"
        self.db.result_json = json.dumps(info)
        self.db.save()

    def parse_data(self, data):
        parsed_data = {'normal': self.main_stats.copy(), 'damage': self.main_stats.copy(),
                       'support': self.main_stats.copy(), 'tank': self.main_stats.copy()}
        hero_stats = {}
        stat_types = ['competitiveStats', 'quickPlayStats']
        for stat_type in stat_types:
            if stat_type in data and 'careerStats' in data[stat_type] and data[stat_type]['careerStats'] is not None:
                competitive_stats = data[stat_type]['careerStats']  # ['allHeroes']
                for hero in competitive_stats:

                    if 'average' in competitive_stats[hero] and competitive_stats[hero]['average'] is not None:
                        avg_stats = competitive_stats[hero]['average']
                        for stat in self.main_stats:
                            if stat in avg_stats:
                                val = avg_stats[stat]
                                if type(val) == str:
                                    val = int(val[-5:-3]) * 60 + int(val[-2:])
                                parsed_data[self.hero_roles[hero]][stat] += val
                        if not 'count' in parsed_data[self.hero_roles[hero]]:
                            parsed_data[self.hero_roles[hero]]['count'] = 0
                        parsed_data[self.hero_roles[hero]]['count'] += 1

                        time_played = competitive_stats[hero]['game']['timePlayed']
                        if len(time_played) == 5:
                            time_played = int(time_played[-5:-3]) * 60 + int(time_played[-2:])
                        elif len(time_played) == 8:
                            time_played = int(time_played[-len(time_played):-6]) * 3600 + int(
                                time_played[-5:-3]) * 60 + int(
                                time_played[-2:])
                        else:
                            time_played = 0
                        if not 'timePlayed' in parsed_data[self.hero_roles[hero]]:
                            parsed_data[self.hero_roles[hero]]['timePlayed'] = 0
                        parsed_data[self.hero_roles[hero]]['timePlayed'] += time_played

                        if not hero in hero_stats:
                            hero_stats[hero] = 0
                        hero_stats[hero] += time_played
                for role in parsed_data:
                    for stat in parsed_data[role]:
                        if 'count' in parsed_data[role] and parsed_data[role]['count'] > 0:
                            parsed_data[role][stat] /= parsed_data[role]['count']
                hero_stats.pop('allHeroes')
                parsed_data['heroTimes'] = hero_stats
        return parsed_data

    def process_data(self, data):
        processed_data = data.copy()

        for role in self.role_coefs:
            coeffs = self.role_coefs[role]
            summ = 0
            for key in coeffs:
                mean_stats = self.avg_responce[role]
                if key in mean_stats:
                    processed_data[role][key] /= mean_stats[key]
                    if key == 'deathsAvgPer10Min':
                        processed_data[role][key] = 1 + (1 - processed_data[role][key])
                    processed_data[role][key] *= coeffs[key]
                    summ += processed_data[role][key]

            processed_data[role]['score'] = summ
        return processed_data