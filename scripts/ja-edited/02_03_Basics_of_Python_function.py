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

# + [markdown] colab_type="text" id="e96zsBv7IfDn"
# ## 関数
#
# 何かひとまとまりの処理を書いた際には、その処理のためのコードをまとめて、プログラム全体の色々な箇所から再利用できるようにしておくと、便利な場合があります。
# ここでは、処理をひとまとめにする方法の一つとして**関数 (function)** を定義する方法を紹介します。

# + [markdown] colab_type="text" id="RCB98_8xv9df"
# ### 関数を定義する
#
# ![関数の定義](images/02/02_10.png)
#
# 例えば、**受け取った値を 2 倍して表示する関数**を作ってみましょう。
#
# 関数を定義するには、まず名前を決める必要があります。
# 今回は `double()` という名前の関数を定義してみます。
#
# 関数も制御構文と同じく**ヘッダー**と**ブロック**を持っています。

# + colab={} colab_type="code" id="iDh3Mpi_IfDp"
# 関数 double() の定義
def double(x):
    print(2 * x)


# + [markdown] colab_type="text" id="yG-qN405v9dg"
# **関数は定義されただけでは実行されません。**
# 定義した関数を使用するためには、定義を行うコードとは別に、実行を行うコードが必要です。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="6QUecRiUv9dg" outputId="7241aa8c-2a9c-4c95-8d63-ebe27a2a6fd8"
# 関数の実行
double(3)

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="dR7DqN2fv9dh" outputId="89bb6598-567d-4247-8e0e-2d15072322df"
double(5)

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="wjStuxcBv9di" outputId="138a4607-ebf9-48f3-e4f5-96863b9eec0f"
double(1.5)


# + [markdown] colab_type="text" id="CRggp-QcIfDs"
# `double(x)` における `x` のように、関数に渡される変数や値のことを**引数 (argument)** といいます。
# 上の例は、名前が `double` で、1つの引数 `x` をとり、`2 * x` という計算を行い、その結果を表示しています。

# + [markdown] colab_type="text" id="VDqeEdX5v9dj"
# ### 複数の引数をとる関数
#
# 複数の引数をとる関数を定義する場合は、関数名に続く `()` の中に、カンマ `,` 区切りで引数名を並べます。
#
# 例えば、引数を 2 つとり、足し算を行う関数 `add()` を作ってみましょう。

# + colab={} colab_type="code" id="ARE2LU8Qv9dl"
# 関数の定義
def add(a, b):
    print(a + b)


# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="Zte-_M1-v9dl" outputId="cf78e6e7-522c-4551-b876-8f7f4f582d92"
# 関数の実行
add(1, 2)

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="7HUAVoGhv9dm" outputId="8e0d0ec9-9774-42b6-ef79-52b20cf88b8a"
add(3, 2.5)

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="IjMBFjvmv9dm" outputId="75da673b-d203-460c-f054-205cbe9ace97"
add(1, -5)


# + [markdown] colab_type="text" id="mwZ-T1CTv9dn"
# 今回の `double()` や `add()` は定義を行い自作した関数ですが、Python には予め多くの関数が定義されています。
# そのような関数を**組み込み関数 (built-in function)** と呼びます。
# すでに使用している `print()` や `len()`, `range()` などが、これに該当します。
# 組み込み関数の一覧は[こちら](https://docs.python.org/ja/3/library/functions.html)で確認することができます。
#

# + [markdown] colab_type="text" id="A8XpuE_av9dn"
# ### 引数をとらない関数
#
# 引数をとらない関数を定義する場合でも、関数名の後に `()` を加える必要があります。
#
# 例えば、実行するとメッセージを表示する関数を定義して、実行してみましょう。

# + colab={} colab_type="code" id="z2Xej00Bv9dn"
# 引数のない関数の定義
def hello():
    print('Chainerチュートリアルにようこそ')


# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="peShhHg2v9dn" outputId="b437e0f9-1c01-4d93-a13c-2d50cf8202f9"
# 引数のない関数の実行
hello()


# + [markdown] colab_type="text" id="BZGSKTbcv9do"
# ### 引数のデフォルト値
#
# 引数には、あらかじめ値を与えておくことができます。
# これは、引数をとる関数を定義する際に、何も引数に値が渡されなかったときにどのような値がその引数に渡されたことにするかをあらかじめ決めておける機能で、その値のことを**デフォルト値**と呼びます。
#
# 例えば、上の `hello()` という関数に、`message` という引数をもたせ、そこにデフォルト値を設定しておきます。

# + colab={} colab_type="code" id="uw2d8qDov9do"
def hello(message='Chainerチュートリアルにようこそ'):
    print(message)


# + [markdown] colab_type="text" id="7i8TQcfzv9do"
# この関数は引数に何も与えずに呼び出すと、「Chainerチュートリアルにようこそ」というメッセージを表示し、引数に別な値が渡されると、その値を表示します。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="Fh4VEHmMv9dp" outputId="d284fd9b-4a96-4039-f585-a01804e360e9"
hello()

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="p2g-ULOWv9dp" outputId="9dd78b5c-4185-4f40-a40f-9d1bdfe3309a"
hello('Welcome to Chainer tutorial')


