from rest_framework.permissions import BasePermission
from .models import User


class IsNotSuspended(BasePermission):
    def has_permission(self, request, view):
        u = request.user
        if not u or not u.is_authenticated:
            return False
        return u.status == User.Status.ACTIVE


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        u = request.user
        if u.is_authenticated and u.is_admin_role():
            return True
        # obj may be Declaration (owner) or Order (buyer)
        owner_id = getattr(obj, "owner_id", None)
        buyer_id = getattr(obj, "buyer_id", None)
        return (owner_id is not None and owner_id == u.id) or (buyer_id is not None and buyer_id == u.id)


class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin_role()
