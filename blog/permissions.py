from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Read-only permissions are allowed for any request
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        """
        Write permissions are only allowed to the author of a post
        """
        return obj.author ==request.user


class BasePermission(object):
    """
    A base class from which all permission classes should inherit.
    """

    def has_permission(self, request, view):
        """
        Returns `True` if permission granted, else `False`
        """
        return True
