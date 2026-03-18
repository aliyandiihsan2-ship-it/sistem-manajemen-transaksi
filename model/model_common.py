from bson import ObjectId
from pydantic_core import core_schema
from typing import Any
from util.util_datetime import convert_str_datetime
class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source_type: Any, _handler: Any
    ) -> core_schema.CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema([
                core_schema.is_instance_schema(ObjectId),
                core_schema.chain_schema([
                    core_schema.str_schema(),
                    core_schema.no_info_plain_validator_function(cls.validate),
                ]),
            ]),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: str(x), when_used='unless-none'
            ),
        )

    @classmethod
    def validate(cls, v: Any) -> ObjectId:
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

class InputDatetime(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source_type: Any, _handler: Any
    ) -> core_schema.CoreSchema:
        return core_schema.json_or_python_schema(
                json_schema=core_schema.str_schema(),
                python_schema=core_schema.union_schema([
                    core_schema.is_instance_schema(ObjectId),
                    core_schema.chain_schema([
                        core_schema.str_schema(),
                        core_schema.no_info_plain_validator_function(cls.validate),
                    ]),
                ]),
                serialization=core_schema.plain_serializer_function_ser_schema(
                    lambda x: str(x), when_used='unless-none'
                ),
            )
    @classmethod
    def validate(cls, v: Any) -> ObjectId:
        try:
            return convert_str_datetime(v)
        except ValueError:
            raise ValueError("Invalid Format (DD-MM-YYYY)")