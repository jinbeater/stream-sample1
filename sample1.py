import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')
st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40],
    '3列目':[300,5,100,6]
})
st.line_chart(df)
st.write(df)
st.dataframe(df)
st.dataframe(df, width=200, height=200)#writeじゃなくてdataframeを使用することでwidthやheightを指定することができる
st.dataframe(df.style.highlight_max(axis=1))#axisは列を指定するときに0、行を指定するときに1
st.table(df.style.highlight_max(axis=1))#静的な表を作りたいときに使用する

#マジックコマンド マークダウン記法で書くことができる
"""
#章
##説明
###項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
#```内のエリアを実際のコードとしてブラウザに表示できる

df2 = pd.DataFrame(
  np.random.rand(10,3),
  columns=['a','b','c']
)
st.dataframe(df2)
st.line_chart(df2)  #折れ線グラフ
st.area_chart(df2)  #折れ線グラフの下のエリアを塗った感じ
st.bar_chart(df2)   #棒グラフ


st.title('新宿付近のマップ')

df3 = pd.DataFrame(
  np.random.rand(100,2)/[50,50] + [35.69,139.70],  #乱数の数値を小さくするために50で割って新宿の緯度と経度を加算している
  columns=['lat','lon']  #緯度と経度
)
st.map(df3)

img = Image.open('浮遊城.jpg')
st.image(img, caption='アインクラッド',use_column_width=True)
