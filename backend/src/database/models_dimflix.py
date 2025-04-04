from uuid import UUID
from datetime import datetime
from typing import Any, List

from sqlalchemy import (
    BIGINT,
    JSON,
    TEXT,
    TIMESTAMP,
    Boolean,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Index,
    func,
    text
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from .db_manager import Base

###########EXAMPLE
class BaseModel(Base):
    __abstract__ = True

    def to_dict(self) -> dict[str, Any]:
        """Метод для преобразования объекта в словарь."""
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


class User(BaseModel):
    __tablename__: str = "users"
    __tableargs__: dict = {"comment": "Пользователи нашего телеграм бота"}

    id: Mapped[int] = mapped_column(
        BIGINT,
        nullable=False,
        primary_key=True,
        index=True,
        comment="Идентификатор пользователя нашего Telegram бота",
    )
    balance: Mapped[int] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        server_default="0",
        comment="Баланс в рублях на аккаунте",
    )
    referrer_id: Mapped[int] = mapped_column(
        BIGINT,
        nullable=True,
        index=True,
        comment="Идентификатор человека, у кого данный пользователь - реферал",
    )
    mailing_notices: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="True",
        comment="Разрешено ли получать уведомления о рассылках",
    )
    referral_notices: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="True",
        comment="Разрешено ли получать уведомления о рефералах",
    )
    news_notices: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="True",
        comment="Разрешено ли получать уведомления о новостях проекта",
    )
    balance_notices: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="True",
        comment="Разрешено ли получать уведомления о балансе и подписках",
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.timezone('UTC', func.current_timestamp()),
        comment="Дата и времени создания аккаунта",
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.timezone('UTC', func.current_timestamp()),
        comment="Дата и времени последней активности",
    )

    payment_history: Mapped[List["PaymentHistory"]] = relationship(
        "PaymentHistory", back_populates="user"
    )
    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="customer")

    def __str__(self):
        return f"{self.id}"


class PaymentHistory(BaseModel):
    __tablename__: str = "payment_history"
    __tableargs__: dict = {"comment": "История пополений пользователей"}
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
        primary_key=True,
        server_default=text("gen_random_uuid()"),
        comment="Внутренний идентификатор платежа в нашей системе",
    )
    user_id: Mapped[int] = mapped_column(
        BIGINT,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
        comment="Индентификатор заказчика",
    )
    currency: Mapped[str] = mapped_column(
        String, nullable=False, server_default="USD", comment="Валюта перевода"
    )
    amount: Mapped[int] = mapped_column(
        Numeric(10, 2), nullable=False, comment="Сумма пополнения"
    )
    provider: Mapped[str] = mapped_column(
        String,
        nullable=False,
        server_default="smart_glocal",
        comment="Провайдер платёжной системы, которой пользовались при оплате",
    )
    referral_percentage: Mapped[Numeric] = mapped_column(
        Numeric(5, 2),
        nullable=False,
        comment="Процент реферальных вознаграждений в диапазоне от 0 до 99.99%",
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.timezone('UTC', func.current_timestamp()),
        comment="Дата и время успешной оплаты",
    )
    payed_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=True,
        comment="Дата и время оплаты, если была"
    )

    user: Mapped["User"] = relationship("User", back_populates="payment_history")


