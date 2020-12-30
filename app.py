# -*- coding: utf-8 -*-
import yaml
import io

# Read YAML file
with open("test.yaml", 'r') as stream:
    data = yaml.safe_load(stream)

for key, value  in data.items():
    print(key,value)

print("=================================")

data['doe']['xmas-fifth-day']['french-hens']=1000

print(data['doe']['xmas-fifth-day']['french-hens'])


# Write YAML file
with io.open('data.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)
    print("done")

