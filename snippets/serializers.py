# This file is similar to Django's forms.py
# Serialization and Deserialization of the snippet instance
# into representations such as JSON.

from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth import get_user_model


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


# snippets is a reverse relationship on the User model.
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'snippets']