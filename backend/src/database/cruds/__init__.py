from .account_chats import AccountChatsCRUD
from .accounts import AccountsCRUD
from .chats import ChatsCRUD
from .task_process_history import TaskProcessHistoryCRUD
from .payment_history import PaymentHistoryCRUD
from .tariffs import TariffsCRUD
from .tasks import TasksCRUD
from .topics import TopicsCRUD
from .users import UsersCRUD
from ..db_manager import DatabaseManager


class CommonCRUD:
    __slots__ = (
        "db_manager",
        "users",
        "tasks",
        "accounts",
        "chats",
        "tasks_history",
        "topics",
        "payment_history",
        "account_chats",
        "tariffs",
    )

    users: UsersCRUD
    tasks: TasksCRUD
    accounts: AccountsCRUD
    chats: ChatsCRUD
    topics: TopicsCRUD
    tasks_history: TaskProcessHistoryCRUD
    payment_history: PaymentHistoryCRUD
    account_chats: AccountChatsCRUD
    tariffs: TariffsCRUD

    def __init__(self, db_manager: DatabaseManager) -> None:
        self.db_manager = db_manager
        self.users = UsersCRUD(self.db_manager, self)
        self.tasks = TasksCRUD(self.db_manager, self)
        self.accounts = AccountsCRUD(self.db_manager, self)
        self.chats = ChatsCRUD(self.db_manager, self)
        self.topics = TopicsCRUD(self.db_manager, self)
        self.tasks_history = TaskProcessHistoryCRUD(self.db_manager, self)
        self.payment_history = PaymentHistoryCRUD(self.db_manager, self)
        self.account_chats = AccountChatsCRUD(self.db_manager, self)
        self.tariffs = TariffsCRUD(self.db_manager, self)
