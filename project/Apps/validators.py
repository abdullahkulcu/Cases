import re

EMAIL_REGEX: re = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")


def validate_variables(*args):
    if args is not None and len(args) > 0:
        for variable in args:
            if variable is None:
                print("Validation : variable is None ---list index :" + str(args.index(variable)))
                return False
            func = {
                int: __integer_validate,
                str: __string_validate,
                dict: __dict_or_list_validate,
                list: __dict_or_list_validate,
                tuple: __dict_or_list_validate,
                float: __integer_validate
            }.get(type(variable), None)
            if func is not None:
                result = func(variable)
                if not result:
                    return result
    else:
        return False
    return True


def __integer_validate(variable):
    return True if variable >= 0 else False


def __string_validate(variable):
    return True if variable not in ["None", "null", "undefined", "", " ", None] else False


def __dict_or_list_validate(variable):
    return True if len(variable) > 0 else False


def email_validate(email):
    return True if bool(EMAIL_REGEX.match(email)) else False
