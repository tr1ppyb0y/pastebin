from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    '''
    List all code snippets, or create a new snippet
    '''

    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.error, status=HTTP_400_BAD_REQUEST)
    



@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    '''
    Retrieve, update or delete a code snippet.
    '''

    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=False)
    
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data, status=HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.error, status=HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    