from django.http import request
from rest_framework import permissions, views
from .models import *

class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if Staff.objects.get(pk=request.user.id):
            if request.method in permissions.SAFE_METHODS:
                return True
            return False
        return False  

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.sale_contact == request.user


class IsSaleTeam(permissions.BasePermission):
    def has_permission(self, request, view):
        if Staff.objects.filter(id=request.user.id, team="Sale").exists():
            return True
        return False 

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.sale_contact == request.user


class IsSupportTeam(permissions.BasePermission):
    def has_permission(self, request, view):

        if Staff.objects.filter(id=request.user.id, team="Support").exists():
            return True
        return False 

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.support_contact == request.user

