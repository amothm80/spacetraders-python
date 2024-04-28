from imports import *

token = ''
api_url = 'https://api.spacetraders.io/v2/'
agent_url = 'my/agent'

def get_token():
    global token
    tokenfile = open('spacetradertoken.txt','r')
    token = tokenfile.readline()


"""display"""
def print_response(responsedata,waitinput):
    print('\n')
    for k,v in responsedata.items():
        print(f'{str(k).replace("_"," ").title()}: {v}')
    if waitinput == True:
        input("press any key to continue...")
    #print('\n')

def print_response_list(responsedata):
    for datum in responsedata:
        print_response(datum,False)

def determine_pagination(responsemeta, page, limit):
    if limit * page > responsemeta['total']:
        uinp = 'b'
    else:
        uinp = input("press enter for next page, or b to exit...")
    page += 1
    return (uinp,page)


"""agent information"""
def display_agent(agent_instance: openapi_client.AgentsApi):
    agent_name = input('please input an agent name: ')
    #try:
    agent_info = agent_instance.get_agent_with_http_info(agent_name)
    #pprint(agent_info.model_dump()['data']['data'])
    print_response(agent_info.model_dump()['data']['data'],True)

def display_agents(agent_instance: openapi_client.AgentsApi,page,limit):
    uinp = ''
    while uinp != 'b':
        agents_info = agent_instance.get_agents_with_http_info(limit=limit,page=page)
        agents_data = agents_info.model_dump()['data']['data']
        agents_meta = agents_info.model_dump()['data']['meta']
        print_response_list(agents_data)
        uinp,page = determine_pagination(agents_meta,page,limit)

def display_my_agent(agent_instance: openapi_client.AgentsApi):
    agent_info = agent_instance.get_my_agent_with_http_info()
    print_response(agent_info.model_dump()['data']['data'],True)

"""systems and waypoints"""
def get_construction(systems_instance: openapi_client.SystemsApi):
    system_symbol = input('please input the system symbol: ')
    waypoint_symbol = input('please input waypoint symbol: ')
    system_info = systems_instance.get_construction_with_http_info(system_symbol,waypoint_symbol)
    print_response(system_info.model_dump()['data']['data'])

def get_jump_gate(systems_instance:openapi_client.SystemsApi):
    system_symbol = input('please input the system symbol: ')
    waypoint_symbol = input('please input waypoint symbol: ')
    system_info = systems_instance.get_jump_gate_with_http_info(system_symbol,waypoint_symbol)
    print_response(system_info.model_dump()['data']['data'])

def get_market(systems_instance:openapi_client.SystemsApi):
    system_symbol = input('please input the system symbol: ')
    waypoint_symbol = input('please input waypoint symbol: ')
    system_info = systems_instance.get_market_with_http_info(system_symbol,waypoint_symbol)
    print_response(system_info.model_dump()['data']['data'])

def get_shipyard(systems_instance:openapi_client.SystemsApi):
    system_symbol = input('please input the system symbol: ')
    waypoint_symbol = input('please input waypoint symbol: ')
    system_info = systems_instance.get_shipyard_with_http_info(system_symbol,waypoint_symbol)
    print_response(system_info.model_dump()['data']['data'])

def get_system(systems_instance:openapi_client.SystemsApi):
    system_symbol = input('please input the system symbol: ')
    waypoint_symbol = input('please input waypoint symbol: ')
    system_info = systems_instance.get_system_with_http_info(system_symbol)
    print_response(system_info.model_dump()['data']['data'])

def get_systems(systems_instance:openapi_client.SystemsApi,page,limit):
    uinp = ''
    while uinp != 'b':
        system_info = systems_instance.get_systems_with_http_info(page=page,limit=limit)
        system_data = system_info.model_dump()['data']['data']
        system_meta = system_info.model_dump()['data']['meta']
        print_response_list(system_data)
        uinp,page = determine_pagination(system_meta,page,limit)


def get_system_waypoints(systems_instance:openapi_client.SystemsApi):
    system_symbol = input('please input the system symbol: ')
    system_info = systems_instance.get_system_waypoints_with_http_info(system_symbol=system_symbol)
    print_response(system_info.model_dump()['data']['data'])

def get_waypoint(systems_instance:openapi_client.SystemsApi):
    system_symbol = input('please input the system symbo: ')
    waypoint_symbol = input('please input the system waypoint: ')
    system_info = systems_instance.get_waypoint_with_http_info(system_symbol=system_symbol,waypoint_symbol=waypoint_symbol)
    print_response(system_info.model_dump()['data']['data'])

