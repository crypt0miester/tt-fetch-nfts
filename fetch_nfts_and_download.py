import json
import time
import struct
from multiprocessing.pool import ThreadPool
from construct import Bytes, Flag, Int8ul
from construct import Struct as cStruct  # type: ignore
import base58
import base64
import json
import requests
from os import path
        


def unpack_metadata_account(data):
    assert(data[0] == 4)
    i = 1
    source_account = base58.b58encode(bytes(struct.unpack('<' + "B"*32, data[i:i+32])))
    i += 32
    mint_account = base58.b58encode(bytes(struct.unpack('<' + "B"*32, data[i:i+32])))
    i += 32
    name_len = struct.unpack('<I', data[i:i+4])[0]
    i += 4
    name = struct.unpack('<' + "B"*name_len, data[i:i+name_len])
    i += name_len
    symbol_len = struct.unpack('<I', data[i:i+4])[0]
    i += 4 
    symbol = struct.unpack('<' + "B"*symbol_len, data[i:i+symbol_len])
    i += symbol_len
    uri_len = struct.unpack('<I', data[i:i+4])[0]
    i += 4 
    uri = struct.unpack('<' + "B"*uri_len, data[i:i+uri_len])
    i += uri_len
    fee = struct.unpack('<h', data[i:i+2])[0]
    i += 2
    has_creator = data[i] 
    i += 1
    creators = []
    verified = []
    share = []
    if has_creator:
        creator_len = struct.unpack('<I', data[i:i+4])[0]
        i += 4
        for _ in range(creator_len):
            creator = base58.b58encode(bytes(struct.unpack('<' + "B"*32, data[i:i+32])))
            creators.append(creator)
            i += 32
            verified.append(data[i])
            i += 1
            share.append(data[i])
            i += 1
    primary_sale_happened = bool(data[i])
    i += 1
    is_mutable = bool(data[i])
    metadata = {
        "update_authority": source_account,
        "mint": mint_account,
        "data": {
            "name": bytes(name).decode("utf-8").strip("\x00"),
            "symbol": bytes(symbol).decode("utf-8").strip("\x00"),
            "uri": bytes(uri).decode("utf-8").strip("\x00"),
            "seller_fee_basis_points": fee,
            "creators": creators,
            "verified": verified,
            "share": share,
        },
        "primary_sale_happened": primary_sale_happened,
        "is_mutable": is_mutable,
    }
    return metadata
    

def download_png_and_json(index):
    with open(f'blockchain_data.json', 'rb') as f:
        raw_tokens_info = json.load(f)

    unpacked = unpack_metadata_account(base64.b64decode(raw_tokens_info['result'][index]['account']['data'][0]))
    file_name = unpacked['data']['name'][14:]
    metadata_json_url = unpacked['data']['uri'] 
    print(f'working on {file_name}')
    if not path.exists(f'assets/{file_name}.png'):
        resp = json.loads(requests.get(metadata_json_url).text)
        with open(f'assets/{file_name}.json', 'w', encoding='utf-8') as f:
            json.dump(resp, f, ensure_ascii=False, indent=4)

        image_url = resp['image']
        
        # dirty work around due to arweave not resolving sometimes.
        try:
            requested_image = requests.get(image_url, allow_redirects=True)
        except: 
            time.sleep(2)
            requested_image = requests.get(image_url, allow_redirects=True)

        with open(f"assets/{file_name}.png", "wb") as f:
            f.write(requested_image.content)

data_length = 9876
list_of_index = [index for index in range(9876)]
interval = 0
workers = 12

for data in range(int(data_length/workers)):
    list_in_pool = list_of_index[interval:interval+workers]

    p = ThreadPool(workers)
    p.map(download_png_and_json, list_in_pool)
    p.close()
    p.join()
    time.sleep(0.5)
    interval += workers

