import sys

import json

try:
    file_path = sys.argv[1]

except IndexError:
    print("USAGE: python3 jsonify.py <file-path>")
    sys.exit(1)

file = open(file_path, 'r').readlines()

json_dict = {}

for line in file:
    content = line.strip().split(':')
    json_dict[content[0].strip()] = content[1].strip()

with open('output.json', 'w') as file:
    json_ctt = json.dumps(json_dict, indent=4)
    file.write(json_ctt)