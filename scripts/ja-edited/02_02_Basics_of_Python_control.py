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

# + [markdown] colab_type="text" id="zTYLayT3qEzA"
# # 制御構文
#
# 複雑なプログラムを記述しようとすると、繰り返しの処理や、条件によって動作を変える処理が必要となります。
# これらは**制御構文**を用いて記述します。
#
# ここでは最も基本的な制御構文を 2 つ紹介します。
#
# - 繰り返し (`for`, `while`)
# - 条件分岐 (`if`)
#
# Python の制御構文は、**ヘッダ (header)** と **ブロック (block)** と呼ばれる 2 つの部分で構成されています。
# これらを合わせて **複合文 (compound statement)** と呼びます。
#
# ![ヘッダーとブロック](images/02/02_05.png)

# + [markdown] colab_type="text" id="ciZc5_PCv9dJ"
# 上図に示すように、制御構文ではヘッダ行に `for` 文や `if-else` 句を記述し、行末に `:` 記号を書きます。次に、ヘッダ行の条件で実行したい一連の処理文を、ブロックとしてその次の行以降に記述していきます。その際、 **インデント (indent)** と呼ばれる空白文字を先頭に挿入することで、ブロックを表現します。同じ数の空白でインデントされた文がブロックとみなされます。
# Python では、インデントとして**スペース 4 つ**を用いることが推奨されています。

# + [markdown] colab_type="text" id="oELnTpERNwCQ"
# ## 繰り返し （for 文）
#
# 同じ内容のメールを宛名だけ個別に変えて、1000 人に一斉送信したい場合など、繰り返す処理を記述する制御構文である `for` を使います。
#
# ![for文](images/02/02_06.png)

# + [markdown] colab_type="text" id="_-50XwKOv9dJ"
# `for` 文の文法は上図のとおりです。
#
# **イテラブルオブジェクト (iterable object)** とは、反復可能オブジェクトのことであり、要素を一度に 1 つずつ返せるオブジェクトのことを指します。
# `range()` という組み込み関数を使うと、引数に与えた整数の回数だけ順番に整数を返すイテラブルオブジェクトを作ることができます。
# `range(5)` と書くと、0, 1, 2, 3, 4 という整数 5 つを順番に返すイテラブルオブジェクトになります。
#
# 後述しますが、このイテラブルオブジェクトとして、リストやタプルも指定することができます。

# + colab={"base_uri": "https://localhost:8080/", "height": 106} colab_type="code" id="f7Y4APgkON_7" outputId="8d3fedd9-b0af-4cf4-ec66-bffb78ce9569"
# 5回繰り返す
for i in range(5):
    print(i)

# + [markdown] colab_type="text" id="oLpTgIv4OPnt"
# 上記の例では、イテラブルオブジェクトが1 つずつ返す値を変数 `i` で受け取っています。
# 最初は `i = 0` から始まっていることに注意してください。
# 最後の値も、`5` ではなく `4` となっています。
# このように、`range()` に 1 つの整数 `n` を与えた場合は、`0` から `n - 1` までの整数を順番に返します。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="SUTjSLuKv9dK" outputId="be21ab95-21c5-4a56-8e73-35f157f13954"
# 繰り返し処理が終わった後の値の確認
i

# + [markdown] colab_type="text" id="4sMmj2Ewv9dL"
# Jupyter Notebook では変数名をコードセルの最後の行に書いて実行するとその変数に代入されている値を確認できましたが、for 文の中のブロックでは明示的に `print()` を使う必要があります。
# `print()` を用いないと、以下のように何も表示されません。

# + colab={} colab_type="code" id="2SlR9vcGv9dL"
# 変数の値は表示されない
for i in range(5):
    i

# + [markdown] colab_type="text" id="tEczQdb9v9dM"
# for 文を使って、0 から始まって 1 ずつ大きくなっていく整数順に取得し、これをリストのインデックスに利用すれば、リストの各要素に順番にアクセスすることができます。

# + colab={"base_uri": "https://localhost:8080/", "height": 70} colab_type="code" id="b6XXuQ_gOnxk" outputId="ad85251e-4bcf-4b1f-c9d0-0aead91f025e"
names = ['佐藤', '鈴木', '高橋']

for i in range(3):
    print(names[i])

