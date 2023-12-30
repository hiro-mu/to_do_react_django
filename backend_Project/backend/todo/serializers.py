from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed', 'tags', )
    
    # tagsに紐づくtagの配列を渡す
    def get_tags(self, obj):
        return [tag.name for tag in obj.tag.all()]
