# app/services/sleep.py
from typing import Optional
from functools import wraps
import anyio

def with_sleep(delay_ms: Optional[int] = 100):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if delay_ms > 0:
                print(f"Simulating delay of {delay_ms} ms")
                await anyio.sleep(delay_ms / 1000)
            return await func(*args, **kwargs)
        return wrapper
    return decorator
