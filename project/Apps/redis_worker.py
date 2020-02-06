from redis import Redis
from django.conf import settings
from .exception_catcher import catch

connection = Redis(host="127.0.0.1", port=6379, db=0, charset="utf-8",
                   decode_responses=True)


class Redis:

    @staticmethod
    @catch()
    def set_array_data(key, value):
        try:
            redis_method = connection.pipeline()
            if key is not None and type(key) == str and value is not None:
                redis_method.lrem(key, 0, str(value))
                redis_method.lpush(key, value)
                redis_method.execute()
            else:
                print("Key not exist")
        except  Exception as e:
            print(e)

    @staticmethod
    def get_array(key, default_value=None):
        try:
            redis_method = connection.pipeline()
            if key is not None and type(key) == str:
                redis_method.lrange(key, 0, -1)
                data = redis_method.execute()[0]
                if data is None:
                    return default_value
                return data
        except Exception as e:
            print(e)
            return default_value
