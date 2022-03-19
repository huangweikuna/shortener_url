import random
import string
import zlib
from functools import lru_cache

from django.conf import settings
from django.core.cache import cache
from django.core.validators import URLValidator

from shortener.models import Url


class ShortenerService(object):
    def __init__(self):
        self.sentinel = object()
        self.validator = URLValidator()

    # @lru_cache(maxsize=settings.LRU_CACHE_LENGTH)
    def get_url(self, code):
        url = cache.get(code, self.sentinel)
        if url is self.sentinel:
            print("redis")
            url_obj = Url.objects.get(code_hash=zlib.crc32(code.encode('utf8')), code=code)
            url = url_obj.url
            cache.set(code, url, timeout=random.randint(settings.REDIS_MAX_EX, settings.REDIS_MIN_EX))
        return url

    # 一级缓存
    @lru_cache(maxsize=settings.LRU_CACHE_LENGTH)
    def new_url(self, url):
        self._check_url(url)
        # 二级缓存
        code = cache.get(url, self.sentinel)
        if code is self.sentinel:
            print("redis")
            url_obj = self._put_if_absent(url)
            code = url_obj[0].code
            cache.set(url, code, timeout=random.randint(settings.REDIS_MAX_EX, settings.REDIS_MIN_EX))
            cache.set(code, url, timeout=random.randint(settings.REDIS_MAX_EX, settings.REDIS_MIN_EX))
        return code

    def _put_if_absent(self, url):
        code = self._random_code()
        url_hash = zlib.crc32(url.encode('utf8'))
        return Url.objects.get_or_create({
            "url": url,
            "url_hash": url_hash,
            "code": code,
            "code_hash": zlib.crc32(code.encode('utf8'))
        }, url_hash=url_hash, url=url)

    def _check_url(self, url):
        self.validator(url)

    def _random_code(self):
        return ''.join(random.sample(string.ascii_letters + string.digits, settings.CODE_LENGTH))
