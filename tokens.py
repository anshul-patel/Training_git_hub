import nltk


'''from anshul import demo
d=demo()
speech=d.audio()'''
#removing stopwords
from nltk.corpus import stopwords

stops=stopwords.words("English")


def stem_with_porter(words):
    porter=nltk.PorterStemmer()
    new_words=[porter.stem(w) for w in words]
    return new_words

def stem_with_lancaster(words):
    porter=nltk.LancasterStemmer()
    new_words=[porter.stem(w) for w in words]
    return new_words

str="enter elements in an array"

a=stem_with_porter(str.split())
print(a)
'''
b=stem_with_lancaster(str.split())
print(b)
'''
