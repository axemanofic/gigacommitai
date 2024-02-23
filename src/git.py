import subprocess


def get_diff() -> str:
    git_diff = ["git", "diff", "--cached", "--diff-algorithm=minimal"]

    call_git_diff = subprocess.run(git_diff, stdout=subprocess.PIPE, text=True, )

    return call_git_diff.stdout
