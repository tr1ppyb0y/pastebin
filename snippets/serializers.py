# This file is similar to Django's forms.py
# Serialization and Deserialization of the snippet instance
# into representations such as JSON.

from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']