# + [markdown] colab_type="text" id="GWhAbt3ov9dq"
# デフォルト値が与えられていない引数は、関数呼び出しの際に必ず何らかの値が渡される必要がありますが、デフォルト値を持つ場合は、何も指定しなくても関数を呼び出すことができるようになります。

# + [markdown] colab_type="text" id="DpwRYy4ov9dq"
# ### 返り値のある関数
#
# 上で定義した足し算を行う関数 `add()` では、計算結果を表示するだけで、計算結果を呼び出し元に戻していませんでした。
# そのため、このままでは計算結果を関数の外から利用することができません。
#
# そこで、`add()` 関数の末尾に `return` 文を追加して、計算結果を呼び出し元に返すように変更してみましょう。

# + colab={} colab_type="code" id="ZCtzpxG1v9dq"
# 返り値のある関数の定義
def add(a, b):
    return a + b


# + [markdown] colab_type="text" id="M9c1_e-sv9dr"
# このように、呼び出し元に返したい値を `return` に続いて書くと、その値が `add()` 関数を呼び出したところへ戻されます。
# `return` で返される値のことを**返り値 (return value)** と言います。
#
# 以下に、計算結果を `result` という変数に格納し、表示する例を示します。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="RPJnjuL5v9dr" outputId="48546d3e-a444-4109-ddf0-7df7b14b9236"
result = add(1, 3)

result

# + [markdown] colab_type="text" id="tagr61vUv9ds"
# 計算結果が `result` に格納されているので、この結果を用いてさらに別の処理を行うことができます。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="Qe8Enb6Ev9ds" outputId="99526b92-37c3-4832-caef-f17aa45701d9"
result = add(1, 3)

result_doubled = result * 2

result_doubled

# + [markdown] colab_type="text" id="fP4OdcI-v9ds"
# また、返り値は「呼び出し元」に返されると書きました。
# この「呼び出し元」というのは、関数を呼び出す部分のことで、上のコードは `add(1, 3)` の部分が `4` という結果の値になり、それが左辺の `result` に代入されています。
#
# これを用いると、例えば「2 と 3 を足した結果と、1 と 3 を足した結果を、掛け合わせる」という計算が、以下のように書けます。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="gs0hBjg6v9ds" outputId="4c76fe15-686d-4aed-f87c-ec55d177728c"
add(2, 3) * add(1, 3)

# + [markdown] colab_type="text" id="BJnkcc_Qv9dt"
# ### 変数のスコープ
#
# 関数の中で定義した変数は基本的には関数の外では利用できません。
# 例えば、以下の例を見てみましょう。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="L8vtxEV7v9dt" outputId="509fbb4d-0b47-4f37-d38c-51018e6f19b2"
a = 1

# 関数の内部で a に 2 を代入
def change():
    a = 2
    
change()

a

# + [markdown] colab_type="text" id="Z9slKEKXv9du"
# 関数の外で `a = 1` と初期化した変数と同じ名前の変数に対して、`change()` 関数の内部で `a = 2` という代入を行っているにもかかわらず、`change()` 関数の実行後にも関数の外側では `a` の値は 1 のままになっています。
# **関数の外側で定義された変数** `a` **に、関数内部での処理が影響していないことがわかります。**
#
# なぜこうなるかというと、関数の中で変数に値が代入されるとき、その変数はその関数の**スコープ (scope)** でだけ有効な**ローカル変数**になり、関数の外にある同じ名前の変数とは別のものを指すようになるためです。
# スコープとは、その変数が参照可能な範囲のことです。
# 上の例では、`a = 2` の代入を行った時点で`change()` 関数のスコープに `a` という変数が作られ、`change()` 関数の中からは `a` といえばこれを指すようになります。関数から抜けると、`a` は 1 を値に持つ外側の変数を指すようになります。
#
# ただし、代入を行わずに、参照するだけであれば、関数の内側から外側で定義された変数を利用することができます。

# + colab={"base_uri": "https://localhost:8080/", "height": 53} colab_type="code" id="XgGcEUSQv9du" outputId="0871b4ef-d71a-4f3f-c556-fc6429e0ee94"
a = 1

def change():
    print('From inside:', a)
    
change()

print('From outside:', a)

# + [markdown] colab_type="text" id="vAHe5xDGv9dv"
# この場合は、`change()` 関数のスコープには `a` という変数は作られないので、関数の中で `a` といえば外側で定義された変数を指します。
#
# 関数の外で定義された変数は**グローバル変数**と呼ばれます。
# グローバル変数は、特に特別な記述を要せず参照することはできますが、関数の中で**代入**を行う場合は `global` 文を使用する必要があります。
# ただ、スコープ外の変数（グローバル変数）を変更することは推奨されないためチュートリアルでは省略します。
#
