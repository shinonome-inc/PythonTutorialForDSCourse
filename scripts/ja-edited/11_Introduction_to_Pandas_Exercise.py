# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] colab_type="text" id="XfmMtuxKYRoO"
# # Pandas確認課題
#
# このPandas確認課題は、データサイエンス100本ノックの問題で最低限必要な問題を抜粋したものですが、[Introduction_to_Pandas](./11_Introduction_to_Pandas.ipynb) に掲載されていない機能が必要な問題もあります。
# 初めて触るライブラリを調べながら使うというのはよくある光景です。この課題では皆さんにもそれに挑戦していただきます。  
# ヒントとして検索キーワードなどを載せておくので、自力で調べながら解いてみましょう。  
#
#

# + [markdown] colab_type="text" id="9ktBdoeha1jL"
# ## 必要モジュールのインポート
#
# この問題で使うモジュールをインポートします．

# + colab={} colab_type="code" id="2IhABxEEaq19"
import pandas as pd
import numpy as np

# + [markdown] colab_type="text" id="llLJCZTEa5Rb"
# ## データの読み込み

# + colab={} colab_type="code" id="uN-SvpE_a50E"
df_customer = pd.read_csv('https://raw.githubusercontent.com/The-Japan-DataScientist-Society/100knocks-preprocess/master/docker/work/data/customer.csv')
df_product = pd.read_csv('https://raw.githubusercontent.com/The-Japan-DataScientist-Society/100knocks-preprocess/master/docker/work/data/product.csv')
df_receipt = pd.read_csv('https://raw.githubusercontent.com/The-Japan-DataScientist-Society/100knocks-preprocess/master/docker/work/data/receipt.csv')

# + [markdown] colab_type="text" id="xm5FMZJobU3Y"
# ---
# ## 問1. 条件抽出
# > P-006: レシート明細データフレーム「df_receipt」から売上日（sales_ymd）、顧客ID（customer_id）、商品コード（product_cd）、売上数量（quantity）、売上金額（amount）の順に列を指定し、以下の条件を満たすデータを抽出せよ。
# > - 顧客ID（customer_id）が"CS018205000001"
# > - 売上金額（amount）が1,000以上または売上数量（quantity）が5以上

# + colab={"base_uri": "https://localhost:8080/", "height": 198} colab_type="code" id="KSOu6AWabVaD" outputId="91faaad5-57ca-4a67-c046-195afa4d21df"


# + [markdown] colab_type="text" id="7WsKq3Voj0LF"
# ---
# ## 問2. ソート
# > P-18: 顧客データフレーム（df_customer）を生年月日（birth_day）で若い順にソートし、先頭5件を全項目表示せよ。

# + colab={"base_uri": "https://localhost:8080/", "height": 694} colab_type="code" id="uLdYmXgdjxaw" outputId="7a064e8c-4db3-4350-a212-688cb9b49980"


# + [markdown] colab_type="text" id="1lRGtDSphhyQ"
# ---
# ## 問3. 全件数
# > P-021: レシート明細データフレーム（df_receipt）に対し、件数をカウントせよ。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="m-ihL_fVhhyQ" outputId="da0669b7-2c34-4dc6-becb-4da002103202"


# + [markdown] colab_type="text" id="MkjDW-oyhhyS"
# ## 問4. ユニーク件数
# > P-022: レシート明細データフレーム（df_receipt）の顧客ID（customer_id）に対し、ユニーク件数をカウントせよ。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="0xSI9r8UhhyS" outputId="0c5a57f4-2088-4109-a40e-eb76c4845af0"

# -

# <details>
# <summary>ヒント</summary>
# 「ユニーク」というのはそのまま検索に使える単語です。  
# </details>

# + [markdown] colab_type="text" id="h9E9b_yUhhyq"
# ---
# ## 問5. 〇〇ごとに集計
# > P-035: レシート明細データフレーム（df_receipt）に対し、顧客ID（customer_id）ごとに売上金額（amount）を合計して全顧客の平均を求め、平均以上に買い物をしている顧客を抽出せよ。ただし、顧客IDが"Z"から始まるのものは非会員を表すため、除外して計算すること。なお、データは先頭5件だけ表示せよ。
#
# 会員のみを抽出する方法は、例えば以下の2通りの方法があります。
# -

df_receipt_only_member = df_receipt[~df_receipt["customer_id"].str.startswith("Z")]
df_receipt_only_member = df_receipt.query("not customer_id.str.startswith('Z')", engine="python")

# + colab={"base_uri": "https://localhost:8080/", "height": 225} colab_type="code" id="7lYKkmsohhyq" outputId="06bbc1ea-d6d0-4841-a6dd-1598974714b6"

# -

# <details>
# <summary>ヒント1</summary>
# 「pandas 要素ごと 集計」 などで今回使える機能に関する記事が見つかります。
# </details>

