# しりとりプログラム
コンピュータとしりとりができる対話型プログラム

## 特徴
- **形態素解析**を活用し、与えられたインターネット記事などの文章から名詞のみを抽出し学習
- **マルチスレッド**を活用した、時間制限縛りモード

---
## word_chain_v3.py
しりとりを行うmainプログラム  
2人対戦及びコンピュータ対戦が可能

### 使い方
1. word_chain_v3.pyを実行する
2. 表示される指示に従いターミナルに文字を入力する


## adlist.py
与えられた文章から名詞を抽出し、学習させるためのプログラム

### 使い方
1. adlist.pyを実行する
2. 学習元となる文章を入力する
3. 表示される指示に従いターミナルに文字を入力する


## adused.py
過去のしりとりで登場した名詞を学習させるためのプログラム

### 使い方
1. adused.pyを実行する
2. 表示される指示に従いターミナルに文字を入力する
