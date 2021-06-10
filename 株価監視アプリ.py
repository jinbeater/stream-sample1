import streamlit as st
import pandas as pd
import yfinance as yf
import altair as alt

st.title('株価可視化アプリ')

st.sidebar.write("""
# GAFA株価
こちらは株価監視ツールです。以下のオプションから表示日数を変更できます。
""")
st.sidebar.write("""
## 表示日数選択
""")

days = st.sidebar.slider('日数を指定してください',1,50,20) 

st.write(f"""
### 過去 **{days}日間** のGAFAの株価
""")

@st.cache                       #毎回データを読み取るのではなく、キャッシュから読み取るので高速に！
def get_data(days, tichers):
  df = pd.DataFrame()         #空のデータフレームを作成。ここにfor文で追加していく
  for company in tickers.keys():
    tkr = yf.Ticker(tickers[company])    #Appleの株価取得
    hist = tkr.history(period=f'{days}d')     #20日間の株価
    hist.index = hist.index.strftime('%d %b %Y')    #インデックスに指定したフォーマットを代入
    hist = hist[['Close']]       #変数histの中に'close'という列だけを代入
    hist.columns = [company]      #Closeというからむ名をAppleに置き換えている
    hist = hist.T                  #行と列を入れ替えている
    hist.index.name = 'Name'
    hist.columns.name = 'Date'
    df = pd.concat([df,hist])

  return df

try:
  st.sidebar.write("""
  ## 株価の範囲指定
  """)

  ymin,ymax = st.sidebar.slider(        #低い方と高い方の値がそれぞれ代入される
    '範囲を指定してください',
    0.0,3500.0,(0.0, 3500.0)
  )

  tickers = {             #辞書型の変数(map)みたいなkeyと値のセット
    'Apple':'AAPL',         #会社名:ティッカーシンボル
    'Facebook':'FB',
    'Google':'GOOGL',
    'Microsoft':'MSFT',
    'Netflix':'NFLX',
    'Amazon':'AMZN',
    'SPDR Portfolio S&P':'SPYD',
    'iShares Core':'HDV'
  }

  df = get_data(days,tickers)

  companies = st.multiselect(
    '会社名を選択してください',
    list(df.index),
    ['Google','Amazon','Facebook','Apple']      #初期値
  )

  if not companies:
    st.error('少なくとも1社は選んでください')
  else:
    data = df.loc[companies]        #ユーザが選んだ会社の情報を取得。.locはpandasのdataframeのメソッド。取得する列を指定。
    st.write('### 株価(USD)',data.sort_index())

    data = data.T.reset_index()
    data = pd.melt(data, id_vars=['Date']).rename(
      columns={'value':'Stock Prices'}
    )

    chart = (
      alt.Chart(data)
      .mark_line(opacity=0.8, clip=True)
      .encode(
      x = "Date:T",
      y = alt.Y("Stock Prices:Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
      color='Name:N'
      )
    )
    st.altair_chart(chart, use_container_width=True)    #use_container_widthはコンテンツが枠に収まるように設定
except:
  st.write('おっとー！？何やらエラーが出たようですよ〜？？')