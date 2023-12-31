# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import IntegralApiEnvironment
from .types.post_process_api_response import PostProcessApiResponse
from .types.pre_process_api_response import PreProcessApiResponse


class ParseClient:
    def __init__(self, *, environment: IntegralApiEnvironment, integral_application_id: str, api_key: str):
        self._environment = environment
        self.integral_application_id = integral_application_id
        self.api_key = api_key

    def pre_process(
        self,
        *,
        api_key: str,
        ip: str,
        method: str,
        request_body: typing.Dict[str, typing.Any],
        headers: typing.Dict[str, typing.Any],
        path: str,
        query_params: typing.Dict[str, typing.Any],
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = None,
        idempotency_key: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
    ) -> PreProcessApiResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", "parse/pre-process"),
            json=jsonable_encoder(
                {
                    "apiKey": api_key,
                    "ip": ip,
                    "method": method,
                    "requestBody": request_body,
                    "headers": headers,
                    "path": path,
                    "queryParams": query_params,
                    "metadata": metadata,
                    "idempotencyKey": idempotency_key,
                    "version": version,
                }
            ),
            headers=remove_none_from_headers(
                {"Integral-Application-Id": self.integral_application_id, "Integral-Application-Id": self.api_key}
            ),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PreProcessApiResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def post_process(
        self,
        *,
        endpoint_id: str,
        request_id: str,
        response_status_code: int,
        request_body: typing.Dict[str, typing.Any],
        api_key: str,
        idempotency_key: str,
    ) -> PostProcessApiResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", "parse/post-process"),
            json=jsonable_encoder(
                {
                    "endpointId": endpoint_id,
                    "requestId": request_id,
                    "responseStatusCode": response_status_code,
                    "requestBody": request_body,
                    "apiKey": api_key,
                    "idempotencyKey": idempotency_key,
                }
            ),
            headers=remove_none_from_headers(
                {"Integral-Application-Id": self.integral_application_id, "Integral-Application-Id": self.api_key}
            ),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostProcessApiResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
