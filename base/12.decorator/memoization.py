import time
import hashlib
import pickle

cache = {}


def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration


def compute_key(func, args, kw):
    # 序列化/反序列化一个对象,这里是用pickle模块对函数和参数对象进行序列化为一个hash值
    key = pickle.dumps((func.__name__, args, kw))
    # hashlib是一个提供MD5和sh1的一个库，该结果保存在一个全局字典中
    return hashlib.sha1(key).hexdigest()


def memoize(duration=10):
    def _memoize(func):
        def __memoize(*args, **kw):
            key = compute_key(func, args, kw)

            # do we have it already
            if (key in cache and
                    not is_obsolete(cache[key], duration)):
                return cache[key]['value']

            # computing
            result = func(*args, **kw)
            # storing the result
            cache[key] = {'value': result, 'time': time.time()}
            return result

        return __memoize

    return _memoize


@memoize(1)
def very_very_complex_stuff(a, b, c):
    print('重新结算')
    return a + b + c


print(very_very_complex_stuff(2, 2, 2))
print(very_very_complex_stuff(2, 2, 2))
print(very_very_complex_stuff(2, 2, 2))
print(very_very_complex_stuff(2, 2, 2))
print(very_very_complex_stuff(2, 2, 2))
print(very_very_complex_stuff(2, 2, 2))

print(very_very_complex_stuff(2, 2, 2))
print(very_very_complex_stuff(2, 2, 2))
print(very_very_complex_stuff(2, 2, 2))
print(very_very_complex_stuff(2, 2, 2))
