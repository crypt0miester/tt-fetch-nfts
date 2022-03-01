import json
import glob

result = []
for f in glob.glob("assets/*.json"):
    with open(f, "r") as infile:
        y = {}
        t = json.load(infile)
        y['name'] = t['name']
        for attribute in t['attributes']:
            y[attribute['trait_type']] = attribute['value']
        # print(y)
        result.append(y)

with open("merged.json", "w") as outfile:
    json.dump(result, outfile, ensure_ascii=False, indent=4)