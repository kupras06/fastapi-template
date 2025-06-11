"""Schema Utils"""

from __future__ import annotations

import contextlib
from collections.abc import Sequence
from datetime import datetime
from typing import Annotated, Any, Generic, TypeVar
from uuid import UUID

from fastapi import File, UploadFile
from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    EmailStr,
    Field,
)

from app.utils.helpers import get_current_timestamp

PyObjectId = Annotated[str, BeforeValidator(str)]
"""Paginate Schema"""


T = TypeVar("T", bound=BaseModel)


class Paginated(BaseModel, Generic[T]):
    """Paginated Model"""

    count: int
    data: Sequence[T]
    total_count: int = 0
    model_config = ConfigDict(
        arbitrary_types_allowed=True, extra="allow", populate_by_name=True
    )


def get_dict_value(item: Any):
    """Get Dict Value from Model"""
    try:
        return item.model_dump()
    except AttributeError:
        return item


class APIModel(BaseModel):
    """BaseModel Wrapper"""

    model_config = ConfigDict(use_enum_values=True)

    def valid_values(self):
        """Get Valid Values"""
        return self.model_dump(
            exclude_defaults=True, exclude_none=True, exclude_unset=True
        )

    @classmethod
    def load(cls, *args: Any):
        """Load Data from Model or Dict"""
        args_dict = {}
        for arg in args:
            obj_dict = arg
            with contextlib.suppress(AttributeError):
                obj_dict = arg.model_dump()
            if not isinstance(obj_dict, dict):
                continue
            args_dict.update(obj_dict)
        return cls.model_validate(args_dict, from_attributes=True)

    @classmethod
    def paginate(cls, data: Sequence[Any], **kwargs):
        """Paginate Helper"""
        count = 1
        if isinstance(data, Sequence):
            validated_data = [cls.model_validate(get_dict_value(item)) for item in data]
            count = len(data)
        else:
            validated_data = [cls.model_validate(get_dict_value(data))]
        return Paginated(count=count, data=validated_data, **kwargs)


class TimestampsMixin(APIModel):
    """Timestamps Mixin"""

    created_at: datetime = Field(
        default_factory=get_current_timestamp, description="Document Created At Time"
    )
    updated_at: datetime = Field(
        default_factory=get_current_timestamp, description="Document Updated At Time"
    )
    is_deleted: bool = Field(default=False)
    updated_by: Annotated[
        str, Field(description="User who made the recent update to resource data")
    ]
    created_by: Annotated[str, Field(description="Resource Creator/Owner User ID")]


class FileInBase(APIModel):
    """File In Base"""

    file: UploadFile = File(...)
    folder_path: str


class GeoSchemaMixin(APIModel):
    """Geo Schema Mixin"""

    latitude: float
    longitude: float
    accuracy: float | None = None  # Accuracy of the geographical coordinates
    altitude: float | None = None  # Altitude above sea level
    altitude_accuracy: float | None = None  # Accuracy of the altitude information


class AddressModel(APIModel):
    """Address Model"""

    street: str
    city: str
    postal_code: int | None = None
    state: str
    country: str | None = "India"


class AddressMixin(APIModel):
    """Address Mixin"""

    address: AddressModel | None = Field(default=None, description="Address Field")


class ImageSchemaMixin(APIModel):
    """Image Schema Mixin"""

    file_id: str | None = None
    file_path: str = "default-image.png"


class RedisOtpModel(APIModel):
    """Redis Otp Model"""

    token: str
    previous_otps: list[str]


class CategoryCreate(APIModel):
    """Category Create"""

    name: str
    description: str = ""
    image_id: str | None = "6383766357664417270919c4"  # Default image ID for the shop
    image: str | None = "/quippix/services/default-image.png"


class CategoryProjection(CategoryCreate):
    """Category Projection"""

    id: UUID


class NamesMixin(APIModel):
    """Names Mixin"""

    first_name: Annotated[str, Field(description="User First Name", default="")] = ""
    last_name: Annotated[str, Field(description="User Lase Name", default="")] = ""
    display_name: Annotated[str, Field(description="User Display Name", default="")] = (
        ""
    )
    email: Annotated[EmailStr, Field(description="User Email Address")]


class SocialMixins(BaseModel):
    """Social Mixins"""

    url: str


class RatingMixin(APIModel):
    """Rating Mixin"""

    avg_rating: Annotated[
        float | None, Field(default=0.0, description="Rating of the resource")
    ] = 0.0
    feedback_count: Annotated[
        float | None,
        Field(default=0.0, description="Number of feedback on this resource"),
    ] = 0.0


class UpdateImageSchemaMixin(APIModel):
    """Update Image Schema Mixin"""

    image_id: str
    image: str
    resource_id: str


class StatusMixins(APIModel):
    """Status Mixins"""

    is_active: Annotated[
        bool,
        Field(
            default=False, description="Flag to indicate if the store is active or not"
        ),
    ] = False
    is_verified: Annotated[
        bool,
        Field(
            default=False,
            description="Flag to indicate if the store is verified or not",
        ),
    ]


class OauthAccountBase(APIModel):
    """Oauth Account Base"""

    access_token: str
    account_id: str
    account_email: str
    expires_at: int | None = None
    refresh_token: str | None = None
    id_token: str | None = None
