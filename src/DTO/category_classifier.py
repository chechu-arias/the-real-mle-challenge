
from typing import Optional

from pydantic import BaseModel, constr, field_validator

import config as config

# TODO: Add optional params
class InputCategoryClassifierEndpoint(BaseModel):
    id: int
    accommodates: int
    room_type: constr(strip_whitespace=True)
    beds: Optional[int] = 1
    bedrooms: int
    bathrooms: int
    neighbourhood: constr(strip_whitespace=True)
    tv: Optional[int] = 0
    elevator: Optional[int] = 0
    internet: Optional[bool] = 0
    latitude: Optional[float] = 0.0
    longitude: Optional[float] = 0.0
    classifier_name: Optional[str] = None

    @field_validator('room_type')
    def check_room_type(cls, value):
        if value not in config.ROOM_TYPE_OPTIONS:
            raise ValueError(f'room_type must be one of {config.ROOM_TYPE_OPTIONS}')
        return value

    @field_validator('neighbourhood')
    def check_neighbourhood(cls, value):
        if value not in config.NEIGHB_OPTIONS:
            raise ValueError(f'neighbourhood must be one of {config.NEIGHB_OPTIONS}')
        return value
