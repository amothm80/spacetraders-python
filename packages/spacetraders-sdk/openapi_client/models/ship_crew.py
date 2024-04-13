# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.  The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.  ```json http {   \"method\": \"GET\",   \"url\": \"https://api.spacetraders.io/v2\", } ```  Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.  We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.   

    The version of the OpenAPI document: 2.0.0
    Contact: joel@spacetraders.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ShipCrew(BaseModel):
    """
    The ship's crew service and maintain the ship's systems and equipment.
    """ # noqa: E501
    current: StrictInt = Field(description="The current number of crew members on the ship.")
    required: StrictInt = Field(description="The minimum number of crew members required to maintain the ship.")
    capacity: StrictInt = Field(description="The maximum number of crew members the ship can support.")
    rotation: StrictStr = Field(description="The rotation of crew shifts. A stricter shift improves the ship's performance. A more relaxed shift improves the crew's morale.")
    morale: Annotated[int, Field(le=100, strict=True, ge=0)] = Field(description="A rough measure of the crew's morale. A higher morale means the crew is happier and more productive. A lower morale means the ship is more prone to accidents.")
    wages: Annotated[int, Field(strict=True, ge=0)] = Field(description="The amount of credits per crew member paid per hour. Wages are paid when a ship docks at a civilized waypoint.")
    __properties: ClassVar[List[str]] = ["current", "required", "capacity", "rotation", "morale", "wages"]

    @field_validator('rotation')
    def rotation_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['STRICT', 'RELAXED']):
            raise ValueError("must be one of enum values ('STRICT', 'RELAXED')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ShipCrew from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShipCrew from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "current": obj.get("current"),
            "required": obj.get("required"),
            "capacity": obj.get("capacity"),
            "rotation": obj.get("rotation") if obj.get("rotation") is not None else 'STRICT',
            "morale": obj.get("morale"),
            "wages": obj.get("wages")
        })
        return _obj

