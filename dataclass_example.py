
from collections.abc import Iterator
from dataclasses import dataclass, field


# フィールドに持つなら、dataclass に任せて生成された方がよさそう
@dataclass(frozen=True, slots=True, eq=False)
class ExampleDataClass:
    val1: int
    val2: int
    val3: int
    maximum: int = field(init=False)

    def __eq__(self, other):
        if not isinstance(other, ExampleDataClass):
            return NotImplemented
        return self.maximum == other.maximum

    def __lt__(self, other):
        if not isinstance(other, ExampleDataClass):
            return NotImplemented
        return self.maximum < other.maximum

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.maximum <= other.maximum


    # 最大値を得るだけなら、その都度取得でもいいのか？
    # 大した負荷じゃなさそうなんだよな
    # てか別に計算とか挟んでも、全然いいっぽいし

    def __post_init__(self):
        # frozen=True なので、このままでは設定できない。
        # self.maximum = max(self.val1, self.val2, self.val3)
        # これで設定できる
        object.__setattr__(self, "maximum", max(self.val1, self.val2, self.val3))


