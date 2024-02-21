import json

with open('lab4/json/sample-data.json', 'r') as file:
    data = json.load(file)

output = {
    "totalCount": str (len(data['imdata'])),
    "imdata": []
}

for item in data['imdata']:
    l1PhysIf = item ["l1PhysIf"]['attributes']

format_topology = "{:<20} {:<50} {:<60}".format (
    l1PhysIf ['dn']
    l1PhysIf ['fecMode']
    l1PhysIf ['mtu']
)

"""format_interface = "{:<50} {:<20} {:<80}".format (
    l1PhysIf ['adminSt']
    l1PhysIf ['bw']
    l1PhysIf ['mode']
)"""

print('Interface Status')
print("="*80)
print("DN" "                      " "Description" "         "  "Speed" "     " "MTU")
print("-"*80)
print(format_topology)
print(f"Total count {output['totalCount']}")