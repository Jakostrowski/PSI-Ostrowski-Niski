from rest_framework import permissions

class Authen(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.method == 'GET':
            return True
        if request.method == "POST":
            return False
        return request.user and request.user.is_authenticated