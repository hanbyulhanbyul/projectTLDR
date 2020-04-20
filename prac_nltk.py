import nltk
nltk.download('punkt')
sentence = 'my name is charlie and i am not happy, please help'

tokens = nltk.word_tokenize(sentence)
print (tokens)

