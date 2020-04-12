import pandas as pd
SCCchat = pd.read_csv(r'SCCchat.csv')
df = pd.DataFrame(SCCchat)
df.columns = ["date", "name", "msg"]
print (date)