from typing import TYPE_CHECKING
from gigachat import GigaChat
from gigachat.models import MessagesRole
from gigachat.models.messages import Messages

if TYPE_CHECKING:
    from src.config.config import Config

from .prompts import paylaod

class GptModel:
    def __init__(self, config: "Config") -> None:
        self._model = GigaChat(**config.config["gigachat"])

    def get_commit_message(self, diff: str) -> str:
        paylaod.messages.append(Messages(role=MessagesRole.USER, content=diff))
        response = self._model.chat(paylaod)
        return response.choices[0].message.content


