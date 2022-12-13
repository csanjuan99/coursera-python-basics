import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

text = "Hello, my name is John. I am 20 years old. I live in New York."

print(word_tokenize(text))
print(nltk.tokenize.sent_tokenize(text))

stopwords = stopwords.words('english')
new_text = []
for i in text.split():
    if i not in stopwords:
        new_text.append(i)

print(new_text)
