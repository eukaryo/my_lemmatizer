# my_lemmatizer

nltkのWordNetLemmatizerは、単語と品詞を入力するとWordNetを読みに行って見出し語化してくれる。返り値はstrで、入力単語の見出し語。ただし、入力単語がWordNetに無かった場合は入力単語をそのまま返す。　https://www.nltk.org/_modules/nltk/stem/wordnet.html

入力単語が見出し語だったのかWordNetに無かったのか区別できないと使いにくいので、それがどちらなのかのbool値を含めた(str, bool)を返り値とする修正版を作った。

from nltk.stem import WordNetLemmatizer する代わりに import my_lemmatizerして同じように使う。(cf: main.py)
