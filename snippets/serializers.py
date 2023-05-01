# This file is similar to Django's forms.py
# Serialization and Deserialization of the snippet instance
# into representations such as JSON.

from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth import get_user_model


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']


# snippets is a reverse relationship on the User model.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'snippets']