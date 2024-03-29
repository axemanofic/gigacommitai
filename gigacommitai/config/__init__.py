from collections import UserDict
from typing import Optional, Any
from pathlib import Path

import rtoml
from platformdirs import user_config_dir

from .schema import AppSchema

CONFIG_DIR = Path(user_config_dir(appname="gigacommit", appauthor=False, roaming=True))


class ConfigDict(UserDict):
    def _process(
        self,
        setting_name: str,
        setting_value: Optional[str] = None,
    ):
        keys = setting_name.split(".")
        for key in keys[:-1]:
            if key in self:
                self = self.setdefault(key, {})
        if setting_value:
            self[keys[-1]] = setting_value

        return self[keys[-1]]

    def get(self, setting_name: str) -> Any:
        return self._process(setting_name)

    def set(self, setting_name: str, setting_value: Any):
        self._process(setting_name, setting_value)

    @classmethod
    def fromSchema(cls, schema: AppSchema):
        return cls(schema.dict(exclude_none=True))


class TomlFile:
    def __init__(self, path: Path) -> None:
        self.__path = path

    def exists(self) -> bool:
        return self.__path.exists()

    def write(self, content: ConfigDict) -> None:
        rtoml.dump(content.data, self.__path)

    def read(self) -> dict:
        return rtoml.load(self.__path)


class Config:
    _config = AppSchema()

    _config_file = TomlFile(CONFIG_DIR / "config.toml")

    @property
    def config(self) -> ConfigDict:
        return ConfigDict.fromSchema(self._config)

    def get(self, setting_name: str):
        return self.config.get(setting_name)

    def set(self, setting_name: str, setting_value: Any):
        config_dict = self.config
        config_dict.set(setting_name, setting_value)
        self._config = AppSchema(**config_dict)
        self._update()

    def _update(self):
        if self._config_file.exists():
            self._config_file.write(self.config)

    def load(self):
        config_file = TomlFile(CONFIG_DIR / "config.toml")
        config_dict = ConfigDict(config_file.read())
        self._config = AppSchema(**config_dict)
        return self

    @classmethod
    def create(cls):
        if not CONFIG_DIR.exists():
            CONFIG_DIR.mkdir()
        if not cls._config_file.exists():
            config_dict = ConfigDict.fromSchema(cls._config)
            cls._config_file.write(config_dict)
        return cls()
