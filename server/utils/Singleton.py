# -*- coding: utf-8 -*-

import threading

lock = threading.Lock()

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        with lock:
            if cls not in instances:
                instances[cls] = cls(*args, **kw)
            return instances[cls]
    return _singleton