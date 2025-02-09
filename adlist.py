from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *
import jaconv
import time
import re

# class MainTextCharFilter(CharFilter):

#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

#     def apply(self, text):
#         return text.split(self.start)[1].split(self.end)[0]

# char_filters = [UnicodeNormalizeCharFilter()] # UnicodeをNFKC(デフォルト)で正規化
                # MainTextCharFilter('<div class="main_text">', '<div class="bibliographical_information">'), # 本文を抽出
                # RegexReplaceCharFilter('<rp>\(.*?\)</rp>', ''), # ルビを削除
                # RegexReplaceCharFilter('<.*?>', '')
                # HTMLタグを削除

t = Tokenizer()
# analyzer = Analyzer(char_filters=UnicodeNormalizeCharFilter(), tokenizer=t, token_filters=CompoundNounFilter())

added_word = []
a = 0
more = "y"

q = re.compile("[\u30A1-\u30FC]+")

s = input("Enter text:")

for tok in t.tokenize(s):
    pos = tok.part_of_speech.split(',')
    if '名詞' in pos:
        print("表層形：" + str(tok.surface))  # 表層形を出力
        yomi = str(tok.reading)
        print(yomi)
        
        with open("list.txt", "r") as f:
            read = f.read().split("\n")
            if yomi in read:
                print("すでに追加された単語です。")
                ad = "n"
                time.sleep(0.3)
            else:
                ad = input("追加しますか？ y or n : ")
        if ad == "y" or ad == "ｙ":
                co = input("訂正しますか？ y or n : ")

                if co == "n"  or co == "ｎ" :
                    while not q.fullmatch(yomi) and yomi != "q":
                        print("カタカナではありません！")
                        yomi = input("読みを入力してください。(q:キャンセル)：")
                    
                    if yomi == "q":
                        print("キャンセルしました。")
                    else:
                        with open("list.txt", "a") as f:
                            f.write(yomi + "\n")
                            added_word.append(yomi)
                            print("追加しました。")
                            a += 1
                else:
                    co_word = input("読みを入力してください。：")
                    while not q.fullmatch(co_word):
                        print("カタカナではありません！")
                        co_word = input("読みを入力してください。(q:キャンセル)：")
                        if co_word == "q":
                            break

                    if co_word in read:
                        print("すでに追加された単語です。")
                    elif co_word == "q":
                        print("キャンセルしました。")
                    else:
                        with open("list.txt", "a") as f:
                            f.write(co_word + "\n")
                            added_word.append(co_word)
                            print("追加しました。")
                            a += 1

while more == "y" or more == "ｙ":
    more = input("他に追加する単語はありますか？ y or n : ")
    if more == "y" or more == "ｙ":
        more_word = input("追加する単語を入力してください：")
        with open("list.txt", "r") as f:
            read = f.read().split("\n")
            if more_word in read:
                print("すでに追加された単語です。")
            elif not q.fullmatch(more_word):
                print("カタカナで入力してください。")
            else:
                k = input("「" + more_word + "」を追加しますか？ y or n : ")
                if k == "y" or k == "ｙ":
                    with open("list.txt", "a") as f:
                        f.write(more_word + "\n")
                        added_word.append(more_word)
                        print("追加しました。")
                        a += 1
                elif k == "n" or k == "ｎ":
                    continue
                else:
                    print("入力エラー")
                    continue
    elif more == "n" or more == "ｎ":
        break
    else:
        print("入力エラー")
        continue

print("______")
if a > 1:
    print("added " + str(a) + " words:" + str(added_word))
elif a == 1:
    print("added " + str(a) + " word:" + str(added_word))
else:
    print("no added words.")
