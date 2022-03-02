# TT fetch nfts
fetching nfts data from blockchain and downloads nfts (image and metadata) from arweave.

## Setup
make sure you have python3 and pip3 and virtualenv installed on your system.
```
git clone https://github.com/crypt0miester/tt-fetch-nfts.git
cd tuskers-fetch-nfts
virtualenv env
source env/bin/activate
pip3 install solana
```

## Run
```
python3 fetch_blockchain_data.py
```
this will create "blockchain_data.json" that has all info of the Candy Machine address.

```
python3 fetch_nfts_and_download.py
```
this will create a folder called assets which has all nfts image and metadata 

## More data
if you would like to fetch more data run the following:

```
python3 merge_json_files_to_one.py
```
this will create a json file contianing all names and attributes of the collection.

```
python3 count_occurrence_in_merged.py
```
this will create a json file containing all occurance of a property/attribute in the collection. (useful for analytics)

In order to run against other collections change the address field in line 30 to your CM address. 

you might want to remove the .gitkeep file in assets folder 
