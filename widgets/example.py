from collections.abc import Callable
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, TypeVar

from widgets.column import Column

T = TypeVar("T")

# NOTE: 値 + ラベルの型を考える
# こうすることで、比較も値基準になるので、値そのものであると表せるか？
@dataclass(frozen=True, slots=True, order=True)
class LabeledValue[T]:
    value: T = field(compare=True)
    label: str = field(compare=False)

    def __str__(self) -> str:
        return self.label

# テキトー

class SortOrder(Enum):
     ASC = auto()
     DESC = auto()


class FilterMethod(Enum):
        EQ = auto()
        NE = auto()
        CONTAINS = auto()
        GE = auto()
        LE = auto()

class EntryValidator:
    # NOTE: 中身覚えてないのと。どうでもいい
    pass

# NOTE: 必要な情報の整理

# 結局、画面構築と現在設定に使う情報は別なんだな
# 特に後者は値だけで、ファイルに保存できるような形。

# 前者は現状列として定義していたが、画面の項目みたいな構造にしたほうがよくね？
# それとも、列そのものとした方がいいのだろうか？

# TODO: 自身が LabeldValue を継承するか、Column を所有するかのどちらかがよさそう。
# 今のつくりは掲揚ありきだけど、別に位置でアクセスすればいいだけだし。

@dataclass(frozen=True, slots=True)
class SortFilterSettingsItem:
    # NOTE: LabeldValue にして、Column 事態をなくすとか？
    # 型で列であることが不明？というか、そういう構造なら、LabeldValue 継承するほうがいいな
    column: Column
    # FilterSettings とかにしてまとめることがあるかも？
    filter_methods: tuple[FilterMethod, ...] | None = None
    filter_entry_validator: EntryValidator | None = None
    filter_entry_converter: Callable[[str], Any] | None = None
    filter_selection_values: tuple[Any] | None = None



@dataclass(frozen=True, slots=True)
class SortFilterSettings:
    column: str # TODO: 対象だから None は許さない？
    sort_order: SortOrder | None
    # TODO: この2つはまとめるべきか？（画面上は Filter Condition）
    filter_method: FilterMethod | None = None
    filter_value: Any | None = None
    # TODO: これは表示・非表示どちらをつっこんでおくべきか？
    # 未設定は全表示＝全選択だよなぁ。
    # bool とセットじゃないとダメかなぁ
    # 1. 含まれている項目は bool 値
    # 2. 含まれてない値は表示＝チェック
    # んー、フィルターの性質上、表示対象を含めてないとダメだな
    # で、None の扱いだけど、フィルターがナシと考えれば、画面上は全選択だろうな。
    filter_selection_values: tuple[Any] | None = None

# TODO: 今コードの整理が主