from rest_framework import serializers
from . import Analytic


class AnalyticsSerializer(serializers.Serializer):
    """Serializers are not from models but from views."""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    desc = serializers.CharField()
    installs_30 = serializers.IntegerField()
    installs_90 = serializers.IntegerField()
    installs_365 = serializers.IntegerField()

    def __str__(self):
        return self.name

    def list(self, validated_data):
        return Analytic(id=None, **validated_data)

    def create(self, validated_data):
        return Analytic(id=None, **validated_data)

    def retrieve(self, validated_data):
        return Analytic(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
