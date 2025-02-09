import time
import re
import sys
import random
import jaconv
from concurrent.futures import ThreadPoolExecutor

m = "n"
t = 0
# turn = 0
name2make = 0
word_count = 1
lil = 0

def get_word():
    Word = input("    「" + jaconv.kata2hira(siri) + "」から始まる言葉を入れてね: ")
    return Word

while True:
    mode = input("モードを選んでね\n　1:comと対戦\n　2:ふたりで対戦\n　0:プログラム終了\n")
    if mode != "0" and mode != "1" and mode != "2":
        print("入力エラー！(半角数字で入力してね)")
        time.sleep(0.1)
        continue
    mode = int(mode)
    if mode == 0:
        sys.exit("プログラムを終了します。。。")
    
    if mode == 1:
        nannido = input("難易度を選んでね\n　1:よわい\n　2:つよい\n　0:もどる\n")
        if nannido != "0" and nannido != "1" and nannido != "2":
            print("入力エラー！(半角数字で入力してね)")
            time.sleep(0.1)
            continue
        elif nannido == "0":
            time.sleep(0.1)
            continue

        name1 = input("名前を入力してね：")
        if name1 == "":
            name1 = "player"
        name2 = "com"
        break
    else:
        name1 = input("１人目の名前を入力してね：")
        if name1 == "":
            name1 = "player1"
        name2 = input("２人目の名前を入力してね：")
        if name2 == "":
            name2 = "player2"
        break
time.sleep(0.1)
while True:
    menu = input("メニュー\n　1:しりとりスタート\n　2:しばり設定\n　0:プログラム終了\n")

    if menu == "2":
        s = input("しばりメニュー\n　1:時間\n　2:文字数\n　0:もどる\n")
        if s == "1":
            t = input("制限時間を秒数で指定してね(0でキャンセル)：")
            if t.isdecimal():
                t = int(t)
                if t == 0:
                    print("キャンセルしました")
                    continue
                print(str(t) + "秒に設定しました！")
            else:
                print("入力エラー！")
                t = 0
                continue
        elif s == "2":
            m = input("文字数しばりをつけますか？　y or n ：")
            if m != "y" and m != "n":
                print("入力エラー！")
                continue
            else:
                print("おっけー！")
        elif s == "0":
            continue
        else:
            print("入力エラー！")
            continue

    elif menu == "1":
        print("しりとりしよう！")
        break
    elif menu == "0":
        sys.exit("プログラムを終了します。。。")
    else:
        print("入力エラー！")
        continue

# with open("list.txt", "r") as f:
#     l = f.read().split("\n")

siri = "リ"
used_word = ["シリトリ"]
pq = re.compile('[\u3041-\u3094 + \u30A1-\u30FC]+')
d = re.compile("[\u309B-\u309C]+")

if mode == 1:
    with open("list.txt", "r") as l:
        list = l.read().split("\n")
        list.remove("")

