from __future__ import annotations

import os
from functools import lru_cache

from pyproject_parser import PyProject

from myproject.model import Config


class ConfigError(Exception):
    pass


@lru_cache
def get_config() -> Config:
    pyproject = PyProject.load("pyproject.toml")
    if not hasattr(pyproject, "tool") or "config" not in pyproject.tool:
        raise RuntimeError(
            "Configuration [tool.config] not found in pyproject.toml"
        )

    config = Config(**pyproject.tool["config"])
    config.config_with_user_expand = os.path.expanduser(
        config.config_with_user_expand
    )

    return config


def check_config(config: Config) -> None:
    pass
