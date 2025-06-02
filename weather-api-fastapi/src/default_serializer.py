from enum import Enum
from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class StatusDefaultResponseEnum(str, Enum):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"


class DefaultResponseSerializer(BaseModel):
    code: int = 200
    status: StatusDefaultResponseEnum = StatusDefaultResponseEnum.SUCCESS
    message: str = None
    data: Optional[Union[List, Dict, str]] = None