class Task(BaseModel):
    __tablename__: str = "tasks"
    __tableargs__: dict = {"comment": "Задачи по рассылке, созданные пользователями."}

    id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        primary_key=True,
        autoincrement=True,
        comment="Внутренний идентификатор задачи в нашей системе",
    )
    customer_id: Mapped[int] = mapped_column(
        BIGINT,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
        comment="Индентификаотр заказчика",
    )
    text: Mapped[str] = mapped_column(
        TEXT,
        nullable=False,
        comment="Рекламный текст, который в последствии будет рассылаться",
    )
    suspended: Mapped[int] = mapped_column(
        Boolean,
        nullable=False,
        server_default="false",
        index=True,
        comment="Приостановлена ли задача, или нет",
    )
    autorenewal: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="true",
        index=True,
        comment="Продлять задачу автоматически при наличии баланса, или нет",
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.timezone('UTC', func.current_timestamp()),
        comment="Дата и времени создания задачи",
    )
    topic_id: Mapped[int] = mapped_column(
        ForeignKey("topics.id"),
        nullable=False,
        index=True,
        comment="Идентификатор темы чата"
    )
    abstract_tariff_id: Mapped[int] = mapped_column(
        ForeignKey("abstract_tariffs.id"),
        nullable=True,
        index=True,
        comment="Идентификатор абстрактного тарифа." \
        "Может быть пустым, т.к пользователь оформляет подписку" \
        "только после создания задачи.",
    )
    sub_purchase_date: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=True,
        comment="Дата и время покупки тарифа." \
        "Может быть пустым, т.к пользователь оформляет подписку" \
        "только после создания задачи."
    )
    sub_expiration_date: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=True,
        comment="Дата и время окончания действия тарифа." \
        "Может быть пустым, т.к пользователь оформляет подписку" \
        "только после создания задачи."
    )
    media: Mapped[str] = mapped_column(
        TEXT,
        nullable=True,
        comment="Имя медиа-файла для рассылки"
    )

    customer: Mapped[User] = relationship("User", back_populates="tasks")
    task_process_history: Mapped[List["TaskProcessHistory"]] = relationship(
        "TaskProcessHistory", 
        back_populates="task",
        cascade="all, delete-orphan",
    )
    topic: Mapped["Topic"] = relationship("Topic", back_populates="tasks")
    tariff: Mapped["Tariff"] = relationship(
        "Tariff",
        primaryjoin="and_(Task.topic_id == Tariff.topic_id, Task.abstract_tariff_id == Tariff.abstract_tariff_id)",
        foreign_keys="[Task.topic_id, Task.abstract_tariff_id]",
        viewonly=True
    )

    def __str__(self):
        return f"{self.id}"


class Account(BaseModel):
    __tablename__: str = "accounts"
    __tableargs__ = {"comment": "Таблица с телеграм аккаунтами для спама рекламой."}

    id: Mapped[int] = mapped_column(
        BIGINT,
        nullable=False,
        primary_key=True,
        index=True,
        comment="Айди аккаунта Teleagram",
    )
    phone_number: Mapped[str] = mapped_column(
        String,
        nullable=False,
        index=True,
        comment="номер телефона, привязанный к аккаунту.",
    )
    api_id: Mapped[int] = mapped_column(
        BIGINT, nullable=False, comment="параметр для аутентификации"
    )
    api_hash: Mapped[str] = mapped_column(
        String, nullable=False, comment="параметр для аутентификации"
    )

    _proxy: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
        comment='прокси для аккаунта в формате JSON. Пример: {"scheme": "socks5", "hostname": "...", "port": 1234}',
    )

    session_string: Mapped[str] = mapped_column(
        TEXT, nullable=False, comment="Сессия в формате строки"
    )

    is_valid: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="true",
        comment="валидная ли сессия или нет",
    )

    chats: Mapped[List["AccountChat"]] = relationship(
        "AccountChat", back_populates="account"
    )

    @property
    def proxy(self) -> dict:
        return self._proxy

    @proxy.setter
    def proxy(self, value: dict) -> None:
        required_keys = [
            ("scheme", str),
            ("hostname", str),
            ("port", int),
            ("username", str),
            ("password", str),
        ]

        for key in required_keys:
            if key[0] not in value or not isinstance(value[key[0]], key[1]):
                raise ValueError(
                    "Missing required keys or incorrect types in proxy settings."
                )

        self._proxy = value

    def __str__(self):
        return f"[{self.id}] {self.phone_number}"


class Topic(BaseModel):
    __tablename__ = "topics"
    __tableargs__ = {
        "comment": "Темы чатов. Каждая тема может быть связана с несколькими чатами."
    }

    id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        primary_key=True,
        index=True,
        comment="айди темы",
    )
    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        index=True,
        comment="название темы",
    )

    chats: Mapped[List["Chat"]] = relationship("Chat", back_populates="topic")
    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="topic")
    tariffs: Mapped[List["Tariff"]] = relationship("Tariff", back_populates="topic")

    def __str__(self):
        return f"[{self.id}] {self.name}"


class Chat(BaseModel):
    __tablename__ = "chats"
    __tableargs__ = {
        "comment": "База чатов по тематикам. Будет пополняться администрацией."
        "Аккаунты будут сверять свои чаты с этими."
    }

    id: Mapped[int] = mapped_column(
        BIGINT,
        nullable=False,
        primary_key=True,
        index=True,
        comment="айди чата в Telegram",
    )

    topic_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("topics.id"),
        nullable=False,
        comment="айди темы, к которой относится чат",
    )

    accounts_banned: Mapped[int] = mapped_column(
        Integer,
        nullable=True,
        server_default="0",
        comment="сколько наших аккаунтов заблокировано в этом чате.",
    )

    topic: Mapped[Topic] = relationship("Topic", back_populates="chats")
    accounts: Mapped[List["AccountChat"]] = relationship(
        "AccountChat", back_populates="chat"
    )

    def __str__(self):
        return f"{self.id}"


