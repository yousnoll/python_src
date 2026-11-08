from collections.abc import Iterable, Iterator
from enum import Enum, auto
from operator import attrgetter
from typing import ClassVar, Final, assert_never

# ● 緑 🟢 🟡 🔴 ✓ ✗ ⚠ ℹ

class Severity(Enum):
    CAUTION = auto()
    WARNING = auto()
    ERROR = auto()

    @property
    def display_name(self):
        if self == Severity.CAUTION:
            return "v" # ⚠|△
        if self == Severity.WARNING:
            return "‼" # ‼|▲
        if self == Severity.ERROR:
            return "✗" # ✗|✖

        return ""


class RowState:
    EMPTY: ClassVar["RowState"]
    CAUTION: ClassVar["RowState"]
    WARNING: ClassVar["RowState"]
    ERROR: ClassVar["RowState"]
    
    def __init__(self, severity: Severity | Iterable[Severity] | None = None):
        severity_set: set[Severity] = set()

        if severity is None:
            pass
        elif isinstance(severity, Severity):
            severity_set.add(severity)
        elif isinstance(severity, Iterable):
            severity_set.update(severity)
        else:
            # こういう、想定外の型が来ることがあり得るのを考慮してあるコードは、かなり丁寧らしい。
            assert_never(severity)

        sorted_severities = sorted(severity_set, key=attrgetter("value"), reverse=True)
        self._severities: Final[tuple[Severity, ...]] = tuple(sorted_severities)

    @property
    def highest_severity(self) -> Severity | None:
         # 要素は降順で並び替えられているので、先頭に最も優先度が高い物がある。
        if self._severities:
            return self._severities[0]

        return None

    @property
    def _sort_key(self) -> int:
        severity = self.highest_severity
        if severity is None:
            return 0

        return severity.value


    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._severities == other._severities

    def __hash__(self):
        return hash(self._severities)


    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._sort_key < other._sort_key

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._sort_key <= other._sort_key


    def __len__(self):
        return len(self._severities)

    def __contains__(self, value):
        return value in self._severities

    def __iter__(self) -> Iterator[Severity]:
        return iter(self._severities)


    def __str__(self) -> str:
        severity = self.highest_severity
        if severity:
            return severity.display_name
        
        return ""

RowState.EMPTY = RowState()
RowState.CAUTION = RowState(Severity.CAUTION)
RowState.WARNING = RowState(Severity.WARNING)
RowState.ERROR = RowState(Severity.ERROR)
