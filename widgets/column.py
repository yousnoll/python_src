
from dataclasses import dataclass


# NOTE: 構造だけなら LabeldValue と同じよう構造ではある。
# ただ、列そのものを表すのと、値に名前を付けるのは同じではない。
# 前者は列そのものを表すためのものであって、値ではない。
# TODO: もしかして、ListView は header と column のオプション持つだけでいいのでは？
# あーでも、この構造自体は必要なのか？それとも Sort / Filter Setting には LaveldValue にして渡す？
@dataclass(frozen=True, slots=True)
class Column:
    name: str
    label: str

    def __str__(self) -> str:
        return self.label
