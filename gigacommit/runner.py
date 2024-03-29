import subprocess
from typing import List


class TaskRunner:
    def __run_command(self, command: List[str]) -> str:
        call_command = subprocess.run(command, stdout=subprocess.PIPE, text=True)
        return call_command.stdout, call_command.stderr

    def check_is_exist_git_repo(self):
        command = ["git", "rev-parse", "--show-toplevel"]
        return self.__run_command(command)

    def get_changes(self) -> str:
        command = ["git", "diff", "--cached", "--diff-algorithm=minimal"]
        return self.__run_command(command)

    def get_staged_files(self) -> str:
        command = ["git", "diff", "--cached", "--name-only"]
        return self.__run_command(command)

    def create_commit(self, message: str, dry_run: bool) -> str:
        command = ["git", "commit", "-m", message]
        if dry_run:
            command += ["--dry-run"]
        return self.__run_command(command)
