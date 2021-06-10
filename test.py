
import csv
import json


#### to conver JSON to CSV
# into the variable data
with open('data.json') as json_file:
    data = json.load(json_file)

districts_data = data['districts']

# now we will open a file for writing
data_file = open('data_file.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for district in districts_data:
    if count == 0:
        # Writing headers of CSV file
        header = district.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(district.values())

data_file.close()

##################################################################
# # to convert CSV to DICT
# d = {}
# value=''
# # your_path = pathlib.PurePath(dirName).joinpath(filename)
# with open('data_file.csv','r') as f:
#     reader = csv.reader(f)
#     for line in reader:
#         if len(line) != 0:
#             # print(line)
#             if line[0] == '266':
#
#                 value = line[1]
#
# print(value)