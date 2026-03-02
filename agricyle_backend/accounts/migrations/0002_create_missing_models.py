from django.db import migrations, models
import django.db.models.deletion
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=160)),
                ("category", models.CharField(blank=True, max_length=120, null=True)),
                ("price", models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ("stock", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(default=timezone.now)),
                ("status", models.CharField(choices=[("CART", "Cart"), ("CONFIRMED", "Confirmed"), ("PREPARING", "Preparing"), ("SHIPPED", "Shipped"), ("CANCELLED", "Cancelled")], default="CART", max_length=20)),
                ("total_amount", models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ("buyer", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="orders", to="accounts.user")),
            ],
        ),
        migrations.CreateModel(
            name="Declaration",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("packaging_type", models.CharField(max_length=120)),
                ("quantity", models.PositiveIntegerField()),
                ("cert_rinsed", models.BooleanField(default=False)),
                ("pickup_date", models.DateField(blank=True, null=True)),
                ("location_address", models.CharField(blank=True, max_length=255, null=True)),
                ("location_lat", models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ("location_lng", models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ("status", models.CharField(choices=[("DRAFT", "Draft"), ("PENDING", "Pending"), ("VALIDATED", "Validated"), ("COLLECTED", "Collected")], default="PENDING", max_length=20)),
                ("created_at", models.DateTimeField(default=timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="declarations", to="accounts.user")),
            ],
        ),
        migrations.CreateModel(
            name="GoodPractice",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title_fr", models.CharField(max_length=200)),
                ("title_ar", models.CharField(max_length=200)),
                ("body_fr", models.TextField()),
                ("body_ar", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="good_practices/")),
                ("video_url", models.URLField(blank=True, null=True)),
                ("created_at", models.DateTimeField(default=timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="OTPCode",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("phone", models.CharField(max_length=30)),
                ("purpose", models.CharField(choices=[("REGISTER", "Register"), ("RESET_PASSWORD", "Reset Password")], max_length=30)),
                ("code_hash", models.CharField(max_length=255)),
                ("expires_at", models.DateTimeField()),
                ("is_used", models.BooleanField(default=False)),
                ("attempts", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="AdminAuditLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("action", models.CharField(max_length=80)),
                ("meta", models.JSONField(blank=True, default=dict)),
                ("created_at", models.DateTimeField(default=timezone.now)),
                ("admin", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="admin_logs", to="accounts.user")),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("qty", models.PositiveIntegerField(default=1)),
                ("unit_price", models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ("order", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="items", to="accounts.order")),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="accounts.product")),
            ],
        ),
    ]