# + [markdown] colab_type="text" id="msGhS1ISv9dN"
# つぎに、さらに汎用性の高いプログラムを目指します。
#
# 上記のコードに関して、汎用性が低い点として、`range(3)` のように `3` という値を直接記述していることが挙げられます。
# この `3` はリストの要素の数を意味していますが、リストの要素の数が変わると、このプログラムも書き換える必要があり、手間がかかったり、ミスが発生する原因となったりします。
#
# リスト内の要素の数は、組み込み関数である `len()` を用いて取得できるため、これを使用した汎用性の高いプログラムに書き換えましょう。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="e4gbC4CIOzve" outputId="b5472139-d75b-46ac-de43-4ab365a4d14c"
len(names)

# + colab={"base_uri": "https://localhost:8080/", "height": 70} colab_type="code" id="4i21QYMwPB1C" outputId="0dffef88-45d8-4025-c5bd-75a333a70e0c"
for i in range(len(names)):
    print('{}さん'.format(names[i]))

# + [markdown] colab_type="text" id="9wx-qJovPEC0"
# これでリストの要素数に依存しないプログラムにすることができました。

# + [markdown] colab_type="text" id="KIO9gkUnv9dR"
# また、リスト自体をイテラブルオブジェクトとして指定することにより、リスト要素数の取得も `[]` でのインデックス番号の指定もせずに、より可読性の高いプログラムを書くことができます。

# + colab={"base_uri": "https://localhost:8080/", "height": 70} colab_type="code" id="EDqeGWucv9dR" outputId="261c1319-2e24-474f-f283-0d3352e24a27"
# リストをイテラブルオブジェクトに指定
for name in names:
    print('{}さん'.format(name))

# + [markdown] colab_type="text" id="iWEhrw_9v9dS"
# 最初のケースと比べていかがでしょうか。
# 動作は変わりませんが「名簿 (`names`) から名前 (`name`) を順に取り出している」ことが伝わりやすくなり、可読性が向上しています。
#
# 今回のイテラブルオブジェクトの `names` は単純な構造でしたが、辞書やリストなどが複雑に組み合わさっている場合は、
# このような工夫により可読性を意識することが重要です。

# + [markdown] colab_type="text" id="eeTHJ3hzPW7U"
# リストをイテラブルオブジェクトとして指定した場合、要素番号を取得できませんが、状況によっては要素番号を使用したいことがあります。
#
# そのような場合は、`enumerate()` という組み込み関数を使います。
# これにイテラブルオブジェクトを渡すと、`(要素番号, 要素)` というタプルを 1 つずつ返すイテラブルオブジェクトになります。

# + colab={"base_uri": "https://localhost:8080/", "height": 70} colab_type="code" id="8dT-qUhGv9dT" outputId="6cdbe801-9f59-49c4-96e6-6d3c54da2e04"
for i, name in enumerate(names):
    message = '{}番目: {}さん'.format(i, name)
    print(message)

# + [markdown] colab_type="text" id="wGwCa9wmP2r4"
# `enumerate()` と同様、`for` 文と合わせてよく使う組み込み関数に `zip()` があります。
#
# `zip()` は、複数のイテラブルオブジェクトを受け取り、その要素のペアを順番に返すイテラブルオブジェクトを作ります。
# このイテラブルオブジェクトは、渡されたイテラブルオブジェクトそれぞれの先頭の要素から順番に、タプルに束ねて返します。
# このイテラブルオブジェクトの長さは、渡されたイテラブルオブジェクトのうち最も短い長さと一致します。

# + colab={"base_uri": "https://localhost:8080/", "height": 53} colab_type="code" id="5w8huhHcQR8F" outputId="528f66f9-c589-481b-f82e-4bf4dfb9982d"
names = ['Python', 'Chainer']
versions = ['3.7', '5.3.0']
suffixes = ['!!', '!!', '?']

for name, version, suffix in zip(names, versions, suffixes):
    print('{} {} {}'.format(name, version, suffix))

# + [markdown] colab_type="text" id="IeQCA00UQYDq"
# `suffixes` の要素数は 3 ですが、より短いイテラブルオブジェクトと共に `zip` に渡されたため、先頭から 2 つ目までしか値が取り出されていません。

# + [markdown] colab_type="text" id="WguFiYgqQnQT"
# ## 条件分岐 （if 文）
#
# `if` は、指定した条件が `True` か `False` かによって、処理を変えるための制御構文です。
#
# ![if文](images/02/02_08.png)

