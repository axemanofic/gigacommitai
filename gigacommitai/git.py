from typing import TYPE_CHECKING
from .gpt import GptModel
from .runner import TaskRunner

if TYPE_CHECKING:
    from .config import Config


class Commit:
    def __init__(self, config: "Config", dry_run: bool):
        self.runner = TaskRunner()
        self.dry_run = dry_run
        self.config = config

    def generate_commit_message(self):
        changes, err = self.runner.get_changes()
        model = GptModel(self.config, dry_run=self.dry_run)
        self.commit_message = model.generate_commit_message(changes)

    def get_staged_files(self) -> str:
        output, error = self.runner.get_staged_files()
        return output

    def create_commit(self, commit_message: str) -> str:
        output, error = self.runner.create_commit(commit_message, dry_run=self.dry_run)
        return output

    def get_commit_message(self) -> str:
        return self.commit_message
