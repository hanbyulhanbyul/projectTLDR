import pandas as pd
SCCchat = pd.read_csv(r'SCCchat.csv')
df = pd.DataFrame(SCCchat)

name = [1]
names = df[df.columns[name]]
msg = [2]
msgs = df[df.columns[msg]]
print(msgs)

# values = df.values
# date = df.index
# type = df.columns
# print(values)

