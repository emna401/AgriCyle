import random
import hashlib
from datetime import timedelta
from django.utils import timezone


def generate_otp_code() -> str:
    return str(random.randint(100000, 999999))


def hash_code(code: str) -> str:
    return hashlib.sha256(code.encode("utf-8")).hexdigest()


def otp_expiry(minutes: int = 15):
    return timezone.now() + timedelta(minutes=minutes)
