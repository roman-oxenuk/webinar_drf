from rest_framework import serializers

from posts_models.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'text', 'created_at', 'author']

    def validate_text(self, value):
        if 'fuck' in value:
            raise serializers.ValidationError('Недопустимое слово в тексте')
        return value
