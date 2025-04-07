from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Anime, Bookmark, WatchHistory, Review
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "member_since", "bio")


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = "__all__"


class BookmarkSerializer(serializers.ModelSerializer):
    anime = AnimeSerializer(read_only=True)

    class Meta:
        model = Bookmark
        fields = ("id", "anime", "created_at")

    def create(self, validated_data):
        anime_data = validated_data.pop("anime")
        anime, _ = Anime.objects.get_or_create(**anime_data)
        return Bookmark.objects.create(anime=anime, **validated_data)


class WatchHistorySerializer(serializers.ModelSerializer):
    anime = AnimeSerializer(read_only=True)

    class Meta:
        model = WatchHistory
        fields = ("id", "anime", "episode", "last_watched")


class ReviewSerializer(serializers.ModelSerializer):
    anime = AnimeSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"
