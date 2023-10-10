from __future__ import annotations

import logging
import logging.config
import os

import typer
import yaml

from changeme.config import check_config, get_config


def main():
    config = get_config()
    check_config(config)

    try:
        with open("logging.yml", "r") as stream:
            logging_cfg = yaml.load(stream, Loader=yaml.FullLoader)
            logging.config.dictConfig(logging_cfg)
    except FileNotFoundError:
        logging.warning(
            "logging.yml not found, logging will be basic. Note: You can use"
            " logging.yml.example."
        )

    logger = logging.getLogger()
    logger.info("Now change this template to actually do something !")


if __name__ == "__main__":
    typer.run(main)
