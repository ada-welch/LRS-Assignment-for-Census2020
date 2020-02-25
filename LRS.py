import requests
import json
import pandas as pd

#short on time and couldn't immediately figure out how to do multiple counties in a call so just did them separately.

response_bx = requests.get("https://api.census.gov/data/2018/pdb/tract?get=State_name,County_name,Low_Response_Score&for=tract:*&in=state:36%20county:005&key=b2e2dbfa82650b43d8df510d878c9c73f42d2a4a")
print("bx_status", response_bx.status_code)
response_bklyn = requests.get("https://api.census.gov/data/2018/pdb/tract?get=State_name,County_name,Low_Response_Score&for=tract:*&in=state:36%20county:047&key=b2e2dbfa82650b43d8df510d878c9c73f42d2a4a")
print("bklyn_status", response_bklyn.status_code)
response_ny = requests.get("https://api.census.gov/data/2018/pdb/tract?get=State_name,County_name,Low_Response_Score&for=tract:*&in=state:36%20county:061&key=b2e2dbfa82650b43d8df510d878c9c73f42d2a4a")
print("ny_status", response_ny.status_code)
response_qns = requests.get("https://api.census.gov/data/2018/pdb/tract?get=State_name,County_name,Low_Response_Score&for=tract:*&in=state:36%20county:081&key=b2e2dbfa82650b43d8df510d878c9c73f42d2a4a")
print("qns_status", response_qns.status_code)
response_rich = requests.get("https://api.census.gov/data/2018/pdb/tract?get=State_name,County_name,Low_Response_Score&for=tract:*&in=state:36%20county:085&key=b2e2dbfa82650b43d8df510d878c9c73f42d2a4a")
print("statenisland_status", response_rich.status_code)

bronx = json.loads(response_bx.text)
brooklyn = json.loads(response_bklyn.text)
queens = json.loads(response_qns.text)
richmond = json.loads(response_rich.text)
ny = json.loads(response_ny.text)

all_nyc = bronx + brooklyn + queens + richmond + ny

#write code that goes through each list in the list and extracts the county, census tract, and LRS  and stores it in a dataframe. write the dataframe to a csv file.

column_names = ["County", "CT", "LRS"]
df = pd.DataFrame(columns = column_names)

df_length = len(df)

for i in all_nyc:
    to_append = [i[1], i[5], i[2]]
    df.loc[df_length] = to_append
    df_length = len(df)

print("number of rows in df:", len(df))
print(df)

df.to_csv("nyc_lrs.csv", index=False)