class AccountChat(BaseModel):
    __tablename__ = "account_chat"
    __tableargs__ = (
        Index('idx_account_chat_unique', 'account_id', 'chat_id', unique=True),
        {
            "comment": "Информация о том, присутствует ли аккаунт в чате или нет."
        }
    )

    id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        primary_key=True,
        index=True,
        comment="Айди записи связи.",
    )

    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"),
        nullable=False,
        comment="Айди аккаунта из таблицы accounts.",
    )

    chat_id: Mapped[int] = mapped_column(
        ForeignKey("chats.id"), nullable=False, comment="Айди чата из таблицы chats."
    )

    banned: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="false",
        comment="Аккаунт забанен в этом чате, или нет",
    )

    in_chat: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="false",
        comment="Находится ли на данный момент аккаунт в чате",
    )

    account: Mapped["Account"] = relationship("Account", back_populates="chats")
    chat: Mapped["Chat"] = relationship("Chat", back_populates="accounts")


class TaskProcessHistory(BaseModel):
    __tablename__ = "task_process_history"
    __tableargs__ = {"comment": "История отправленных аккаунтами сообщений."}

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, nullable=False)

    account_id: Mapped[int] = mapped_column(
        BIGINT,
        ForeignKey("accounts.id"),
        nullable=False,
        index=True,
        comment="айди аккаунта отправившего сообщение",
    )

    chat_id: Mapped[int] = mapped_column(
        BIGINT,
        ForeignKey("chats.id"),
        nullable=False,
        index=True,
        comment="айди чата сообщения",
    )

    message_id: Mapped[int] = mapped_column(
        BIGINT, nullable=False, comment="айди отправленного сообщения"
    )

    task_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("tasks.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="айди задачи с текстом отправленного сообщения",
    )

    sent_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        index=True,
        server_default=func.timezone('UTC', func.current_timestamp()),
        comment="Дата и время отправки рекламного сообщения",
    )

    account: Mapped[Account] = relationship("Account")
    task: Mapped[Task] = relationship("Task", back_populates="task_process_history")

    def __str__(self):
        return f"{self.id}"


class AbstractTariff(BaseModel):
    __tablename__ = "abstract_tariffs"
    __tableargs__ = {"comment": "Названия тарифов"}

    id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        primary_key=True,
        autoincrement=True,
        comment="Идентификатор абстрактного тарифа"
    )
    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment="Название тарифа"
    )

    tariffs: Mapped[List["Tariff"]] = relationship("Tariff", back_populates="abstract_tariff")

    def __str__(self):
        return f"[{self.id}] {self.name}"


class Tariff(BaseModel):
    __tablename__ = "tariffs"
    __tableargs__ = {
        "comment": "Связь между абстрактными тарифами и темами." \
            "То есть в этой базе данных мы получаем цены на тарифы" \
            "в зависимости от темы чата."
    }

    id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        primary_key=True,
        autoincrement=True,
        comment="Идентификатор тарифа"
    )

    abstract_tariff_id: Mapped[int] = mapped_column(
        ForeignKey("abstract_tariffs.id"),
        nullable=False,
        index=True,
        comment="Идентификатор абстрактного тарифа"
    )

    topic_id: Mapped[int] = mapped_column(
        ForeignKey("topics.id"),
        nullable=False,
        index=True,
        comment="Идентификатор темы"
    )

    price_per_day: Mapped[Numeric] = mapped_column(
        Numeric(10, 2),
        nullable=False,
        comment="Цена тарифа для данной темы (в день)"
    )
    
    msgs_per_day: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment="Количество сообщений в день"
    )

    disabled: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="false",
        comment="Отключен ли тариф для данной темы",
    )

    msgs_time_interval: Mapped[Integer] = mapped_column(
        Integer,
        nullable=False,
        server_default="30",
        comment="Интервал между сообщениями в минутах для данного тарифа",
    )

    abstract_tariff: Mapped["AbstractTariff"] = relationship("AbstractTariff", back_populates="tariffs")
    topic: Mapped["Topic"] = relationship("Topic", back_populates="tariffs")

    def __str__(self):
        return f"Abstract: {self.abstract_tariff_id} | Topic: {self.topic_id}"
    