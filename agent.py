from imports import *

# def display_agent(agent_instance: openapi_client.AgentsApi):
#     agent_name = input('please input an agent name: ')
#     #try:
#     agent_info = agent_instance.get_agent_with_http_info(agent_name)
#     #pprint(agent_info.model_dump()['data']['data'])
#     print_response(agent_info.model_dump()['data']['data'],True)

# def display_agents(agent_instance: openapi_client.AgentsApi,page,limit):
#     uinp = ''
#     while uinp != 'b':
#         agents_info = agent_instance.get_agents_with_http_info(limit=limit,page=page)
#         agents_data = agents_info.model_dump()['data']['data']
#         agents_meta = agents_info.model_dump()['data']['meta']
#         print_response_list(agents_data)
#         uinp,page = determine_pagination(agents_meta,page,limit)


#     # agent_instance.get_my_agent_with_http_info()
    