# <details>
# <summary>ヒント2</summary>
# メソッド名は "groupby" です。
# </details>

# + [markdown] colab_type="text" id="iNO7ESvWhhyw"
# ---
# ## 問6. DataFrameの結合
# > P-038: 顧客データフレーム（df_customer）とレシート明細データフレーム（df_receipt）から、各顧客ごとの売上金額合計を求めよ。ただし、買い物の実績がない顧客については売上金額を0として表示させること。また、顧客は性別コード（gender_cd）が女性（1）であるものを対象とし、非会員（顧客IDが'Z'から始まるもの）は除外すること。なお、結果は先頭5件だけ表示せよ。
# -

df_customer_only_member = df_customer[~df_customer["customer_id"].str.startswith("Z")]
df_customer_only_member = df_customer.query("not customer_id.str.startswith('Z')", engine="python")

# + colab={"base_uri": "https://localhost:8080/", "height": 728} colab_type="code" id="hmc6LUaEhhyw" outputId="f1b1dc56-af65-4fbf-9d8a-5c0490a2ad17"

# -

# <details>
# <summary>ヒント1</summary>
# タイトル通り 「pandas DataFrame 結合」などと調べれば必要な機能に関する記事が見つかります。  
# </details>
#

# <details>
# <summary>ヒント2</summary>
# "merge", "join"という似たメソッドがあります。  
# 今回の場合"merge"が便利でしょう。
# </details>

# + [markdown] colab_type="text" id="umDmd8kohhzA"
# ---
# ## 問7. 時系列データ
# > P-046: 顧客データフレーム（df_customer）の申し込み日（application_date）はYYYYMMD形式の文字列型でデータを保有している。これを日付型（dateやdatetime）に変換し、顧客ID（customer_id）とともに抽出せよ。なお、データは先頭5件を表示せよ。

# + colab={"base_uri": "https://localhost:8080/", "height": 348} colab_type="code" id="pVAxV-TWhhzA" outputId="2d2e2281-7181-41b4-81e4-a9e834b93927"

# -

# <details>
# <summary>ヒント1</summary>
# 「pandas datetime」などで該当の機能が見つかるかと思います。
# </details>
#

# <details>
# <summary>ヒント2</summary>
# "pd.to_datetime"というメソッドが使えるでしょう。このメソッドを適用する際ですが、for文を使わずに実装しましょう。

# + [markdown] colab_type="text" id="9v_q6BLjhhzU"
# ---
# ## 問8. 関数
# > P-061: レシート明細データフレーム（df_receipt）の売上金額（amount）を顧客ID（customer_id）ごとに合計し、合計した売上金額を常用対数化（底=10）して顧客ID、売上金額合計とともに表示せよ。ただし、顧客IDが"Z"から始まるのものは非会員を表すため、除外して計算すること。なお、結果は先頭5件を表示せよ。

# + colab={"base_uri": "https://localhost:8080/", "height": 437} colab_type="code" id="d5_2HQ-2hhzU" outputId="56ba3b92-2071-4a8d-c555-d9007bb43316"


# + [markdown] colab_type="text" id="boe923CMhhzq"
# ---
# ## 問9. 欠損数
# > P-079: 商品データフレーム（df_product）の各項目に対し、欠損数を確認せよ。

# + colab={"base_uri": "https://localhost:8080/", "height": 169} colab_type="code" id="bxl__vC5hhzq" outputId="d8bb408a-6897-4e5a-8416-ce67a8a5fce4"


# + [markdown] colab_type="text" id="afprSqIvhhzs"
# ---
# ## 問10. 欠損値の除去
# > P-080: 商品データフレーム（df_product）のいずれかの項目に欠損が発生しているレコードを全て削除した新たなdf_product_1を作成せよ。なお、削除前後の件数を表示させ、前設問で確認した件数だけ減少していることも確認すること。

# + colab={} colab_type="code" id="q3_9sLdHhhzt"


# + colab={} colab_type="code" id="qFNnYstw1vTG"
len(df_product), len(df_product_1)

# + [markdown] colab_type="text" id="GtiO20ZKhhzu"
# ---
# ## 問11. 欠損値の穴埋め
# > P-081: 単価（unit_price）と原価（unit_cost）の欠損値について、それぞれの平均値で補完した新たなdf_product_2を作成せよ。なお、平均値について1円未満は四捨五入とせよ。補完実施後、各項目について欠損が生じていないことも確認すること。

# + colab={} colab_type="code" id="puFf-7Ewhhzu"

# -

# ### 余談
# ChatGPTやBing AIに聞けば大抵のことは教えてくれます。  
# 何回か入力文章を吟味しないといけないこともありますが、知らないことを調べる場合は自分で検索するよりも早いです。  
# ただ、ChatGPTなどは嘘をつく場合があるので、自分でソースを参照する姿勢は必要です。  
#
# これはBingAIの回答例です。  
# ![BingAIの回答例](./images/11/BingAI.png)
