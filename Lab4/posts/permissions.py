from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # pozwolenie do odczytu
        if request.method in permissions.SAFE_METHODS:
            return True

        # prawo do zapisu ma autor postu
        return obj.author == request.user