from rest_framework import permissions


class AdminAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'retrieve':
            return request.user.is_superuser
        else:
            return False
