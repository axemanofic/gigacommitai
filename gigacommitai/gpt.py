from typing import TYPE_CHECKING

from gigachat import GigaChat
from gigachat.models import MessagesRole, Chat
from gigachat.models.messages import Messages

if TYPE_CHECKING:
    from .config import Config


class GptModel:
    def __init__(self, config: "Config", dry_run: bool) -> None:
        self.config = config.config["gigachat"]
        self.dry_run = dry_run

    def __generate_commit_message(self, changes: str) -> str:
        model = GigaChat(**self.config["settings"])
        chat = Chat(**self.config["chat"])
        chat.messages.append(
            Messages(
                role=MessagesRole.USER,
                content=changes,
            )
        )
        response = model.chat(chat)
        return response.choices[0].message.content

    def generate_commit_message(self, changes: str) -> str:
        if self.dry_run:
            return "test commit message"
        else:
            return self.__generate_commit_message(changes)
