import json
from typing import TypeVar, Type, Any

T = TypeVar("T")


def serializer(obj: Any) -> bytes:
    return json.dumps(obj, default=lambda o: o.__dict__).encode()


def deserializer(c: Type[T], data) -> T:
    return c(**json.loads(data.decode()))
