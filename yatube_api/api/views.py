# TODO:  Напишите свой вариант
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters
from rest_framework.viewsets import ReadOnlyModelViewSet

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
from posts.models import Post, Group, Follow


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        return (get_object_or_404(Post, id=self.kwargs['post_id'])
                .comments.all())

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        author = self.request.user
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=author, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ('following__username', 'user__username')
    pagination_class = None

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
