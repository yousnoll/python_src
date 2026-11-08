from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")

@dataclass(frozen=True, slots=True, order=True)
class LabeledValue(Generic[T]):
    value: T
    label: str = field(compare=False)

    def __str__(self) -> str:
        return self.label

def as_labeled_value(value: T | LabeledValue[T]) -> LabeledValue[T]:
    if isinstance(value, LabeledValue):
        return value

    return LabeledValue[T](value=value, label=str(value))