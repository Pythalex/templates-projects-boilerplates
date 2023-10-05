from typing import Optional

from pydantic import BaseModel, Field


class Config(BaseModel):
    configuration: str
    config_with_dashes: str = Field(alias="config-with-dashes")
    optional_config_int: Optional[int] = Field(
        alias="optional-config-int", default=None
    )
    config_with_user_expand: str = Field(
        alias="config-with-user-expand", default="~"
    )
