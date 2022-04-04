import pandas as pd
import requests

df = pd.read_csv('list_ip.csv')

cutoff_list = []
ip_list = []

for y in range (0,200):

    ip = df.iloc[y]

    url = ('https://ipqualityscore.com/api/json/ip')
    params = {
        'key': 'YOUR_API_KEY',
        'ip': ip,
        'strictness': 2,
        'allow_public_access_points': 'true',
        'mobil': 'false',
        'fast': 'false',
        'lighter_penalties': 'false'

    }

    response = requests.get(url, params)
    data = response.json()

    cutoff_list.append(data)
    ip_list.append(ip)


my_df = pd.DataFrame(cutoff_list)
my_df_ip = pd.DataFrame(ip_list)

extracted_col = my_df_ip['ip']
my_df = my_df.join(extracted_col)

my_df.to_csv('list.csv', index=False)
print(my_df)