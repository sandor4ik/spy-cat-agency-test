import requests

from rest_framework import serializers

from .models import Cat, Mission, Target

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['id', 'name', 'years_of_experience', 'breed', 'salary']

    def validate_breed(self, value):
        response = requests.get('https://api.thecatapi.com/v1/breeds')

        if response.status_code != 200:
            raise serializers.ValidationError('Could not fetch breeds from TheCatAPI')

        breeds = response.json()
        breed_names = [breed['name'].lower() for breed in breeds]

        if value.lower() not in breed_names:
            raise serializers.ValidationError(f'{value} is not a valid breed')
        
        return value

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'is_complete']

    def validate(self, attrs):
        if attrs.get('is_complete'):
            raise serializers.ValidationError("Cannot create or update a target as complete.")
        return attrs

    def create(self, validated_data):
        return Target.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.mission = validated_data.get('mission', instance.mission)
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.is_complete = validated_data.get('is_complete', instance.is_complete)
        instance.save()
        return instance

class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)
    cat = serializers.PrimaryKeyRelatedField(queryset=Cat.objects.all(), allow_null=True)

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'is_complete', 'targets']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission
    
    def update(self, instance, validated_data):
        targets_data = validated_data.pop('targets', [])
        instance.cat = validated_data.get('cat', instance.cat)
        instance.is_complete = validated_data.get('is_complete', instance.is_complete)
        instance.save()

        for target_data in targets_data:
            target_id = target_data.get('id')
            if target_id:
                target = Target.objects.get(id=target_id, mission=instance)
                if not target.is_complete:
                    target.notes = target_data.get('notes', target.notes)
                target.is_complete = target_data.get('is_complete', target.is_complete)
                target.save()
            else:
                Target.objects.create(mission=instance, **target_data)
        return instance