from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Declaration, Product, Order, OrderItem, GoodPractice, OTPCode, AdminAuditLog

User = get_user_model()

admin.site.register(User)
admin.site.register(Declaration)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(GoodPractice)
admin.site.register(OTPCode)
admin.site.register(AdminAuditLog)
