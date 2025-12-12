from time import time

_cache = {}

def get(key):
    item = _cache.get(key)
    if not item or item[1] < time():
        return None
    return item[0]

def set(key, value, ttl):
    _cache[key] = (value, time() + ttl)
