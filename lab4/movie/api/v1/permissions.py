from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='developer').exists():
            return True
        return False
    def has_object_permission(self, request, view, obj):
        return True