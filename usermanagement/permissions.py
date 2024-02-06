from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow superusers to access any user profile
        if request.user.is_superuser:
            return True

        # Allow regular users to access their own profile
        return obj == request.user