from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer

@api_view(['GET'])
# @permission_classes([AllowAny])
@permission_classes([])
def get_blogs(request):
    paginator = PageNumberPagination()
    paginator.page_size = 6
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-created_at')
    result_page = paginator.paginate_queryset(blogs, request)
    serializer = BlogSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
# @permission_classes([AllowAny])
@permission_classes([])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        category_ids = request.data.get('category', [])
        categories = Category.objects.filter(pk__in=category_ids)
        blog = serializer.save(created_by_id=request.data.get('created_by'), categories=categories)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
@authentication_classes([])
@permission_classes([])
def update_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BlogSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([])
@permission_classes([])
def delete_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
