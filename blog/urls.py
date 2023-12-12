from django.urls import path
from .views import (
    PostListAPIView, PostAddAPIView, PostGetIdAPIView,
    PostUpdateAPIView, PostDeleteAPIView,
    CommentListAPIView, CommentAddAPIView, CommentGetIdAPIView,
    CommentUpdateAPIView, CommentDeleteAPIView
)

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/add/', PostAddAPIView.as_view(), name='post-add'),
    path('posts/<int:pk>/', PostGetIdAPIView.as_view(), name='post-detail'),
    path('posts/<int:pk>/update/', PostUpdateAPIView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteAPIView.as_view(), name='post-delete'),

    path('comments/', CommentListAPIView.as_view(), name='comment-list'),
    path('comments/add/', CommentAddAPIView.as_view(), name='comment-add'),
    path('comments/<int:pk>/', CommentGetIdAPIView.as_view(), name='comment-detail'),
    path('comments/<int:pk>/update/', CommentUpdateAPIView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteAPIView.as_view(), name='comment-delete'),
]
