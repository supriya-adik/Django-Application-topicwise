import json
from pprint import  pprint
with open("company.json","r") as f :
    d = json.loads(f.read())

pprint(d)
print(help(pprint.pprint))