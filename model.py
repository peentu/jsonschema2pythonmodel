# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = Modelfromdict(json.loads(json_string))

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
    veggieLike: bool
    """The name of the vegetable."""
    veggieName: str

    def __init__(self, veggieLike: bool, veggieName: str) -> None:
        self.veggieLike = veggieLike
        self.veggieName = veggieName

    @staticmethod
    def from_dict(obj: Any) -> 'Veggie':
        assert isinstance(obj, dict)
        veggieLike = from_bool(obj.get("veggieLike"))
        veggieName = from_str(obj.get("veggieName"))
        return Veggie(veggieLike, veggieName)

    def to_dict(self) -> dict:
        result: dict = {}
        result["veggieLike"] = from_bool(self.veggieLike)
        result["veggieName"] = from_str(self.veggieName)
        return result


class Model:
    """A representation of a person, company, organization, or place"""
    fruits: Optional[List[str]]
    vegetables: Optional[List[Veggie]]

    def __init__(self, fruits: Optional[List[str]], vegetables: Optional[List[Veggie]]) -> None:
        self.fruits = fruits
        self.vegetables = vegetables

    @staticmethod
    def from_dict(obj: Any) -> 'Model':
        assert isinstance(obj, dict)
        fruits = from_union([lambda x: from_list(from_str, x), from_none], obj.get("fruits"))
        vegetables = from_union([lambda x: from_list(Veggie.from_dict, x), from_none], obj.get("vegetables"))
        return Model(fruits, vegetables)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fruits"] = from_union([lambda x: from_list(from_str, x), from_none], self.fruits)
        result["vegetables"] = from_union([lambda x: from_list(lambda x: to_class(Veggie, x), x), from_none], self.vegetables)
        return result


def Modelfromdict(s: Any) -> Model:
    return Model.from_dict(s)


def Modeltodict(x: Model) -> Any:
    return to_class(Model, x)
