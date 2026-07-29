import redis
from django.conf import settings
from datetime import timedelta


redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=0,
    decode_responses=True,
)

def save_otp(phone_number: str, otp_code: str):
    redis_client.set(
        phone_number, otp_code, ex=timedelta(minutes=5)
    )

def get_otp(phone_number: str):
    return redis_client.get(phone_number)

def delete_otp(phone_number: str):
    redis_client.delete(phone_number)

def can_request_otp(phone_number: str):
    key = f"otp_limit:{phone_number}"

    return redis_client.set(key, 1, ex=60, nx=True)

def increase_attempt(phone_number: str):
    key = f"otp_attempt:{phone_number}"

    attempts = redis_client.incr(key)
    redis_client.expire(key, 300)
    return attempts

def delete_attempt(phone_number: str):
    redis_client.delete(f"otp_attempt:{phone_number}")