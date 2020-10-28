from rest_framework import serializers

from first.models import Teacher


class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField()
    gender = serializers.SerializerMethodField()
    department = serializers.CharField()
    age = serializers.IntegerField()

    def get_gender(self, obj):
        return obj.get_gender_display()

class TeacherDeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    department = serializers.CharField(max_length=20)


    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)