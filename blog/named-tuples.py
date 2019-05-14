import typing
import collections


class MyCar(typing.NamedTuple):
    colour: str
    automatic: bool


car1 = MyCar('red', True)
print(car1)