def supply_construction(systems_instance:openapi_client.SystemsApi):
    system_symbol = input('please input the system symbol: ')
    waypoint_symbol = input('please input the waypoint symbol: ')
    supply_const_request = ''
    systems_instance.supply_construction_with_http_info(system_symbol=system_symbol,waypoint_symbol=waypoint_symbol,supply_construction_request=supply_const_request)
    print_response(system_info.model_dump()['data']['data'])



"""contracts"""

def accept_contract(contracts_instance:openapi_client.ContractsApi):
    contract_id = input('please input a contract id: ')
    contract_info = contracts_instance.accept_contract_with_http_info(contract_id=contract_id)
    print_response(contract_info.model_dump()['data']['data'])

def deliver_contract(contracts_instance:openapi_client.ContractsApi):
    contract_id = input('please input a contract id: ')
    deliver_contract_request = ''
    contract_info = contracts_instance.deliver_contract_with_http_info(contract_id=contract_id, deliver_contract_request=deliver_contract_request)
    print_response(contract_info.model_dump()['data']['data'])

def fulfill_contract(contracts_instance:openapi_client.ContractsApi):
    contract_id = input('please input a contract id: ')
    contract_info = contracts_instance.fulfill_contract_with_http_info(contract_id=contract_id)
    print_response(contract_info.model_dump()['data']['data'])

def get_contract(contracts_instance:openapi_client.ContractsApi):
    contract_id = input('please input a contract id: ')
    contract_info = contracts_instance.get_contract_with_http_info(contract_id=contract_id)
    print_response(contract_info.model_dump()['data']['data'])

def get_contracts(contracts_instance:openapi_client.ContractsApi,page,limit):
    uinp = ''
    while uinp != 'b':
        contract_info = contracts_instance.get_contracts_with_http_info(page=page,limit=limit)
        contract_data = contract_info.model_dump()['data']['data']
        contract_meta = contract_info.model_dump()['data']['meta']
        print_response_list(contract_data)
        uinp,page = determine_pagination(contract_meta,page,limit)

"""factions"""


"""fleet"""
    
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

    pagination_start_page = 1
    pagination_limit = 10

    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        agent_instance = openapi_client.AgentsApi(api_client)
        systems_instance = openapi_client.SystemsApi(api_client)
        contracts_instance = openapi_client.ContractsApi(api_client)
        fleet_instance = openapi_client.FleetApi(api_client)
        factions_instance = openapi_client.FactionsApi(api_client)
        agent_symbol = 'BAZEN' # str | The agent symbol (default to 'FEBA66')


        """ 
       



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
        fleet_instance.negotiate_contract_with_http_info("SHIPSYMBOL")
        fleet_instance.orbit_ship_with_http_info("SHIPSYMBOL")
        fleet_instance.purchase_ship_with_http_info("PURCHASESHIPREQUEST")
        fleet_instance.patch_ship_nav_with_http_info("SHIPSYMBOL","PATCHSHIPNAVREQUEST")
        fleet_instance.refuel_ship_with_http_info("SHIPSYMBOL","REFUELSHIPREQUEST")
        fleet_instance.repair_ship_with_http_info("SHIPSYMBOL")
        fleet_instance.scrap_ship_with_http_info("SHIPSYMBOL")
        fleet_instance.purchase_cargo_with_http_info("SHIPSYMBOL","PURCHASECARGOREQUEST")
        fleet_instance.remove_mount_with_http_info("SHIPSYMBOL","REMOVEMOUNTREQUEST")
        fleet_instance.sell_cargo_with_http_info("SHIPSYMBO","SELLCARGOREQUEST")
        fleet_instance.ship_refine_with_http_info("SHIPSYMBO","SHIPREFINEREQUEST")
        fleet_instance.siphon_resources_with_http_info("SHIPSYMBOL")
        fleet_instance.transfer_cargo_with_http_info("SHIPSYMBOL","TRANSFERCARGO")
        fleet_instance.warp_ship_with_http_info("SHIPSYMBOL","NAVIGATESHIPREQUEST")
        """
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
                        display_agents(agent_instance,pagination_start_page,pagination_limit)

            except ApiException as e:
                print(json.loads(e.body)['error']['message'])
                input("press any key to continue...")
            except Exception as e:
                print(e)
                input("press any key to continue...")