import requests
from collections import Counter
import json


with open(f"merged.json", "r") as f:
    json_obj = json.load(f)

bg = Counter(item['Background'] for item in json_obj)
body = Counter(item['Body'] for item in json_obj)
clothing = Counter(item['Clothing'] for item in json_obj)
tusks  = Counter(item['Tusks'] for item in json_obj)
tuskwear  = Counter(item['Tuskwear'] for item in json_obj)
headwear = Counter(item['Headwear'] for item in json_obj)
eyes = Counter(item['Eyes'] for item in json_obj)
holding = Counter(item['Holding'] for item in json_obj)

occurrence = {}

occurrence['background'] = dict(bg)
occurrence['body'] = dict(body)
occurrence['clothing'] = dict(clothing)
occurrence['tusks'] = dict(tusks)
occurrence['tuskwear'] = dict(tuskwear)
occurrence['headwear'] = dict(headwear)
occurrence['eyes'] = dict(eyes)
occurrence['holding'] = dict(holding)


with open("occurrence.json", "w") as outfile:
    json.dump(occurrence, outfile, ensure_ascii=False, indent=4)