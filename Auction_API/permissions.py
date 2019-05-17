from rest_framework import permissions

class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # The method is a safe method
            return True
        else:
            # The method isn't a safe method
            # Only owners are granted permissions for unsafe methods
            return obj.owner == request.user


### For future reference 
#https://www.programcreek.com/python/example/71197/rest_framework.permissions.SAFE_METHODS
#Need to check if logged in user is the owner of the auction
#https://stackoverflow.com/questions/43064417/whats-the-differences-between-has-object-permission-and-has-permission-in-drfp
#https://stackoverflow.com/questions/38718454/django-rest-framework-owner-permissions
