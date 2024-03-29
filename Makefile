reload-config:
	rm -rf ~/.config/gigacommit
	poetry run gc
rebuild:
	poetry install
	poetry build
