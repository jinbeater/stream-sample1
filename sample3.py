import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 超入門')
st.write('プレグレスバーの表示')
#プレグレスバー
latest_iteration = st.empty()   #空要素を変数に入れる
bar = st.progress(0)            #実際のバーの表示のメソッド

for i in range(100):
  latest_iteration.text(f'iteration{i+1}')
  bar.progress(i+1)
  time.sleep(0.1)             #バーの進んでいく速度

st.write('読み込み完了!')       #プレグレスバーのfor文が終了してから下の処理にくる
