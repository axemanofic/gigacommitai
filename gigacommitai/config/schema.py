from typing import List, Literal

from pydantic.v1 import BaseModel
from gigachat.settings import Settings
from gigachat.models import Chat, MessagesRole, Messages


SCOPE = Literal["GIGACHAT_API_PERS", "GIGACHAT_API_CORP"]


class ModelSettings(Settings):
    model = "GigaChat"
    scope: SCOPE = "GIGACHAT_API_PERS"
    credentials = "MY_CLIENT_SECRET_TOKEN"
    profanity_check = False
    verify_ssl_certs = False


class ModelChat(Chat):
    messages: List[Messages] = [
        Messages(
            role=MessagesRole.USER,
            content="""
            Опиши какие изменения произошли в данном коде.
            Сгенерируй свое сообщение очень кратко.
            """
        )
    ]
    n = 1
    temperature = 0.7
    top_p = 1.0
    max_tokens = 200
    stream = False
    repetition_penalty = 0.0
    profanity_check = False


class Model(BaseModel):
    settings: ModelSettings = ModelSettings()
    chat: ModelChat = ModelChat()


class AppSchema(BaseModel):
    gigachat: Model = Model()
