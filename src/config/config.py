from typing import Optional, Any
from pathlib import Path

import typer
import rtoml
from platformdirs import user_config_dir

from .schema import AppSchema, GigachatSchema

CONFIG_DIR = Path(user_config_dir(appname="gigacommit", appauthor=False, roaming=True))


class TomlFile:
    def __init__(self, path: Path) -> None:
        self.__path = path

    def exists(self) -> bool:
        return self.__path.exists()

    def write(self, content: dict) -> None:
        rtoml.dump(content, self.__path)

    def read(self) -> dict:
        return rtoml.load(self.__path)


class Config:
    _default_config = AppSchema(gigachat=GigachatSchema())

    _config: Optional[dict[str, Any]] = None

    _config_file = TomlFile(CONFIG_DIR / "config.toml")

    @property
    def config(self):
        if self._config:
            return self._config
        else:
            return dict()

    def get(self, setting_name: str, default: Any = None):
        if not self._config:
            return default
        keys = setting_name.split(".")
        value = self._config
        for key in keys:
            if key in value:
                value = value[key]
        return value

    def set(self, setting_name: str, setting_value: Any):
        if not self._config:
            raise Exception
        keys = setting_name.split(".")
        value = self._config
        for key in keys[:-1]:
            if key in value:
                value = value.setdefault(key, {})
        value[keys[-1]] = setting_value

    def update(self):
        if self._config_file.exists() and self._config:
            self._config_file.write(self._config)

    def load(self):
        config_file = TomlFile(CONFIG_DIR / "config.toml")
        config_dict = config_file.read()
        config_schema = AppSchema(**config_dict)
        self._config = config_schema.model_dump()
        return self

    @classmethod
    def create(cls):
        if not CONFIG_DIR.exists():
            CONFIG_DIR.mkdir()
        if not cls._config_file.exists():
            cls._config_file.write(cls._default_config.model_dump())
        return cls()


class AppContext(typer.Context):
    obj: Config
