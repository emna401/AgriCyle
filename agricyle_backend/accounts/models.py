from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    class Role(models.TextChoices):
        FARMER = "FARMER", "Farmer"
        BENEFICIARY = "BENEFICIARY", "Beneficiary"
        DUAL = "DUAL", "Dual"
        ADMIN = "ADMIN", "Admin"
        SUPERADMIN = "SUPERADMIN", "SuperAdmin"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        PENDING = "PENDING", "Pending"
        SUSPENDED = "SUSPENDED", "Suspended"
        BLOCKED = "BLOCKED", "Blocked"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.FARMER)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)

    phone = models.CharField(max_length=30, blank=True, null=True, unique=True)
    governorate = models.CharField(max_length=100, blank=True, null=True)
    delegation = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    # FARM
    farm_name = models.CharField(max_length=120, blank=True, null=True)
    farm_address = models.CharField(max_length=255, blank=True, null=True)
    farm_lat = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    farm_lng = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

    def is_admin_role(self) -> bool:
        return self.role in {self.Role.ADMIN, self.Role.SUPERADMIN}


class Declaration(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        PENDING = "PENDING", "Pending"
        VALIDATED = "VALIDATED", "Validated"
        COLLECTED = "COLLECTED", "Collected"

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="declarations")
    packaging_type = models.CharField(max_length=120)
    quantity = models.PositiveIntegerField()
    cert_rinsed = models.BooleanField(default=False)

    pickup_date = models.DateField(blank=True, null=True)

    # location of declaration (could be farm or storage)
    location_address = models.CharField(max_length=255, blank=True, null=True)
    location_lat = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    location_lng = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=160)
    category = models.CharField(max_length=120, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)


class Order(models.Model):
    class Status(models.TextChoices):
        CART = "CART", "Cart"
        CONFIRMED = "CONFIRMED", "Confirmed"
        PREPARING = "PREPARING", "Preparing"
        SHIPPED = "SHIPPED", "Shipped"
        CANCELLED = "CANCELLED", "Cancelled"

    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.CART)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def recalc_total(self):
        total = 0.0
        for it in self.items.all():
            total += float(it.unit_price) * int(it.qty)
        self.total_amount = total
        self.save(update_fields=["total_amount"])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class GoodPractice(models.Model):
    title_fr = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200)
    body_fr = models.TextField()
    body_ar = models.TextField()
    image = models.ImageField(upload_to="good_practices/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)


class OTPCode(models.Model):
    class Purpose(models.TextChoices):
        RESET_PASSWORD = 'reset_password', 'Réinitialisation de mot de passe'

    email = models.EmailField()
    code = models.CharField(max_length=6)
    code_hash = models.CharField(max_length=64)  # Pour stocker le hash du code OTP
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    purpose = models.CharField(max_length=20, choices=Purpose.choices)
    attempts = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP pour {self.email} - Code: {self.code}"

class AdminAuditLog(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_logs")
    action = models.CharField(max_length=80)
    meta = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(default=timezone.now)



