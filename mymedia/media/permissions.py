from rest_framework import permissions
import logging

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view/edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read/Write permissions are only allowed to the owner of the medium
        print('username: ' + request.user.username + ' password: ' + request.user.password)
        print('auth: ' + str(request.auth))
        print('is_authenticated: ' + str(request.user.is_authenticated()))
        return obj.owner == request.user