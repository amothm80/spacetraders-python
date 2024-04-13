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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.ship_requirements import ShipRequirements
from typing import Optional, Set
from typing_extensions import Self

class ShipModule(BaseModel):
    """
    A module can be installed in a ship and provides a set of capabilities such as storage space or quarters for crew. Module installations are permanent.
    """ # noqa: E501
    symbol: StrictStr = Field(description="The symbol of the module.")
    capacity: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Modules that provide capacity, such as cargo hold or crew quarters will show this value to denote how much of a bonus the module grants.")
    range: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Modules that have a range will such as a sensor array show this value to denote how far can the module reach with its capabilities.")
    name: StrictStr = Field(description="Name of this module.")
    description: StrictStr = Field(description="Description of this module.")
    requirements: ShipRequirements
    __properties: ClassVar[List[str]] = ["symbol", "capacity", "range", "name", "description", "requirements"]

    @field_validator('symbol')
    def symbol_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['MODULE_MINERAL_PROCESSOR_I', 'MODULE_GAS_PROCESSOR_I', 'MODULE_CARGO_HOLD_I', 'MODULE_CARGO_HOLD_II', 'MODULE_CARGO_HOLD_III', 'MODULE_CREW_QUARTERS_I', 'MODULE_ENVOY_QUARTERS_I', 'MODULE_PASSENGER_CABIN_I', 'MODULE_MICRO_REFINERY_I', 'MODULE_ORE_REFINERY_I', 'MODULE_FUEL_REFINERY_I', 'MODULE_SCIENCE_LAB_I', 'MODULE_JUMP_DRIVE_I', 'MODULE_JUMP_DRIVE_II', 'MODULE_JUMP_DRIVE_III', 'MODULE_WARP_DRIVE_I', 'MODULE_WARP_DRIVE_II', 'MODULE_WARP_DRIVE_III', 'MODULE_SHIELD_GENERATOR_I', 'MODULE_SHIELD_GENERATOR_II']):
            raise ValueError("must be one of enum values ('MODULE_MINERAL_PROCESSOR_I', 'MODULE_GAS_PROCESSOR_I', 'MODULE_CARGO_HOLD_I', 'MODULE_CARGO_HOLD_II', 'MODULE_CARGO_HOLD_III', 'MODULE_CREW_QUARTERS_I', 'MODULE_ENVOY_QUARTERS_I', 'MODULE_PASSENGER_CABIN_I', 'MODULE_MICRO_REFINERY_I', 'MODULE_ORE_REFINERY_I', 'MODULE_FUEL_REFINERY_I', 'MODULE_SCIENCE_LAB_I', 'MODULE_JUMP_DRIVE_I', 'MODULE_JUMP_DRIVE_II', 'MODULE_JUMP_DRIVE_III', 'MODULE_WARP_DRIVE_I', 'MODULE_WARP_DRIVE_II', 'MODULE_WARP_DRIVE_III', 'MODULE_SHIELD_GENERATOR_I', 'MODULE_SHIELD_GENERATOR_II')")
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
        """Create an instance of ShipModule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of requirements
        if self.requirements:
            _dict['requirements'] = self.requirements.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShipModule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol": obj.get("symbol"),
            "capacity": obj.get("capacity"),
            "range": obj.get("range"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "requirements": ShipRequirements.from_dict(obj["requirements"]) if obj.get("requirements") is not None else None
        })
        return _obj


