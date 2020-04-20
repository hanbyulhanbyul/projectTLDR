import pandas as pd
import nltk
SCCchat = pd.read_csv(r'SCCchat.csv')
df = pd.DataFrame(SCCchat)

top_N = 20
word_dist = nltk.FreqDist(SCCchat['User'])
print('All frequencies')
print('='*60)
rslt = pd.DataFrame(word_dist.most_common(top_N), columns=['Word', 'Frequency'])

print (rslt)
print ('='*60)