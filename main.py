
import io
import sys
import os


sys.path.insert(0, os.path.abspath('packages/spacetraders-sdk/openapi_client'))
sys.path.insert(0, os.path.abspath('packages/spacetraders-sdk'))
import openapi_client.api
import openapi_client.api.contracts_api
import openapi_client.api.fleet_api
import openapi_client
from openapi_client import ApiClient
from openapi_client import api
from openapi_client.rest import ApiException
from pprint import pprint
import requests
from requests.exceptions import HTTPError
import json
#sys.path.insert(0, os.path.abspath('packages/spacetraders-sdk'))




token = ''
api_url = 'https://api.spacetraders.io/v2/'
agent_url = 'my/agent'

def get_token():
    global token
    tokenfile = open('spacetradertoken.txt','r')
    token = tokenfile.readline()

def display_agent(agent_instance: openapi_client.AgentsApi):
    agent_name = input('please input an agent name: ')
    #try:
    agent_info = agent_instance.get_agent_with_http_info(agent_name)
    pprint(agent_info.model_dump()['data']['data'])
    input("press any key to continue...")

    agent_instance.get_agents_with_http_info()
    agent_instance.get_my_agent_with_http_info()
    

    


if __name__ == '__main__':
    get_token()

    # Defining the host is optional and defaults to https://api.spacetraders.io/v2
    # See configuration.py for a list of all supported configuration parameters.
    configuration = openapi_client.Configuration(
        host = "https://api.spacetraders.io/v2"
    )

    # The client must configure the authentication and authorization parameters
    # in accordance with the API server security policy.
    # Examples for each auth method are provided below, use the example that
    # satisfies your auth use case.

    # Configure Bearer authorization: AgentToken
    configuration = openapi_client.Configuration(
        #access_token = os.environ["BEARER_TOKEN"]
        access_token = token
    )

    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        agent_instance = openapi_client.AgentsApi(api_client)
        systems_instance = openapi_client.SystemsApi(api_client)
        contracts_instance = openapi_client.ContractsApi(api_client)
        fleet_instance = openapi_client.FleetApi(api_client)
        factions_instance = openapi_client.FactionsApi(api_client)
        agent_symbol = 'BAZEN' # str | The agent symbol (default to 'FEBA66')

        systems_instance.get_construction_with_http_info("SYSTEMSYMBOL","WAYPOINTSYMBOL")
        systems_instance.get_jump_gate_with_http_info("SYSTEMSYMBOL","WAYPOINTSYMBOL")
        systems_instance.get_market_with_http_info("SYSTEMSYMBOL","WAYPOINTSYMBOL")
        systems_instance.get_shipyard_with_http_info("SYSTEMSYMBOL","WAYPOINTSYMBOL")
        systems_instance.get_system_with_http_info("SYSTEMSYMBOL")
        systems_instance.get_systems_with_http_info()
        systems_instance.get_system_waypoints_with_http_info("SYSTEMSYMBOL")
        systems_instance.get_waypoint_with_http_info("SYSTEMSYMBOL","WAYPOINTSYMBOL")
        systems_instance.supply_construction_with_http_info("SYSTEMSYMBOL","WAYPOINTSYMBOL","SUPPLYCONSTRCUTIONREQUEST")

        contracts_instance.accept_contract_with_http_info("CONTRACTID")
        contracts_instance.deliver_contract_with_http_info("CONTRACTID","DELIVERCONTRACTREQUEST")
        contracts_instance.fulfill_contract_with_http_info("CONTRACTID")
        contracts_instance.get_contract_with_http_info("CONTRACTID")
        contracts_instance.get_contracts_with_http_info()

        factions_instance.get_faction_with_http_info("FACTIONSYMBOL")
        factions_instance.get_factions_with_http_info()
        
        fleet_instance.dock_ship_with_http_info("SHIPSYMBOL")
        fleet_instance.extract_resources_with_http_info("SHIPSYMBOL")
        fleet_instance.extract_resources_with_survey_with_http_info("SHIPSYMBOL")
        fleet_instance.get_my_ship_with_http_info("SHIPSYMBOL")
        fleet_instance.get_my_ships_with_http_info()
        fleet_instance.get_my_ship_cargo_with_http_info("SHIPSYMBOL")
        fleet_instance.get_repair_ship_with_http_info("SHIPSYMBOL")
        fleet_instance.get_mounts_with_http_info("SHIPSYMBOL")
        fleet_instance.get_scrap_ship_with_http_info("SHIPSYMBOL")
        fleet_instance.get_ship_cooldown_with_http_info("SHIPSYMBOL")
        fleet_instance.install_mount_with_http_info("SHIPSYMBOL","INSTALLMOUNTREQUEST")
        fleet_instance.get_ship_nav_with_http_info("SHIPSYMBOL")
        fleet_instance.navigate_ship_with_http_info("SHIPSYMBOL")
        fleet_instance.jettison_with_http_info("SHIPSYMBOL","JETTISONREQUEST")
        fleet_instance.jump_ship_with_http_info("SHIPSYMBOL","JUMPSHIPREQUEST")

        
        userinp = ''
        while userinp != 'exit':
            try:
                print("please choose one of the below options:")
                print("press 1 to display agent info")
                print("press 2 to display systems info")
                print("press 3 to display contract info")
                print("press 4 to display fleet info")
                print("press 5 to display faction info")
                print("type exit to exit")
                userinp = input(":")
                match userinp:
                    case '1':
                        display_agent(agent_instance)

            except ApiException as e:
                print(json.loads(e.body)['error']['message'])
                input("press any key to continue...")
            except:
                print("connection error")
                input("press any key to continue...")