from celery import current_app
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .. import serializers
from .. import tasks


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = serializers.CurrentUserSerializer(request.user)
        return Response(serializer.data)


class CurrentTalentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = serializers.TalentUserSerializer(request.user.talantuser)
        return Response(serializer.data)


class CurrentUserDotaResultView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = serializers.DotaResultSerializer(request.user.talantuser.dota_result)
        return Response(serializer.data)


class CurrentUserCsResultView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = serializers.CsResultSerializer(request.user.talantuser.cs_result)
        return Response(serializer.data)


class CurrentUserOverwatchResultView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = serializers.OverwatchResultSerializer(request.user.talantuser.overwatch_result)
        return Response(serializer.data)


class CsAnalyseStart(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ctx = {'error': None}
        user = request.user

        if user.talantuser.steam_id is None:
            ctx['error'] = "Привяжите Steam к аккаунту"
            return Response(ctx)
        if user.talantuser.cs_task:
            ctx['error'] = 'Задача уже в очереди'
            return Response(ctx)
        task = tasks.cs_count.delay(user.pk)
        user.talantuser.cs_task = task.id
        user.talantuser.save()

        ctx['task_id'] = task.id

        return Response(ctx)


class DotaAnalyseStart(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ctx = {'error': None, 'task_id': None}
        user = request.user

        if user.talantuser.steam_id is None:
            ctx['error'] = "Привяжите Steam к аккаунту"
            return Response(ctx)
        if user.talantuser.dota_task:
            ctx['error'] = 'Задача уже в очереди'
            return Response(ctx)

        task = tasks.dota_count.delay(user.pk)
        user.talantuser.dota_task = task.id
        user.talantuser.save()

        ctx['task_id'] = task.id

        return Response(ctx)


class OverwatchAnalyseStart(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ctx = {'error': None, 'task_id': None}
        user = request.user

        if user.talantuser.blizzard_battletag is None:
            ctx['error'] = "Привяжите BattleNet к аккаунту"
            return Response(ctx)
        if user.talantuser.overwatch_task:
            ctx['error'] = 'Задача уже в очереди'
            return Response(ctx)

        task = tasks.overwatch_count.delay(user.pk)
        user.talantuser.overwatch_task = task.id
        user.talantuser.save()

        ctx['task_id'] = task.id

        return Response(ctx)


class TaskStatus(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        task_id = request.query_params.get('task')
        ctx = {}

        task = current_app.AsyncResult(task_id)
        ctx['status'] = task.status  # SUCCESS, FAILURE

        return Response(ctx)
