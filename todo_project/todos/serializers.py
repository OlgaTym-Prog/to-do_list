from rest_framework import serializers
from .models import Task, Tag


class TagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Tag
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        task = Task.objects.create(**validated_data)

        for tag_data in tags_data:
            if 'id' in tag_data and tag_data is not None:
                tag = Tag.objects.filter(id=tag_data['id']).first()
                if tag:
                    task.tags.add(tag)
            elif 'name' in tag_data and tag_data['name']:
                tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
                task.tags.add(tag)

        return task

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if tags_data:
            instance.tags.clear()
            for tag_data in tags_data:
                if 'id' in tag_data and tag_data['id'] is not None:
                    tag = Tag.objects.filter(id=tag_data['id']).first()
                    if tag:
                        instance.tags.add(tag)
                elif 'name' in tag_data:
                    tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
                    instance.tags.add(tag)

        return instance

