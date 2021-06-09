import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


#チェックボックス
cb = st.checkbox('Link Start')

if cb:    #もしチェックボックスにチェックが入っていたら
  img = Image.open('浮遊城.jpg')
  st.image(img, caption='アインクラッド',use_column_width=True)


#セレクトボックス
option = st.selectbox(
  'あなたが好きなアニメは？',
  ('銀魂', 'ソードアートオンライン', '物語シリーズ', '進撃の巨人')
)

st.write('あなたが好きなアニメは', option)

#ラジオボタン
rb = st.radio(
  "なんのアニメの主人公が好きなんだい",
  ('銀魂', 'ソードアートオンライン', '物語シリーズ', '進撃の巨人'))

if rb == '銀魂':
  st.write('坂田銀時')
elif rb == 'ソードアートオンライン':
  st.write('桐ヶ谷和人')
elif rb == '物語シリーズ':
  st.write('阿良々木暦')
else:
  st.write('エレン・イェーガー')


#テキストエリア
ti = st.text_input('あなたの趣味を教えてください')
st.write('私の趣味は' + ti)


#スライダー
score = st.slider('あなたの数学の点数は何点だい？',0,100,50)    #(コメント,最小,最大,初期値)
st.write('私の数学の点数は')
st.write(score)

#サイドバーへの表示
ti = st.sidebar.text_input('あなたのサイドバーの趣味を教えてください')
st.sidebar.write('私の趣味は' + ti)

#ツーカラムレイアウト
left_column, right_column = st.beta_columns(2)
button = left_column.button('クリックで右カラムに文字を表示')
if button:    #もしボタンが押されたら
  right_column.write('ボタンが押されたよ')

#エクスパンダー
expander1 = st.beta_expander('お問い合わせ1')
expander1.write('お問い合わせ内容1')
expander2 = st.beta_expander('お問い合わせ2')
expander2.write('お問い合わせ内容2')
expander2.write('お問い合わせ内容3')
expander2.write('お問い合わせ内容4')

#カラーピッカー
color = st.color_picker('色を選んでください', '#ff0000')
st.write('The current color is', color)


#文字出力内でhtmlを使用
st.write('<span style="color:red;background:pink">該当するデータがありません・・・・</span>',
              unsafe_allow_html=True)