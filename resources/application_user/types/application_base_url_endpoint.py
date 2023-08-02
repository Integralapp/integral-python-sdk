# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime


class ApplicationBaseUrlEndpoint(pydantic.BaseModel):
    id: str
    created_at: str = pydantic.Field(alias="createdAt")
    updated_at: str = pydantic.Field(alias="updatedAt")
    deleted_at: typing.Optional[str] = pydantic.Field(alias="deletedAt")
    path: str
    name: str
    scope_key: str = pydantic.Field(alias="scopeKey")
    description: str
    method: str
    query_params: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(alias="queryParams")
    request_body: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(alias="requestBody")
    request_headers: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(alias="requestHeaders")
    sandbox_field_location: typing.Optional[str] = pydantic.Field(alias="sandboxFieldLocation")
    sandbox_field_name: typing.Optional[str] = pydantic.Field(alias="sandboxFieldName")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
