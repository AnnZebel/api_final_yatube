from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):

    # def has_object_permission(self, request, view, obj):
    #     return (request.method in permissions.SAFE_METHODS
    #             or obj.author == request.user)
    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user or request.method
                in permissions.SAFE_METHODS)
