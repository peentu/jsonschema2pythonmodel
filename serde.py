import json
from typing import TypeVar, Type

T = TypeVar("T")


def serializer(obj):
    return json.dumps(obj, default=lambda o: o.__dict__).encode()


def deserializer(c: Type[T], data):
    return c(**json.loads(data.decode()))
