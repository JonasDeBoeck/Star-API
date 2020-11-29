from api.models import Star
from rest_framework import serializers
from django.contrib.auth.models import User


class StarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Star
        fields = ('id', 'name', 'star_system', 'distance')


class StarDetailedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Star
        fields = ('id', 'name', 'star_system', 'distance', 'year_of_discovery', 'apparent_magnitude', 'absolut_magnitude',
                  'spectral_class', 'parallax')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
