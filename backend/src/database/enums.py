from enum import Enum


class BalanceChangeType(Enum):
    PLUS = "+"
    MINUS = "-"
    EQUATE = "="
    PAY = "$"
    