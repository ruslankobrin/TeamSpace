from django.contrib.auth.models import User
from rest_framework import serializers

from teamapp.models import Person, Team


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]


class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Person
        fields = "__all__"
        read_only = True

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        team_ids = validated_data.pop("teams", [])

        user = User.objects.create(**user_data)

        person = Person.objects.create(user=user, **validated_data)
        person.teams.set(team_ids)
        return person


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return instance.name


class TeamAllSerializer(serializers.ModelSerializer):
    team_id = TeamField(queryset=Team.objects.all())

    class Meta:
        model = Team
        fields = ("team_id",)
