from imports import *

# def print_response(responsedata,waitinput):
#     print('\n')
#     for k,v in responsedata.items():
#         print(f'{str(k).replace("_"," ").title()}: {v}')
#     if waitinput == True:
#         input("press any key to continue...")
#     #print('\n')

# def print_response_list(responsedata):
#     for datum in responsedata:
#         print_response(datum,False)

# def determine_pagination(responsemeta, page, limit):
#     if limit * page > responsemeta['total']:
#         uinp = 'b'
#     else:
#         uinp = input("press enter for next page, or b to exit...")
#     page += 1
#     return (uinp,page)