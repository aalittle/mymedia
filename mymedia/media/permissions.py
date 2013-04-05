from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view/edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read/Write permissions are only allowed to the owner of the medium
        
        return obj.owner == request.user