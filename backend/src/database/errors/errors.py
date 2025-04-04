from .base import AppError


class InsufficientFundsError(AppError):
    """Ошибка: недостаточно денег на балансе."""

    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Недостаточно средств. Баланс: {balance}, требуется: {amount}"
        )


class UserNotFoundError(AppError):
    """Ошибка: пользователь не найден."""

    def __init__(self, user_id: int):
        self.user_id = user_id
        super().__init__(f"Пользователь с ID {user_id} не найден.")


class TaskNotFoundError(AppError):
    """Ошибка: задача не найдена."""

    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(f"Задача с ID {task_id} не найдена.")


class TariffNotFoundError(AppError):
    """Ошибка: тариф не найден."""

    def __init__(self, tariff_id: int):
        self.tariff_id = tariff_id
        super().__init__(f"Тариф с ID {tariff_id} не найден.")


class PayNotFoundError(AppError):
    """Ошибка: платеж не найден."""

    def __init__(self, pay_id: int):
        self.pay_id = pay_id
        super().__init__(f"Платеж с ID {pay_id} не найден.")
        