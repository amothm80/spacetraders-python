# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.  The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.  ```json http {   \"method\": \"GET\",   \"url\": \"https://api.spacetraders.io/v2\", } ```  Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.  We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.   

    The version of the OpenAPI document: 2.0.0
    Contact: joel@spacetraders.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ship_mount import ShipMount

class TestShipMount(unittest.TestCase):
    """ShipMount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShipMount:
        """Test ShipMount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShipMount`
        """
        model = ShipMount()
        if include_optional:
            return ShipMount(
                symbol = 'MOUNT_GAS_SIPHON_I',
                name = '',
                description = '',
                strength = 0,
                deposits = [
                    'QUARTZ_SAND'
                    ],
                requirements = openapi_client.models.ship_requirements.ShipRequirements(
                    power = 56, 
                    crew = 56, 
                    slots = 56, )
            )
        else:
            return ShipMount(
                symbol = 'MOUNT_GAS_SIPHON_I',
                name = '',
                requirements = openapi_client.models.ship_requirements.ShipRequirements(
                    power = 56, 
                    crew = 56, 
                    slots = 56, ),
        )
        """

    def testShipMount(self):
        """Test ShipMount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()