# + [markdown] colab_type="text" id="J-Z8g-Klv9dV"
# `elif` と `else` は任意であり、`elif` は 1 つだけでなく複数連ねることができます。
#
# 例えば、0 より大きいことを条件とした処理を書いてみます。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="E-x_6gXwSsm7" outputId="86d289f1-92f1-4ada-ff3e-017e71f7c4b4"
# if の条件を満たす場合
a = 1

if a > 0:
    print('0より大きいです')
else:
    print('0以下です')

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="BmcHf-w5v9dV" outputId="134ddbe4-5605-4286-945e-a128ad6abc23"
# if の条件を満たさない場合
a = -1

if a > 0:
    print('0より大きいです')
else:
    print('0以下です')

# + [markdown] colab_type="text" id="u0F8tX6FStcQ"
# また、`if` に対する条件以外の条件分岐を追加する場合は、下記のように `elif` を使います。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="6li0UyjpStjg" outputId="8e0cecde-fce4-4db6-8d1c-0dbeb80e36b0"
a = 0

if a > 0:    
    print('0より大きいです')
elif a == 0:
    print('0です')
else:
    print('0より小さいです')

# + [markdown] colab_type="text" id="tZ15Hv9Gv9dY"
# ## 繰り返し （while 文）
#
# 繰り返し処理は、`for` 以外にも `while` を用いて記述することもできます。
# `while` 文では、以下のように**ループを継続する条件**を指定します。
# 指定された条件文が `True` である限り、ブロックの部分に記述された処理が繰り返し実行されます。
#
# ![while文](images/02/02_09.png)

# + [markdown] colab_type="text" id="Zjv8d3Rmv9dZ"
# `while` 文を使用した 3 回繰り返すプログラムは下記のとおりです。

# + colab={"base_uri": "https://localhost:8080/", "height": 70} colab_type="code" id="aFhfzaDFv9dZ" outputId="075646ab-8c87-41ea-fd6e-d7ee37334441"
count = 0

while count < 3:
    print(count)
    count += 1

# + [markdown] colab_type="text" id="1Q3QReThv9da"
# ここで使われている `count` という変数は、ループの中身が何回実行されたかを数えるために使われています。
# まず `0` で初期化し、ループ内の処理が一度行われるたびに `count` の値に 1 を足しています。
# この `count` を使った条件式を `while` 文に与えることで、ループを回したい回数を指定しています。
#
# 一方、`while True` と指定すると、`True` は変数ではなく値なので、変更されることはなく、ループは無限に回り続けます。
# `while` 文自体は無限ループの状態にしておき、ループの中で `if` 文を使って、ある条件が満たされた場合はループを中断する、という使い方ができます。
# これには `break` 文が用いられます。
#
# 以下は、`break` 文を使って上のコードと同様に 3 回ループを回すコードです。

# + colab={"base_uri": "https://localhost:8080/", "height": 70} colab_type="code" id="wj65vycFv9da" outputId="14670424-de4d-4493-bf64-2339416c69db"
count = 0

while True:
    print(count)
    count += 1
    
    if count == 3:
        break

# + [markdown] colab_type="text" id="AQFnBfgEv9da"
# `count` の値が 3 と等しいかどうかが毎回チェックされ、等しくなっていれば `break` 文が実行されて `while` ループが終了します。

# + [markdown] colab_type="text" id="2rtEn2APv9db"
# `while` 文を使って、指定された条件を満たして**いない**間ループを繰り返すという処理も書くことができます。`while` 文自体の使い方は同じですが、条件を反転して与えることで、与えた条件が `False` である間繰り返されるようにすることができます。
#
# これには、ブール値を反転する `not` を用います。
# `not True` は `False` を返し、`not False` は `True` を返します。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="0PucNNA0v9db" outputId="dc0151bc-a617-48c1-c63b-5826c8ed201c"
not True

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="9iX7JkEOv9db" outputId="3d72981a-bde9-46e1-de00-4fad8b237fda"
not False

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="TkSUZ1iZv9dc" outputId="5577f165-0fa0-4ffa-af45-ac847a311049"
not 1 == 2

# + [markdown] colab_type="text" id="0aM2yZ7qv9dd"
# このように、`not` はあとに続くブール値を反転します。
# これを用いて、`count` が 3 **ではない**限りループを繰り返すというコードを `while` 文を使って書いてみましょう。

# + colab={"base_uri": "https://localhost:8080/", "height": 70} colab_type="code" id="vhvBNYCXv9dd" outputId="c7651cd7-4f86-47ad-b8a6-c505dd996de5"
count = 0

while not count == 3:
    print(count)
    count += 1
