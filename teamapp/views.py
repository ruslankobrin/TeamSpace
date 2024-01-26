from rest_framework import viewsets
from .models import Person, Team
from .serializers import PersonSerializer, TeamSerializer, TeamAllSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def check_args(self, request):
        person = self.get_object()
        team_id = request.data.get("team_id")
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"error": "Team not found"}, status=400)
        return person, team

    @action(detail=True, methods=["post"], serializer_class=TeamAllSerializer)
    def move_person_to_team(self, request, pk=None):
        person, team = self.check_args(request)

        person.teams.add(team)
        serializer = PersonSerializer(self.get_object())
        return Response(serializer.data)

    @action(detail=True, methods=["post"], serializer_class=TeamAllSerializer)
    def remove_person_to_team(self, request, pk=None):
        person, team = self.check_args(request)

        person.teams.remove(team)
        serializer = PersonSerializer(self.get_object())
        return Response(serializer.data)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
