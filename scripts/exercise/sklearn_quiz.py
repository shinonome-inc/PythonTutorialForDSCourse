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
#     name: python3
# ---

# + [markdown] id="Wqlw5ktcykfi"
# # 【確認課題】scikit-learn

# + [markdown] id="dp2rHHDHzZd0"
# ## 前準備
#
#
#

# + [markdown] id="2j_gL_RC1_8_"
# ### データの読み取り
#
# scikit-learnから提供される`iris`というデータセットを読み込みます。

# + id="YKJY4Q9R0aB7"
from sklearn.datasets import load_iris
import pandas as pd


iris = load_iris()

# 説明変数の読み取り
data = iris.data
feature_names = iris.feature_names
df_data = pd.DataFrame(data=data, columns=feature_names)

# 目的変数の読み取り
target = iris.target
target_names = iris.target_names
df_target = pd.DataFrame(data=target, columns=["target"])


# + [markdown] id="hfBraFA414qg"
# ### 説明変数の把握
#
# 問. `df_data` の先頭 5 行を表示しましょう。
#

# + colab={"base_uri": "https://localhost:8080/", "height": 206} id="T7StoNXU2iXm" outputId="0fedad15-b679-44d2-b9c7-d3bf12198c40"

# -

# 問. `df_data` の行数と列数を表示しましょう。

# + colab={"base_uri": "https://localhost:8080/"} id="Zdx6hnA026SC" outputId="bfd5bff8-4a4d-4a8d-f8a4-a5dae9e2e82f"


# + [markdown] id="lJ-3Jg-k6QSx"
# 問. `df_data` の基本特徴量を表示しましょう。
#

# + colab={"base_uri": "https://localhost:8080/", "height": 300} id="mDKbvknP6arO" outputId="9b0dc5de-a88d-49e4-b2ba-b325ef698519"

# -

# 問. `df_data` に欠損値がないかを確認しましょう。

# + colab={"base_uri": "https://localhost:8080/"} id="DqRq3xhB61Sx" outputId="21e8de9b-478b-4a88-c17e-b2d335c98fc6"


# + [markdown] id="R3ZD__9G7FeJ"
# ### 目的変数の把握
#
# 問. `df_target` のうち、ランダムに 10 行表示しましょう。
#
# -



# 目的変数の数字はそれぞれ、
#
# - 0 が `setosa`（ヒオウギアヤメ）
# - 1 が `versicolor`（ブルーフラッグ）
# - 2 が `virginica`（バージニカ）
#
# を指しています。
#

# + [markdown] id="XPik8k4I2_Zz"
# ### データの可視化（Extra）
#
# 問. x 軸を petal length (cm)、y 軸を petal width (cm)にして散布図を作成しましょう。
# ただし、目的変数に応じて点の色と形を変更してください。
#
# -





# + [markdown] id="sjDOl12S86VJ"
# ## 機械学習
#

# + [markdown] id="OZYFySxQ9BrG"
# ### データの分割
#
# 問. iris データを 4:1 に分割して、80% を学習データとして 20% をテストデータとしてください。
#
# ただし、分割した後の変数名は以下の通りにしてください。
#
# | 変数名  |      内容      |
# | :-----: | :------------: |
# | x_train | 学習用の説明変数 |
# | x_test | テスト用の説明変数 |
# | y_train | 学習用の目的変数 |
# | y_test | テスト用の目的変数 |
#
# 学習データでモデルの学習を行い、テストデータでモデルの評価を行います。
#

# + id="KZfVWvll9T-X"


# + [markdown] id="Ce6m5w8K-Zui"
# 問. 本当に 4:1 に分割できているか確認しましょう。
#

# + colab={"base_uri": "https://localhost:8080/"} id="X4dBgVxV-dz9" outputId="c74c6df3-1d92-4ef8-b7ca-53e779e61ad5"


# + [markdown] id="psKYYN9_-jTI"
# ### 学習
#
# 問. RandamForest の学習モデルのインスタンスを生成しましょう。
#

# + id="tQGdKQsh_HHe"


# + [markdown] id="OseolTqIGfsc"
# 問. `x_train` と `y_train` を用いて、モデルを学習させましょう。
#

# + colab={"base_uri": "https://localhost:8080/", "height": 130} id="x7ePCmqnJ6Ic" outputId="cfad6048-c06f-40f2-846c-cafc73b7168c"


# + [markdown] id="5cKU0YfKIUTQ"
# ### 推論
#

# + [markdown] id="iHjsUA3K3MeI"
# 問. 学習したモデルに `x_test` を入力して予測をしましょう。

# + id="RUgEb9q-Idbb"


# + [markdown] id="c1ZE3GGx3Tal"
# 問. 予測結果と `y_test` に対して、`accuracy` を計算することでモデルを評価しましょう。
#

# + colab={"base_uri": "https://localhost:8080/"} id="TTI2DqDlIjhP" outputId="9b0c755f-652e-4017-fd29-382369aec2b3"

# -

# 実は、iris データセットはかなり簡単な分布をしているので、正解率はほぼ 100% になったと思います。
