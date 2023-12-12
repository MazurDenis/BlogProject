# blog/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from drf_yasg.utils import swagger_auto_schema

class PostListAPIView(APIView):
    @swagger_auto_schema(responses={200: PostSerializer(many=True)})
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
      
class PostAddAPIView(APIView):
    @swagger_auto_schema(request_body=PostSerializer, responses={201: PostSerializer()})
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostGetIdAPIView(APIView):
    @swagger_auto_schema(responses={200: PostSerializer()})
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
      
class PostUpdateAPIView(APIView):
    @swagger_auto_schema(request_body=PostSerializer, responses={200: PostSerializer()})
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
class PostDeleteAPIView(APIView):
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentListAPIView(APIView):
    @swagger_auto_schema(responses={200: CommentSerializer(many=True)})
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
      
class CommentAddAPIView(APIView):
    @swagger_auto_schema(request_body=CommentSerializer, responses={201: CommentSerializer()})
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentGetIdAPIView(APIView):
    @swagger_auto_schema(responses={200: PostSerializer()})  
    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

class CommentUpdateAPIView(APIView):
    @swagger_auto_schema(request_body=PostSerializer, responses={200: PostSerializer()})
    def put(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
class CommentDeleteAPIView(APIView):      
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.
