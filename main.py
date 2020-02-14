from nltk.stem import WordNetLemmatizer
import my_lemmatizer

# 初回
# import nltk
# nltk.download("all")

word_list=[("better","n"),("better","a"),("better","r"),("met","v"),("sdgaseszdcgs","n")]

lemmatizer = WordNetLemmatizer()
my_lemmatizer = my_lemmatizer.My_WordNetLemmatizer()

for word in word_list:
    print(word[0] + ", lemmatizer: " + str(lemmatizer.lemmatize(word[0], pos=word[1])))
    print(word[0] + ", my_lemmatizer: " + str(my_lemmatizer.my_lemmatize(word[0], pos=word[1])))


