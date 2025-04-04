from alembic_utils.pg_function import PGFunction
from alembic_utils.pg_trigger import PGTrigger


##==> Description:
# Тригер, срабатывающий на добавление нового значения в таблицу `accounts`.
# Он добавляет связи аккаунта со всеми существующими чатами. 
################################################################# EXAMPLES
trgfunc_add_account_chat = PGFunction(
    schema="public",
    signature="trgfunc_add_account_chat()",
    definition="""
RETURNS TRIGGER AS $$
DECLARE
    chat_record RECORD;
BEGIN
    -- Цикл по всем существующим чатам
    FOR chat_record IN SELECT id FROM chats LOOP
        INSERT INTO account_chat (account_id, chat_id, banned, in_chat)
        VALUES (NEW.id, chat_record.id, FALSE, FALSE);
    END LOOP;

    RETURN NEW;
END;
$$

LANGUAGE plpgsql;
""")

trg_add_account_chat = PGTrigger(
    schema="public",
    signature="trg_add_account_chat",
    on_entity="public.accounts",
    is_constraint=False,
    definition="""AFTER INSERT ON accounts
        FOR EACH ROW
        EXECUTE FUNCTION trgfunc_add_account_chat();""",
)


##==> Description:
# Тригер, срабатывающий на добавление нового значения в таблицу `chats`.
# Он добавляет связи всех аккаунтов с новым чатом.
#################################################################
trgfunc_add_chat_account = PGFunction(
    schema="public",
    signature="trgfunc_add_chat_account()",
    definition="""
RETURNS TRIGGER AS $$
DECLARE
    account_record RECORD;
BEGIN
    -- Цикл по всем существующим аккаунтам
    FOR account_record IN SELECT id FROM accounts LOOP
        INSERT INTO account_chat (account_id, chat_id, banned, in_chat)
        VALUES (account_record.id, NEW.id, FALSE, FALSE);
    END LOOP;

    RETURN NEW;
END;
$$

LANGUAGE plpgsql;
""")

trg_add_chat_account = PGTrigger(
    schema="public",
    signature="trg_add_chat_account",
    on_entity="public.chats",
    is_constraint=False,
    definition="""AFTER INSERT ON chats
        FOR EACH ROW
        EXECUTE FUNCTION trgfunc_add_chat_account();""",
)


##==> List of all replaceable etities
##########################################
all_entities = [
    trgfunc_add_account_chat,
    trg_add_account_chat,

    trgfunc_add_chat_account,
    trg_add_chat_account,
]