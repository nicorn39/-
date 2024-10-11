import streamlit as st
import random

#ちいかわのうさぎ言語に変換する関数
def convert_to_usagi(text):
    #単語を置き換えるルールを設定
    replacements = {
        "こんにちは": "ヤハ！",
        "ありがとう": "ウ ウ・ラ・ラ ウラ♬ ウララ ヤ～ハ ヤ～ハ…プルヤッ…",
        "すごい": "ヴゥルルルルルル",
        "楽しい": "キャハッ キャハハハッ キャ～ァ キャハッ",
        "疲れた": "ツツウラウラ",
        "おいしい": "シャク！！シャークシャク！"
    }

    #エフェクトの追加（感情を強調するため）
    exclamations = ["ィィィィィィ ヤァァァァ ァアッハ！！！", "ゥララララァアーッ…スクッ", "イヤァーーッハ", "ウ・ラ・ヤ・ハ ヤハウ・ラ", "ゥルルルルルル", "トウッ ィヤハッ！"]

    #テキストを単語ごとに変換
    converted_text = text
    for word, replacement in replacements.items():
        converted_text = converted_text.replace(word, replacement)

    #変換後のテキストにランダムでうさぎらしい表現を追加
    converted_text += " " + random.choice(exclamations)

    return converted_text

#Streamlitアプリの作成
st.title("うさぎ語変換アプリ🐰")
st.write("テキストを入力すると、うさぎの言葉に変換します！")

#ユーザーのテキスト入力を受け付ける
user_input = st.text_area("変換したいテキストを入力してください：")

#変換ボタン
if st.button("うさぎ語に変換"):
    if user_input:
        usagi_text = convert_to_usagi(user_input)
        st.subheader("結果")
        st.write(usagi_text)
    else:
        st.write("テキストを入力してください！")
