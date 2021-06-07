import requests

setuapi_endpoint= 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin'

pincode = input('Enter pincode: ')
date = input('Enter date(31-05-2021): ')

setuapi_params={
    'pincode': pincode,
    'date': date
}

# response =  requests.get(url=f'{setuapi_endpoint}?pincode={pincode}&date={date}')
response =  requests.get(url=setuapi_endpoint, params=setuapi_params)
response.raise_for_status()
data = response.json()
# print(data)
total_ward = len(data['sessions'])

if total_ward > 0:
    for i in range(total_ward):
        if (data["sessions"][i]["available_capacity"]>0):
            print(f'------------------------------------------------------------------------------------------')
            print(f'Ward No: {i+1}\nFees Type: {data["sessions"][i]["fee_type"]}\nMinimum Age: {data["sessions"][i]["min_age_limit"]}\n  Ward Name: {data["sessions"][i]["name"]}\n Address: {data["sessions"][i]["address"]}'
                  f'\n Address: {data["sessions"][i]["state_name"]}\n Vaccine: {data["sessions"][i]["vaccine"]}\n Available Slot Count: {len(data["sessions"][i]["slots"])}\n Slots: {data["sessions"][i]["slots"]}'
                  f'\n Total Vaccin: {data["sessions"][i]["available_capacity"]}\n           Dose1 Available: {data["sessions"][i]["available_capacity_dose1"]}'
                  f'\n           Dose2 Available: {data["sessions"][i]["available_capacity_dose2"]}\n')
        else:
            print(f'------------------------------------------------------------------------------------------')
            print(f'Currently no Vaccine available at Ward: {data["sessions"][i]["name"]}\n ')

# else:
    # print('Sorry. Currently no Vaccine available in your area')