from Camper.ExceptionCatcher import CamperException
from django.conf import settings


def __error_callback(err):
    print(err)


def catch(default_value=None, default_method=None, error_callback=None):
    return CamperException().exception_catcher(
        default=default_value,
        error_callback=__error_callback if error_callback is None else error_callback,
        record=False,
        callback=default_method
    )