time.sleep(0.2)
print("【 ひらがな or カタカナ(全角) 】で入力してね")
print("（「こうさん」と入力すると、ゲーム終了）")
time.sleep(0.5)
print("じゃあ、しりとりの「り」から！")
z = 0
while True:
    if name2make == 1:
        break

    time.sleep(0.7)
    print(name1 + "のターン！")
    if m == "y" and z == 0:
        time.sleep(1)
        mn = random.randint(2,7)
        if mn == 7:
            print("7文字以上！")
        else:
            print(str(mn) + "文字！")
    
    time.sleep(1)
    if t != 0:
        with ThreadPoolExecutor() as executor:
            feature = executor.submit(get_word)
            for i in range(0,t):
                time.sleep(0.5)
                if not feature.running():
                    break
                time.sleep(0.5)
                if not feature.running():
                    break
            if feature.running():
                feature.cancelled()
                # print(feature.running())
                print("\n...時間切れ！\n"+name2+"の勝ち！(Press Enter)")
                break
            Word = feature.result()
    else:
        Word = get_word()
    
    if Word == "":
        print("なんか言ってよ～～")
        z = 1
        continue

    Word = jaconv.hira2kata(Word)
    mozisuu = len(Word)

    if Word == "コウサン":
        print(name1 + "の負け～！")
        break
    
    if d.search(Word):
        print("濁点、半濁点を単独で使わないで！")
        z = 1
        continue

    if not pq.fullmatch(Word):
        print("ひらがなかカタカナ(全角)で入力して！")
        z = 1
        continue

    if Word[0] != siri:
        print("最初の文字が違うよ～")
        z = 1
        continue

    if m == "y":
        if mn == 7:
            if mozisuu < 7:
                print("7文字以上だって！")
                z = 1
                continue
        else:
            if mozisuu != mn:
                print(str(mn) + "文字だって！")
                z = 1
                continue

    if Word in used_word:
        print("それはもう言ったよ！　" + name2 + "の勝ち！")
        break

    if Word[-1] == "ー":
        bou_word = Word
        Word = Word[:-1]
        bou = 1
    else:
        bou = 0
    
    if Word[-1] == "ャ":
        Word = Word[:-1] + "ヤ"
        lil = 1
    elif Word[-1] == "ュ": 
        Word = Word[:-1] + "ユ"
        lil = 1
    elif Word[-1] == "ョ": 
        Word = Word[:-1] + "ヨ"
        lil = 1
    elif Word[-1] == "ァ": 
        Word = Word[:-1] + "ア"
        lil = 1
    elif Word[-1] == "ィ": 
        Word = Word[:-1] + "イ"
        lil = 1
    elif Word[-1] == "ゥ": 
        Word = Word[:-1] + "ウ"
        lil = 1
    elif Word[-1] == "ェ": 
        Word = Word[:-1] + "エ"
        lil = 1
    elif Word[-1] == "ォ": 
        Word = Word[:-1] + "オ"
        lil = 1

    if Word[-1] == "ン":
        print("「ん」で終わってるから、" + name2 + "の勝ち！")
        if bou == 1:
            Word = bou_word
        used_word.append(Word)
        word_count += 1
        break

    siri = Word[-1]

    if lil == 1:
        if Word[-1] == "ヤ":
            Word = Word[:-1] + "ャ"
        elif Word[-1] == "ユ": 
            Word = Word[:-1] + "ュ"
        elif Word[-1] == "ヨ": 
            Word = Word[:-1] + "ョ"
        elif Word[-1] == "ア": 
            Word = Word[:-1] + "ァ"
        elif Word[-1] == "イ": 
            Word = Word[:-1] + "ィ"
        elif Word[-1] == "ウ": 
            Word = Word[:-1] + "ゥ"
        elif Word[-1] == "エ": 
            Word = Word[:-1] + "ェ"
        elif Word[-1] == "オ": 
            Word = Word[:-1] + "ォ"
        
        lil = 0

    if bou == 1:
        Word = bou_word

    used_word.append(Word)
    word_count += 1
    z = 0

    # 相手
    if mode == 2:
        z = 0

        while True:
            time.sleep(1)
            print("\n"+ name2 + "のターン！")
            if m == "y" and z == 0:
                time.sleep(1)
                mn = random.randint(2,7)
                if mn == 7:
                    print("7文字以上！")
                else:
                    print(str(mn) + "文字！")
            
            time.sleep(1)
            if t != 0:
                with ThreadPoolExecutor() as executor:
                    feature = executor.submit(get_word)
                    for i in range(0,t):
                        time.sleep(0.5)
                        if not feature.running():
                            break
                        time.sleep(0.5)
                        if not feature.running():
                            break
                    if feature.running():
                        feature.cancelled()
                        # print(feature.running())
                        print("\n...時間切れ！\n"+name1+"の勝ち！(Press Enter)")
                        name2make = 1
                        break
                    Word = feature.result()
            else:
                Word = get_word()

            if Word == "":
                print("なんか言ってよ～～")
                z = 1
                continue

            Word = jaconv.hira2kata(Word)
            mozisuu = len(Word)

            if Word == "コウサン":
                print(name2 + "の負け～！")
                name2make = 1
                break

            if d.search(Word):
                print("濁点、半濁点を単独で使わないで！")
                z = 1
                continue
            if not pq.fullmatch(Word):
                print("ひらがなかカタカナで入力して！")
                z = 1
                print(Word)
                continue

            if Word[0] != siri:
                print("最初の文字が違うよ～")
                z = 1
                continue

            if m == "y":
                if mn == 7:
                    if mozisuu < 7:
                        print("7文字以上だって！")
                        z = 1
                        continue
                else:
                    if mozisuu != mn:
                        print(str(mn) + "文字だって！")
                        z = 1
                        continue

            if Word in used_word:
                print("それはもう言ったよ！　" + name1 + "の勝ち！")
                name2make = 1
                break

            if Word[-1] == "ー":
                bou_word = Word
                Word = Word[:-1]
                bou = 1
            else:
                bou = 0
            
            if Word[-1] == "ャ":
                Word = Word[:-1] + "ヤ"
                lil = 1
            elif Word[-1] == "ュ": 
                Word = Word[:-1] + "ユ"
                lil = 1
            elif Word[-1] == "ョ": 
                Word = Word[:-1] + "ヨ"
                lil = 1
            elif Word[-1] == "ァ": 
                Word = Word[:-1] + "ア"
                lil = 1
            elif Word[-1] == "ィ": 
                Word = Word[:-1] + "イ"
                lil = 1
            elif Word[-1] == "ゥ": 
                Word = Word[:-1] + "ウ"
                lil = 1
            elif Word[-1] == "ェ": 
                Word = Word[:-1] + "エ"
                lil = 1
            elif Word[-1] == "ォ": 
                Word = Word[:-1] + "オ"
                lil = 1

            if Word[-1] == "ン":
                print("「ん」で終わってるから、" + name1 + "の勝ち！")
                name2make = 1
                if bou == 1:
                    Word = bou_word
                used_word.append(Word)
                word_count += 1
                break

            siri = Word[-1]

            if lil == 1:
                if Word[-1] == "ヤ":
                    Word = Word[:-1] + "ャ"
                elif Word[-1] == "ユ": 
                    Word = Word[:-1] + "ュ"
                elif Word[-1] == "ヨ": 
                    Word = Word[:-1] + "ョ"
                elif Word[-1] == "ア": 
                    Word = Word[:-1] + "ァ"
                elif Word[-1] == "イ": 
                    Word = Word[:-1] + "ィ"
                elif Word[-1] == "ウ": 
                    Word = Word[:-1] + "ゥ"
                elif Word[-1] == "エ": 
                    Word = Word[:-1] + "ェ"
                elif Word[-1] == "オ": 
                    Word = Word[:-1] + "ォ"
                
                lil = 0

            if bou == 1:
                Word = bou_word

            used_word.append(Word)
            word_count += 1
            print()
            z = 0
            break

    if mode == 1:
        while True:
            time.sleep(1)
            print("\ncomのターン！")
            wordlist = []
            for lw in list:
                list_word = "%s" % lw
                if list_word[0] == siri:
                    wordlist.append(list_word)
            time.sleep(1.2)

            if len(wordlist) == 0:
                time.sleep(2)
                print("...思いつかないや！" + name1 + "の勝ち！")
                name2make = 1
                break
            else:
                com_think = 0
                while True:
                    com_word = wordlist[random.randint(0,len(wordlist)-1)]
                    com_think += 1
                    if com_think == 5:
                        time.sleep(1)
                        print("うーん...。")
                    elif com_think == 500:
                        time.sleep(1)
                        print("...ちょっと待ってね。")
                    elif com_think == 5000:
                        time.sleep(3)
                        print("ああ！思いつかない！")
                        time.sleep(1)
                        print(name1 + "の勝ち！")
                        name2make = 1
                        break
                    
                    if com_word[-1] == "ン":
                        if nannido == "1":
                            break
                        else:
                            continue
                    elif com_word in used_word:
                        if nannido == "1":
                            break
                        else:
                            continue
                    else:
                        break
            if name2make == 1:
                break
            print("「" + jaconv.kata2hira(siri) + "」から始まる言葉：「" + jaconv.kata2hira(com_word) + "」")

            time.sleep(0.8)
            if com_word in used_word:
                print("あ、これはもう言ったね...！　" + name1 + "の勝ち！")
                name2make = 1
                break
            elif com_word[-1] == "ー":
                com_bou_word = com_word
                com_word = com_word[:-1]
                bou = 1
            else:
                bou = 0

            if com_word[-1] == "ン":
                print("あ、「ん」で終わっちゃった...。" + name1 + "の勝ち！")
                if bou == 1:
                    com_word = com_bou_word
                name2make = 1
                used_word.append(com_word)
                word_count += 1
                break

            if com_word[-1] == "ャ":
                com_word = com_word[:-1] + "ヤ"
                lil = 1
            elif com_word[-1] == "ュ": 
                com_word = com_word[:-1] + "ユ"
                lil = 1
            elif com_word[-1] == "ョ": 
                com_word = com_word[:-1] + "ヨ"
                lil = 1
            elif com_word[-1] == "ァ": 
                com_word = com_word[:-1] + "ア"
                lil = 1
            elif com_word[-1] == "ィ": 
                com_word = com_word[:-1] + "イ"
                lil = 1
            elif com_word[-1] == "ゥ": 
                com_word = com_word[:-1] + "ウ"
                lil = 1
            elif com_word[-1] == "ェ": 
                com_word = com_word[:-1] + "エ"
                lil = 1
            elif com_word[-1] == "ォ": 
                com_word = com_word[:-1] + "オ"
                lil = 1

            siri = com_word[-1]

            if lil == 1:
                if com_word[-1] == "ヤ":
                    com_word = com_word[:-1] + "ャ"
                elif com_word[-1] == "ユ": 
                    com_word = com_word[:-1] + "ュ"
                elif com_word[-1] == "ヨ": 
                    com_word = com_word[:-1] + "ョ"
                elif com_word[-1] == "ア": 
                    com_word = com_word[:-1] + "ァ"
                elif com_word[-1] == "イ": 
                    com_word = com_word[:-1] + "ィ"
                elif com_word[-1] == "ウ": 
                    com_word = com_word[:-1] + "ゥ"
                elif com_word[-1] == "エ": 
                    com_word = com_word[:-1] + "ェ"
                elif com_word[-1] == "オ": 
                    com_word = com_word[:-1] + "ォ"
                
                lil = 0

            if bou == 1:
                com_word = com_bou_word

            used_word.append(com_word)
            word_count += 1
            print()
            z = 0
            break

with open("used_word.txt", "a") as f:
    for i in used_word:
        f.write("%s\n" % i)


used_hirawords = []
for j in used_word:
    used_hiraword = jaconv.kata2hira(j)
    used_hirawords.append(used_hiraword)

print("\n単語数：" + str(word_count))
print("登場した単語:" + str(used_hirawords))