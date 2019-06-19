""" Django Rest Framework implementation of 'Blog Project'

This module is in place from a previous stage of the development cycle when
I was building the blog with a React front end and passing the blog data to and
from the front end using Django Rest Framework.

TODO: Pick up project again once deployed with standard Django templates.
"""

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """Read-only permissions for any request"""
        if request.method in permissions.SAFE_METHODS:
            return True

        """Write permissions for author only"""
        return obj.author == request.user
