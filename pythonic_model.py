# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = pythonic_model_from_dict(json.loads(json_string))

from typing import Any, Optional, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Veggie:
    """Do I like this vegetable?"""
    veggie_like: bool
    """The name of the vegetable."""
    veggie_name: str

    def __init__(self, veggie_like: bool, veggie_name: str) -> None:
        self.veggie_like = veggie_like
        self.veggie_name = veggie_name

    @staticmethod
    def from_dict(obj: Any) -> 'Veggie':
        assert isinstance(obj, dict)
        veggie_like = from_bool(obj.get("veggieLike"))
        veggie_name = from_str(obj.get("veggieName"))
        return Veggie(veggie_like, veggie_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["veggieLike"] = from_bool(self.veggie_like)
        result["veggieName"] = from_str(self.veggie_name)
        return result


class PythonicModel:
    """A representation of a person, company, organization, or place"""
    fruits: Optional[List[str]]
    vegetables: Optional[List[Veggie]]

    def __init__(self, fruits: Optional[List[str]], vegetables: Optional[List[Veggie]]) -> None:
        self.fruits = fruits
        self.vegetables = vegetables

    @staticmethod
    def from_dict(obj: Any) -> 'PythonicModel':
        assert isinstance(obj, dict)
        fruits = from_union([lambda x: from_list(from_str, x), from_none], obj.get("fruits"))
        vegetables = from_union([lambda x: from_list(Veggie.from_dict, x), from_none], obj.get("vegetables"))
        return PythonicModel(fruits, vegetables)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fruits"] = from_union([lambda x: from_list(from_str, x), from_none], self.fruits)
        result["vegetables"] = from_union([lambda x: from_list(lambda x: to_class(Veggie, x), x), from_none], self.vegetables)
        return result


def pythonic_model_from_dict(s: Any) -> PythonicModel:
    return PythonicModel.from_dict(s)


def pythonic_model_to_dict(x: PythonicModel) -> Any:
    return to_class(PythonicModel, x)
