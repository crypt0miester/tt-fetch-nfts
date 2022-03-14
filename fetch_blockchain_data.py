
from solana.rpc.api import Client
import requests
import json 

payload = {
    "method": "getProgramAccounts",
    "jsonrpc": "2.0",
    "params": [
        "metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s",
        {
            "encoding": "base64",
            "filters": [
                {
                    "memcmp": {
                        "offset": 326,
                        "bytes": "",
                    }
                }
            ],
        },
    ],
    "id": "f0e26f8e-7c9b-40f6-a712-af65978b67da",
}

# api_endpoint = "https://free.rpcpool.com/"
# api_endpoint = "https://api.mainnet-beta.solana.com"

api_endpoint = "https://ssc-dao.genesysgo.net"

address= "6NA8MuVWUxAaxKgM3JXyeGhPjuCqHvkb6R5bLwsG255X" # TUSKERS CM

payload["params"][1]["filters"][0]["memcmp"]["bytes"] = address
resp = json.loads(requests.post(api_endpoint, json = payload).text)
with open('blockchain_data.json', 'w', encoding='utf-8') as f:
    json.dump(resp, f, ensure_ascii=False, indent=4)
