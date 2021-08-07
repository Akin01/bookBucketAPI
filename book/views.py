from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import bookSerializer
from .models import bookList
from django.http import Http404
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
@api_view(['GET','POST','DELETE'])
def allBook(request):

    querysets = bookList.objects.all()
    serializer = bookSerializer(querysets, many=True)
    
    if request.method == "GET":
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = bookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        querysets.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


@cache_page(60 * 15)
@api_view(['GET','PUT','DELETE'])
def Book(request, pk):

    try:
        querysets = bookList.objects.get(id=pk)
    except bookList.DoesNotExist:
        raise Http404

    if request.method == "GET":        
        serializer = bookSerializer(querysets)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = bookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        querysets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@cache_page(60 * 15)
@api_view(['GET','PATCH'])
def editBook(request,pk):

    try:
        querysets = bookList.objects.get(id=pk)
    except bookList.DoesNotExist:
        raise Http404

    if request.method == "GET":        
        serializer = bookSerializer(querysets)
        return Response(serializer.data)

    elif request.method == "PATCH":
        serializer = bookSerializer(querysets, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
