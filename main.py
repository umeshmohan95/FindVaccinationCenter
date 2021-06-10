import requests
import csv



user_selection = input('Find Vaccin based on district(1)/pincode(2) or enter 3 to view all District Names (enter no): ')


if user_selection=='2':

    pincode = input('Enter pincode: ')
    date = input('Enter date(31-05-2021): ')

    setuapi_endpoint = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin'
    setuapi_params={
        'pincode': pincode,
        'date': date
    }

    # get your state id by using this : https://cdn-api.co-vin.in/api/v2/admin/location/states and use this
    # https://cdn-api.co-vin.in/api/v2/admin/location/districts/1 to get all district details instead of 1 replace it with your desired state_id(which you got from 1st url)

    response =  requests.get(url=setuapi_endpoint, params=setuapi_params)
    # response =  requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?'district_id'=266&date=12-06-2021')
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

elif user_selection == '1':

    dist = input('Enter District: ')
    date = input('Enter date(31-05-2021): ')
    dist_code = ''

    with open('data_file.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if len(line) != 0:
                # print(line)
                if line[1].lower() == dist.lower():
                    dist_code = line[0]

    setuapi_endpoint = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict'
    setuapi_params = {
        'district_id': dist_code,
        'date': date
    }

    response =  requests.get(url=setuapi_endpoint, params=setuapi_params)
    # response =  requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?'district_id'=266&date=12-06-2021')
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
else:

    with open('data_file.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if len(line) != 0:
                print(line[1])

    print('Please find the list of District to select')
