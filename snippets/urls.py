from django.urls import path
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import SnippetViewSet, UserViewSet, api_root

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_class=[StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', api_root),
    path('user/', user_list, name='user-list'),
    path('user/<int:pk>', user_detail, name='user-detail'),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight')
]

urlpatterns = format_suffix_patterns(urlpatterns)