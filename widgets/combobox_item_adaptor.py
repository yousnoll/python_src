from collections.abc import Iterable
from tkinter import ttk
from typing import Final, Generic, TypeVar

from widgets.labeled_value import LabeledValue, as_labeled_value

T = TypeVar("T")

class ComboboxItemAdaptor(Generic[T]):
    def __init__(self, target: ttk.Combobox):
        self._combobox: Final = target
        self._items: tuple[LabeledValue, ...] = ()

    @property
    def items(self) -> tuple[LabeledValue[T]]:
        return tuple(self._items)

    def set_items(self, items: Iterable[T | LabeledValue[T]]):
        self._items = tuple([as_labeled_value(item) for item in items])
        labels = [item.label for item in self._items]
        self._combobox.configure(values=labels)

    @property
    def values(self) -> tuple[T]:
        return tuple([item.value for item in self._items])

    @property
    def selected_value(self) -> T | None:
        index = self.current()
        if index < 0:
            return None
        
        return self._items[index].value


combobox = ttk.Combobox()
adaptor = ComboboxItemAdaptor[int](combobox)
