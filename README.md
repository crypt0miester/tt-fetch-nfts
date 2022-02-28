# Team Tuskers 
fetching nfts data from blockchain and downloads nfts (image and metadata) from arweave.

## Setup

'''
git clone https://github.com/
cd tuskers-fetch-nfts
virtualenv env
source env/bin/activate
pip install solana
'''

## Run
'''
python fetch_blockchain_data.py
'''
this will create "blockchain_data.json" that has all info of the Candy Machine address.

'''
python fetch_nfts_and_download.py
'''
this will create a folder called assets which has all nfts image and metadata 

In order to run against other collections change the address field in line 30 to your CM address. 