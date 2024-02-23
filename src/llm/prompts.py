from gigachat.models.chat import Chat
from gigachat.models.messages import Messages
from gigachat.models.messages_role import MessagesRole


content = """
Опиши какие изменения произошли в данном коде.
Сгенерируй свое сообщение очень кратко.
"""


paylaod = Chat(
    messages=[
        Messages(
            role=MessagesRole.SYSTEM,
            content=content,
        )
    ],
    temperature=0.7,
    max_tokens=20
)
