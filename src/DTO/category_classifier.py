
from typing import Optional

from pydantic import BaseModel, constr, validator

import config as config


class InputCategoryClassifierEndpoint(BaseModel):
    id: int
    accommodates: int
    room_type: constr(strip_whitespace=True)
    beds: int
    bedrooms: int
    bathrooms: int
    neighbourhood: constr(strip_whitespace=True)
    tv: int
    elevator: int
    internet: bool
    latitude: float
    longitude: float
    model_name: Optional[str] = None

    @validator('room_type')
    def check_room_type(cls, value):
        if value not in config.ROOM_TYPE_OPTIONS:
            raise ValueError(f'room_type must be one of {config.ROOM_TYPE_OPTIONS}')
        return value

    @validator('neighbourhood')
    def check_neighbourhood(cls, value):
        if value not in config.NEIGHB_OPTIONS:
            raise ValueError(f'neighbourhood must be one of {config.NEIGHB_OPTIONS}')
        return value
