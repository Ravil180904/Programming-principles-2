import json

with open('lab4/json/sample-data.json', 'r') as file:
    data = json.load(file)

output = {
    "totalCount": str (len(data['imdata'])),
    "imdata": []
}

for item in ['imdata']:
    l1_phys_if = item ['l1physIf']['attributes']

format_interface = "{:<50} {:<80} {:<30}".format (
    l1_phys_if = ['adminSt'],
    l1_phys_if = ['bw'],
    l1_phys_if = ['mode']
)

print(format_interface)
print("="*80)
print(f"Total count {output['totalCount']}")
