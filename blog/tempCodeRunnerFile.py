class BasePermission(object):
    # A base class from which all permission classes should inherit.

    def has_permission(self, request, view):
        # Returns `True` if permission granted, else `False`
        return True
