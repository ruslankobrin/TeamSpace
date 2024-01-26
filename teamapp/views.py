from rest_framework import viewsets
from .models import Person, Team
from .serializers import PersonSerializer, TeamSerializer, TeamAllSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @action(detail=True, methods=["post"], serializer_class=TeamAllSerializer)
    def move_to_team(self, request, pk=None):
        person = self.get_object()
        team_id = request.data.get("team_id")
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"error": "Team not found"}, status=400)
        person.teams.add(team)
        serializer = PersonSerializer(self.get_object())
        return Response(serializer.data)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
