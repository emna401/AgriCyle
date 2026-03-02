from django import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    # Importez toutes les fonctions nécessaires
    admin_farmers_map,
    export_users_xlsx,
    register,
    token_login, 
    reset_password_request, 
    reset_password_confirm,
    api_health,
    stats_farmer,
    stats_beneficiary,
    stats_admin,
    export_orders_report_xlsx,
    export_orders_report_pdf,
    # Viewsets
    MeViewSet,
    DeclarationViewSet,
    ProductViewSet,
    OrderViewSet,
    GoodPracticeViewSet,
    UserViewSet,
    # Fonctions admin (NOUVELLES)
    get_users,
    admin_update_user,
    suspend_user,
    activate_user,
    reset_user_password,
    delete_user,
    
)

router = DefaultRouter()
router.register("me", MeViewSet, basename="me")
router.register("declarations", DeclarationViewSet, basename="declarations")
router.register("products", ProductViewSet, basename="products")
router.register("orders", OrderViewSet, basename="orders")
router.register("good-practices", GoodPracticeViewSet, basename="good-practices")
router.register("users", UserViewSet, basename="user")

urlpatterns = [
    path("health/", api_health, name="api-health"),
    path("", include(router.urls)),
    
    # auth
    path("auth/token/", token_login, name="token-login"),
    path("auth/reset/request/", reset_password_request, name="reset-password-request"),
    path("auth/reset/confirm/", reset_password_confirm, name="reset-password-confirm"),
    path("auth/register/", register, name="register"),
    
    # stats
    path("stats/farmer/", stats_farmer, name="stats-farmer"),
    path("stats/beneficiary/", stats_beneficiary, name="stats-beneficiary"),
    path("stats/admin/", stats_admin, name="stats-admin"),
    path("farmers-map/admin", admin_farmers_map, name="admin_farmers_map"),

    # exports
    path("exports/orders_report.xlsx", export_orders_report_xlsx, name="export-orders-xlsx"),
    path("exports/orders_report.pdf", export_orders_report_pdf, name="export-orders-pdf"),
    
    # Admin user management endpoints (NOUVEAUX)
    path("admin/users/", get_users, name="get-users"),
    path("admin/users/<int:user_id>/", admin_update_user, name="admin-update-user"),
    path("admin/users/<int:user_id>/suspend/", suspend_user, name="suspend-user"),
    path("admin/users/<int:user_id>/activate/", activate_user, name="activate-user"),
    path("admin/users/<int:user_id>/reset-password/", reset_user_password, name="reset-user-password"),
    path("admin/users/<int:user_id>/delete/", delete_user, name="delete-user"),
    path('admin/users/export-excel/', export_users_xlsx, name='export_users_xlsx')
]