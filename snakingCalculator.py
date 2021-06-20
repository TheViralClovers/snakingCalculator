import requests
import json
from tabulate import tabulate
import time

common_snake = 1000
uncommon_snake = 3500
rare_snake = 12500
classic_snake = 35000
sketch_snake = 100000

final_table_list = []

page = 1
common_count = 0
uncommon_count = 0
rare_count = 0
classic_count = 0
sketch_count = 0
checkComplete = 0
owner = input("Enter your wax address ")

complete_raw_data = []
# response = requests.get("https://wax.api.atomicassets.io/atomicassets/v1/assets?owner=k3bri.wam&collection_name=novarallywax&page=1&limit=9999999999&order=desc&sort=asset_id")

while checkComplete == 0:
    response = requests.get(f"https://wax.api.atomicassets.io/atomicassets/v1/assets?owner={owner}&collection_name=novarallywax&page={page}&limit=1000&order=desc&sort=asset_id")
    raw_data = json.loads(response.content)
    complete_raw_data += raw_data["data"]
    if len(raw_data["data"]) == 1000:
        # print(page)
        page += 1      
    else:
        checkComplete = 1
        
# print(len(complete_raw_data))

for i in range(len(complete_raw_data)):
    rarity = complete_raw_data[i]["template"]["immutable_data"]["Rarity"]
    if rarity == "Common":
        common_count += 1
    if rarity == "Uncommon":
        uncommon_count += 1
    if rarity == "Rare":
        rare_count += 1
    if rarity == "Classic":
        classic_count += 1
    if rarity == "Sketch":
        sketch_count += 1

common_row = list(("COMMON",common_count,(common_count*common_snake),(common_count*common_snake/10)))
uncommon_row = list(("UNCOMMON",uncommon_count,(uncommon_count*uncommon_snake),(uncommon_count*uncommon_snake/10)))
rare_row = list(("RARE",rare_count,(rare_count*rare_snake),(rare_count*rare_snake/10)))
classic_row = list(("CLASSIC",classic_count,(classic_count*classic_snake),(classic_count*classic_snake/10)))
sketch_row = list(("SKETCH",sketch_count,(sketch_count*sketch_snake),(sketch_count*sketch_snake/10)))
final_table_list = list((common_row,uncommon_row,rare_row,classic_row,sketch_row))

# print(final_table_list)

table = tabulate(final_table_list, headers=["","Quantity","Snaking Power","Snaking Power Pre-launch"], tablefmt='orgtbl')
# print(common_count,uncommon_count,rare_count,classic_count,sketch_count)
print("\n")

print(table)

total_snake = (common_count*common_snake) + (uncommon_count*uncommon_snake) + (rare_count*rare_snake) + (classic_count*classic_snake) + (sketch_count*sketch_snake)
# print(total_snake)

print(f"\nYou will be making {total_snake} Snake Oil per day and {total_snake/10} Snake Oil per day before launch\nMade by TheViralClovers/k3bri.wam")

while True:
    time.sleep(1000)