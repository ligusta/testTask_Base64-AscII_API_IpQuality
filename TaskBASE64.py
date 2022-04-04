import base64
import pandas as pd

df = pd.read_csv('b64.csv', header=None)

cutoff_list = []

for i in range(len(df)):

    sfile = df.values[i][0]

    base64_message = sfile
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    cutoff_list.append(message)

my_df = pd.DataFrame(cutoff_list)
my_df.columns = ['ip']
my_df.to_csv('list_ip.csv', index=False)

print(my_df)