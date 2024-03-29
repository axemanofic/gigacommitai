# GigaCommitAI

CLI инструмент для генерации коммитов на основе ИИ

## Установка

> Минимальная поддерживаемая версия Python - 3.8.
> Проверьте свою версию Python командой python --version

1. Установить gigacommit

- c помощью _pip_

```
pip install gigacommitai
```

- c помощью _pipx_

```
pipx install gigacommitai
```

- c помощью _poetry_

```
poetry add gigacommitai
```

2. Установить свой токен для авторизации

- Получите свой Client Secret
- Вставьте свой токен с помощью команды

```
gigacommitai config set gigachat.settings.credentials <CLIENT_SECRET>
```

## Как использовать?

1. Командой ниже можно сгенерировать сообщение для коммита

```
gigacommitai commit
```

2. Командой ниже можно вывести всю конфигурацию

```
gigacommitai config show
```

3. Командой ниже можно вывести значение параметра, например:

```
gigacommitai config get gigachat.settings.model
```

4. Командой ниже можно изменить значение параметра, например:

```
gigacommitai config set gigachat.settings.model <ТВОЕ_ЗНАЧЕНИЕ>
```

## Можно ли менять конфигурацию через файл?

Да. Конфигурация хранится в вашей директории где хранятся пользовательские конфигурации

- На Linux `~/.config/gigacommitai/config.toml`
- На Mac `~/Library/Application Support/gigacommitai/config.toml`
- На Windows `<APPDATA>/gigacommitai/gigacommitai/config.toml`

> Рекомендуется делать бэкап конфигурации во избежании проблем с запуском CLI

## Участие в проекте

GigaCommitAI - это проект с иходным кодом. Приветсвуется любое участие в разработке или улучшение документации.
