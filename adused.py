import sys
import re
add_word = []
count = 0
q = re.compile("[\u30A1-\u30FC]+")
more = "y"

with open("used_word.txt","r") as u:
    used = u.read().split("\n")
    if used == [""]:
        sys.exit("[used_word.txt]が空です。\nプログラムを終了します。")
    used.remove("シリトリ")
with open("list.txt","r") as l:
    read = l.read().split("\n")
    for word in used:
        if not word in read:
            while True:
                ad = input("「" + word + "」を追加しますか？(訂正して追加もy)　y or n：")
                if ad == "y" or ad == "ｙ":
                    co = input("訂正しますか？　y or n：")
                    if co == "y" or co == "ｙ":
                        word = input("読みを入力してください：")
                        continue
                    elif co == "n" or co == "ｎ":
                        if word in read:
                            print("「" + word + "」はすでに追加された単語です。")
                            continue
                        elif word in add_word:
                            print("「" + word + "」はすでに追加された単語です。")
                            continue
                        else:
                            if not q.fullmatch(word):
                                print("カタカナで入力してください。")
                                continue
                            with open ("list.txt", "a") as f:
                                f.write(word + "\n")
                            add_word.append(word)
                            count += 1 
                            break
                    else:
                        print("error")
                        continue
                elif ad == "n" or ad == "ｎ":
                    print("キャンセルしました。")
                    break
                else:
                    print("error")
                    continue
        else:
            if word != "":
                print("「" + word + "」はすでに追加された単語です。")

while more == "y" or more == "ｙ":
    more = input("他に追加する単語はありますか？ y or n : ")
    if more == "y" or more == "ｙ":
        more_word = input("追加する単語を入力してください：")
        with open("list.txt", "r") as f:
            read = f.read().split("\n")
            if more_word in read or more_word in add_word:
                print("すでに追加された単語です。")
            elif not q.fullmatch(more_word):
                print("カタカナで入力してください。")
            else:
                k = input("「" + more_word + "」を追加しますか？ y or n : ")
                if k == "y" or k == "ｙ":
                    with open("list.txt", "a") as f:
                        f.write(more_word + "\n")
                        add_word.append(more_word)
                        print("追加しました。")
                        count += 1
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

# with open("list.txt", "a") as f:
#     for i in add_word:
#         f.write("%s\n" % i)

a = input("\n[used_word.txt]の内容を消去しますか？　y or n：")
if a == "y" or a == "ｙ":
    open("used_word.txt", "w").close()
    print("消去しました。")
    
print("______")
if count > 1:
    print("added " + str(count) + " words:" + str(add_word))
elif count == 1:
    print("added " + str(count) + " word:" + str(add_word))
else:
    print("no added words.")