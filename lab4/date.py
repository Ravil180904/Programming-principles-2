# 1. Write a Python program to subtract five days from current date.

from datetime import date, timedelta

today = date.today()

credit = today - timedelta(days = 5)
print(credit)
print()

#2. Write a Python program to print yesterday, today, tomorrow.
from datetime import date, timedelta
import datetime

today = date.today()

yesterday = today - timedelta(days = 1)

tomorrow = today + timedelta(days = 1)

print("Yesterday day: ", yesterday.strftime("%Y/%m/%d, %H:%M:%S"))
print("Today is ", today.strftime("%Y/%m/%d"))
print("Tomorrow day is ", tomorrow.strftime("%Y/%m/%d"))
print()

# 3. Write a Python program to drop microseconds from datetime.
from datetime import date, timedelta
import datetime

today = datetime.datetime.now()

today_drop_microseconds = today.replace(microsecond = 0)
print(today_drop_microseconds)
print()

# 4. Write a Python program to calculate two date difference in seconds.

import json

with open('lab4/json/sample-data.json', 'r') as file:
    data = json.load(file)

output = {
    "totalCount": str (len(data['imdata'])),
    "imdata": []
}

for item in ['imdata']:
    l1_phys_if = item ['l1physIf']['attributes']

format_interface = "{:50}".format (
    l1_phys_if ['adminSt'],
    l1_phys_if ['bw'],
    l1_phys_if ['mode']
)

print(format_interface)
print(f"Total count {output['totalCount']}")
