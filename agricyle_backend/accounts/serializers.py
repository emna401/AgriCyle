from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User
from .models import Declaration, Product, Order, OrderItem, GoodPractice

User = get_user_model()


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id","username","email","role","status",
            "governorate","delegation",
            "farm_name","farm_address","farm_lat","farm_lng",
        ]


class DeclarationSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Declaration
        fields = "__all__"
        read_only_fields = ["owner","owner_id","created_at","updated_at","status"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id","product","product_name","qty","unit_price"]


class OrderSerializer(serializers.ModelSerializer):
    buyer_id = serializers.IntegerField(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id","buyer_id","created_at","status","total_amount","items"]


class GoodPracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodPractice
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    password = serializers.CharField()


class ResetRequestSerializer(serializers.Serializer):
    phone = serializers.CharField()


class ResetConfirmSerializer(serializers.Serializer):
    phone = serializers.CharField()
    otp = serializers.CharField()
    new_password = serializers.CharField(min_length=8)


class CartAddItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    qty = serializers.IntegerField(min_value=1)


class CartUpdateItemSerializer(serializers.Serializer):
    qty = serializers.IntegerField(min_value=1)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'role'] 
class OrderSetStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=[s for s, _ in Order.Status.choices])

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, min_length=4)

    phone = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    email = serializers.EmailField(required=True) 

    role = serializers.ChoiceField(choices=User.Role.choices, required=False)
    governorate = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    delegation = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    farm_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    farm_address = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    farm_lat = serializers.DecimalField(max_digits=10, decimal_places=6, required=False, allow_null=True)
    farm_lng = serializers.DecimalField(max_digits=10, decimal_places=6, required=False, allow_null=True)

    # -------- VALIDATIONS --------
    def validate_username(self, v):
        if User.objects.filter(username=v).exists():
            raise serializers.ValidationError("Username déjà utilisé.")
        return v


    def validate_email(self, v):
        if v and User.objects.filter(email=v).exists():
            raise serializers.ValidationError("Email déjà utilisé.")
        return v

    # -------- CREATION --------
    def create(self, validated_data):
        password = validated_data.pop("password")
        role = validated_data.get("role") or User.Role.FARMER

        user = User(**validated_data)
        user.role = role
        user.status = User.Status.ACTIVE
        user.set_password(password)
        user.save()
        return user
