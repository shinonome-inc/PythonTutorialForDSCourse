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

# + [markdown] colab_type="text" id="D3QflLv0qdiy"
# # Python 入門
#
# 本章では、プログラミング言語 Python の基礎的な文法を学んでいきます。
# 次章以降に登場するコードを理解するにあたって必要となる最低限の知識について、最短で習得するのが目標です。
# より正確かつ詳細な知識を確認したい場合には、[公式のチュートリアル](https://docs.python.jp/3/tutorial/index.html)などを参照してください。
#
# Pythonにはバージョンとして 2 系と 3 系の 2 つの系統があり、互換性のない部分もあります。
# 本チュートリアルでは、3 系である **Python 3.6** 以上を前提とした解説を行っています。
#
# ## Python の特徴
#
# プログラミング言語には、Python 以外にも C 言語や Java、Ruby、R のように様々なものがあります。それぞれの言語がすべての用途に適しているわけではなく、しばしば用途によって得手不得手があります。
#
# 本チュートリアルでは基本的に Python というプログラミング言語を扱います。
# その理由は、Python はデータ解析・機械学習のためのライブラリが充実しており、データ解析や機械学習の分野で最もよく使われている言語だからです。
# また、Web アプリケーションフレームワークの開発も活発で、データ解析だけでなく Web サービス開発まで同じ言語で統一して行える点も魅力です。
#

# + [markdown] colab_type="text" id="unYvpNZCv9aF"
# さらには、初学者にとっても学びやすい言語です。
# 初学者がプログラミングを学び始めるときにつまづきがちな難しい概念が他の言語と比べ多くなく、入門しやすい言語といえます。
#
# まとめると、Python には
#
# - データ解析や機械学習によく使われている
# - Web アプリケーションの開発などでもよく使われている
# - 初学者がはじめやすい言語
#
# のような魅力があります。

# + [markdown] colab_type="text" id="jZNTuBQ54BSu"
# ### 文法とアルゴリズム
#
# プログラミングによってある特定の処理をコンピュータで自動化したい場合、**文法**と**アルゴリズム**の 2 つを理解しておく必要があります。
#
# プログラムでは、まずはじめにコンピュータに命令を伝えるためのルールとなる**文法**を覚える必要があります。
# 文法を無視した記述があるプログラムは、実行した際にエラーとなり処理が停止します。そのため、文法はしっかりと理解しておく必要があります。
#
# ただし、文法さえ理解していれば十分かというとそうではありません。一般的に、初学者向けのプログラミングの参考書では、この文法だけを取り扱うことも多いのですが、コンピュータに処理を自動化させることが目的であれば、文法だけでなく**アルゴリズム**も理解する必要があります。アルゴリズムとは、どういう順番でどのような処理をしていくかの一連の手順をまとめたものです。
#
# この章では、Python の文法について紹介し、機械学習やディープラーニングで必要となるアルゴリズムについてはこれ以降の章で紹介します。
#
# ここでは以下 4 つの文法に主眼を置きながら説明していきます。
#
# - 変数
# - 制御構文
# - 関数
# - クラス

# + [markdown] colab_type="text" id="hO4YLiKjIfDi"
# ## 変数
#
# **変数 (variable)** とは、様々な値を格納することができる、**名前がついた入れ物**です。
# この変数に値を格納したり、更新したりすることで、計算結果を一時的に保持しておくことができます。
#
# ### 代入と値の確認
#
# それでは、`a` という名前の変数に、`1` を**代入**してみましょう。

# + colab={} colab_type="code" id="SjpDQJn-3Rct"
a = 1

# + [markdown] colab_type="text" id="aitz3Hri_a-n"
# 代入は `=` の記号を用います。
# 数学的には `=` は等しいという意味を持ちますが、Python では **「左辺の変数に、右辺の値を代入する」** という意味になります。
#
# Jupyter Notebook 上では、変数名だけ、もしくは変数名を最後の行に記述したセルを実行すると、値を確認することができます。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="6SbAfM5Rv9aM" outputId="e8173162-1c03-418e-f01f-3785b6b255e9"
a

# + [markdown] colab_type="text" id="8b0i8oelv9aR"
# このように、変数に格納されている値を確認することができました。
# また、値を確認するための他の方法として、`print()` と呼ばれる**関数 (function)** を使用することもできます。
# 関数について詳しくは後述しますが、`print()` のように Python には予め多くの関数が定義されています。 そのような関数を**組み込み関数 (built-in function)** といいます。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="oTHXMTjiv9aR" outputId="fc9f6804-a059-48f1-ae0a-45ca25eecc86"
print(a)

# + [markdown] colab_type="text" id="nGNlqHW_v9aV"
# 変数につける名前は、コードを書く人が自由に決めることができます。
# ただし、わかりやすい名前をつけることがとても大切です。
# 例えば、人の名前を格納するための変数が `a` という変数名だと、それがどのような使われ方をするのかを容易に類推することができません。
# `name` という名前であれば、ひと目で見て何のための変数かが分かるようになります。
# これは、自分のコードを読む他人や、未来の自分にとってコードを理解するための大きな手がかりとなります。

# + [markdown] colab_type="text" id="BQhk7-XfDFhS"
# ### コメント
#
# Python では、`#` の後からその行の終わりまでに存在する全ての文字列は無視されます。
# この `#` の後ろに続く部分を **コメント (comment)** と呼び、すでに書かれたコードをコメントにすることを **コメントアウト (comment out)** と言います。
# コメントは、コード中に変数の意味や処理の意味をコードを読む人に伝えるためによく使われます。
#
# Jupyter Notebook のコードセルに書かれたコードを行ごとコメントアウトしたい場合は、その行を選択した状態で `Ctrl + /` を入力することで自動的に行の先頭に `#` 記号を挿入することができます。複数行を選択していれば、選択された複数の行が同時にコメントアウトされます。また、コメントアウトされている行を選択した状態で同じキー入力を送ると、コメントアウトが解除されます。
# 下のセルを実行してみましょう。

# + colab={} colab_type="code" id="YK_XjChXDXmH"
# この行及び下の行はコメントアウトされているため実行時に無視されます
# print(a)

# + [markdown] colab_type="text" id="_xAqta5WIfGJ"
# `print(a)` が書かれているにも関わらず、何も表示されませんでした。
# これは、`print(a)` 関数が書かれた行がコメントアウトされていたためです。

# + [markdown] colab_type="text" id="I_Z6hhts_v4c"
# ### 変数の型
#
# プログラミングで扱う値には種類があります。
# Python では、**整数 (integer)**、**実数 (real number)**、**文字列 (string)** などが代表的な値の種類です。
# それぞれの種類によって、コンピュータ内での取扱い方が異なり、この種類のことは一般に**型 (type)** と呼びます。
#
# 例えば、整数、実数、そして文字列をそれぞれ別々の変数に代入するコードは以下のとおりです。

# + colab={} colab_type="code" id="FChuhC8Jv9aa"
a = 1

# + colab={} colab_type="code" id="qCdjuQqNv9ac"
b = 1.2

# + colab={} colab_type="code" id="VLMovMgnv9ae"
c = 'Chainer'

# + [markdown] colab_type="text" id="DwMajDvAv9ag"
# プログラムは型によって変数の取り扱いが異なるため、型の違いがエラーの原因になることがあります。そのため、簡単に型の特徴は把握しておく必要があります。
#
# まずは、上記の `a`, `b`, `c` の型を確認する方法を紹介します。
# 型の確認は `type()` という組み込み関数を使用します。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="RUflpSu6v9ag" outputId="3219c3be-c030-478f-ef28-b2da097fc8f4"
type(a)

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="YBtHAigUv9aj" outputId="36b7795d-d590-4b51-c02e-b3aa656d6bd5"
type(b)

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="6PaQmlMCv9an" outputId="a0b6ebc3-0871-47f6-b8e1-46937b23d623"
type(c)

# + [markdown] colab_type="text" id="gatuDQAyv9aq"
# `a` は `int` という整数の型をもつ変数であり、`b` は `float` という実数の型をもつ変数です。
# この `float` という型の名前は、コンピュータ内で実数を扱うときの形式である**浮動小数点数 (floating-point number)** に由来しています。
#
# `c` は `str` という文字列の型をもつ変数であり、値を定義するにはシングルクォーテーション `' '` もしくはダブルクォーテーション `" "` で対象の文字列をくくる必要があります。

# + [markdown] colab_type="text" id="Chdmx6HGIfEV"
# Python では、`.` を含まない連続した数字を `int`、直前・直後も含め `.` が含まれる連続した数字を `float` だと自動的に解釈します。
# 例えば、`7` や `365` は `int` ですが、`2.718`、`.25`、`10.` などは `float` になります。

# + [markdown] colab_type="text" id="by0V-W7nIfEj"
# 例えば、実数の `5` は以下のように書くことができます。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="uUYCOBaAIfEj" outputId="00c3e638-e7dd-4d7a-affa-863d9407c9e0"
type(5.0)

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="y26NMdQ2IfEo" outputId="cc8fe9ce-1a65-444c-cc59-3d11de8862b0"
type(5.)

# + [markdown] colab_type="text" id="g3BdGDJaIfEr"
# 一方、`.5` と書くと、これは `0.5` の略記と解釈されることに注意してください。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="aXpxR7WmIfEs" outputId="f6ade488-902d-4d96-9cc0-e0a96caca7f6"
type(.5)

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="enBKbL9fIfEx" outputId="992db59f-1989-4d2d-db0d-241aa434cc83"
print(.5)

# + [markdown] colab_type="text" id="VsdsnV9uiQev"
# ### 算術演算子
#
# 様々な計算を意味する**演算子**と呼ばれる記号があります。
# はじめに紹介するのは**算術演算子 (arithmetic operator)** と呼ばれるもので、 2 つの変数または値を取り、 1 つの演算結果を返します。
#
# 代表的な演算として**四則演算（加算・減算・乗算・除算）**があります。
# 四則演算に対応する演算子として、Python では以下の記号が用いられます。
#
# | 演算 | 記号 |
# |------|------|
# | 加算（足し算） | `+` |
# | 減算（引き算） | `-` |
# | 乗算（掛け算） | `*` |
# | 除算（割り算） | `/` |
#
# 具体例を見ながら使い方を説明します。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="MBaRZ2RkBWbd" outputId="744c489e-75bd-4fbb-f6c1-7e73d751ff07"
# 整数と整数で加算 -> 結果は整数
1+1

# + [markdown] colab_type="text" id="DE56EVRvIfFJ"
# このように、演算子を使う際には、**記号の両側に値を書きます。**
# このとき、演算子の両側にひとつずつ空白を空けることが多いです。
# 文法的な意味はありませんが、コードが読みやすくなります。
# この空白は Python のコーディング規約である [PEP8](https://pep8-ja.readthedocs.io/ja/latest/#section-14) でも推奨されています。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="BSsWGE_Ev9bH" outputId="3a1c9e29-c5de-4d34-b3b3-3a240378e4bd"
1 + 1

# + [markdown] colab_type="text" id="ai1hzuv6v9bJ"
# 値が代入されている変数との演算も下記のように行うことができます。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="yvA4BP5hIfFJ" outputId="cedf23b1-33b6-4f96-c655-9b64346e755c"
a + 2

# + [markdown] colab_type="text" id="y6xkeITrv9bL"
# また、`int` と `float` は異なる型同士ですが、計算を行うことができます。
# `int` と `float` の演算結果の型は `float` になります。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="IjU6vwcdIfFM" outputId="21f73fdf-108e-4988-f2b4-4cfcffc219bf"
# 整数と実数で加算 -> 結果は実数
a + b

# + [markdown] colab_type="text" id="PwsK4SxPIfFN"
# 他の演算子の例を示します。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="hL5QmnGgBYNF" outputId="d408993d-3a50-4e49-9e40-f15696984208"
# 整数と整数で減算 -> 結果は整数
2 - 1

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="huifgJVkv9bR" outputId="1b6ddcff-4a15-4306-b615-cc27c0ccb0b2"
# 実数と整数で減算 -> 結果は実数
3.5 - 2

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="v82yE4keBZeo" outputId="40c8b70c-1e5a-4649-c5d4-141a9cefc76e"
# 整数と整数で乗算 -> 結果は整数
3 * 5

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="kYYOMXTHv9bX" outputId="a1fde9ed-7a8f-4184-f2e4-86e1a76b6c3d"
# 実数と整数で乗算 -> 結果は実数
2.5 * 2

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="KHRGnOcNBi05" outputId="a988ca7c-861f-4529-b243-c195573c0e2c"
# 整数と整数で除算 -> 結果は実数
3 / 2

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="NxnIvty-v9bd" outputId="d1057e6c-490d-4dfc-fea6-53b6121bda09"
# 整数と整数で除算 -> 結果は実数
4 / 2

# + [markdown] colab_type="text" id="TDJRJR5vIfFe"
# Python 3 では、 `/` 記号を用いて除算を行う場合、除数（割る数）と被除数（割られる数）が整数であっても、計算結果として実数が返ります。
# 計算結果として実数を返す除算のことを特に、**真の除算 (true division)** と言います。
# 一方、商（整数部分）を返すような除算演算子として、 `//` 記号が用意されています。 `/` 記号を 2 回、間を空けずに繰り返します。計算結果として商を返す除算のことを、 **切り捨て除算 (floor division)** と呼びます。
# 商を計算したい場合に便利な演算子であるため、こちらも覚えておきましょう。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="PFwX_4_pBbY0" outputId="260dd494-deb0-49c6-edb6-19d1662137e7"
# 整数と整数で切り捨て除算 -> 結果は整数
3 // 2

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="nCyFpJHKv9bh" outputId="32099b02-2f65-46c5-89d9-343396552ed9"
# 整数と整数で切り捨て除算 -> 結果は整数
4 // 2

# + [markdown] colab_type="text" id="Mywi7srHv9bj"
# また、ここで注意すべき点として、整数や実数と文字列の演算は基本的にエラーになります。

# + colab={"base_uri": "https://localhost:8080/", "height": 172} colab_type="code" id="ia8mAAr5v9bj" outputId="38cd2f68-c08d-4abe-c8bf-300d8c8b1154"
# error
a + c

# + [markdown] colab_type="text" id="T24iNnwSv9bk"
# **エラーメッセージを読みましょう。**
#
# > TypeError: unsupported operand type(s) for +: 'int' and 'str'
#
# と言われています。「+ にとって int と str はサポートされていない被作用子（+ が作用する対象のこと。operand）です」と書かれています。「int に str を足す」ということはできないというわけです。
#
# このようにエラーメッセージからは自分のミスに関する情報を得ることができます。
# 何を間違えたかはエラーをもとに調べれば大抵わかりますから、まずはエラーについて調べることを心がけましょう。
#
# `int` もしくは `float` と、 `str` の間の加算、減算、除算では上記のエラーが生じます。
# ただし、`str` と `int` の**乗算**は特別にサポートされており、計算を実行することができます。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="oKJmWQKcv9bl" outputId="513c4f7e-081e-4b3f-826a-39e8e5885dff"
# str と int で乗算
c * 3

# + [markdown] colab_type="text" id="xPX4dcGUv9bm"
# 上のコードは、`c` という文字列を `3` 回繰り返す、という意味になります。

# + [markdown] colab_type="text" id="mmlvVMcIv9bm"
# `str` 同士は足し算を行うことができます。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="DOK7H8LJv9bn" outputId="5654572a-9d44-423a-9ada-da324b5f7dfa"
name1 = 'Chainer'
name2 = 'チュートリアル'

name1 + name2

# + [markdown] colab_type="text" id="QoCq87hkv9bq"
# 整数と文字列を連結したいこともあります。
# 例えば、`1` という整数に、 `'番目'` という文字列を足して `'1番目'` という文字列を作りたいような場合です。
# その場合には、型を変換する**キャスト (cast)** という操作をする必要があります。
#
# 何かを `int` にキャストしたい場合は `int()` という組み込み関数を使い、`str` にキャストしたい場合は `str()` という組み込み関数を使います。では、`1` という整数を `str` にキャストして、 `'番目'` という文字列と足し算を行ってみましょう。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="H8E1Puhmv9bq" outputId="31d58419-7b97-4bc6-f923-79f2c8fd9edb"
1

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="TlnTtXUnv9br" outputId="b970fbfe-4151-42f9-ad44-0e607f912e02"
type(1)

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="EK9fF95av9bt" outputId="a5ef7604-c6ed-4ffd-e19c-39b39496c752"
str(1)

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="JxGEBOZzv9bw" outputId="cca1f61a-82c9-4f12-9921-97068ab3a6d0"
type(str(1))

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="2boojYfbv9by" outputId="9ac453cd-d210-4f5c-fcac-1502f0b69482"
str(1) + '番目'
# -

# 演算子の話から少しそれますが、フォーマット文字列を使用すると `+` を使用せずに、自然な文字列の中に変数の値を埋め込むことができます。
# フォーマット文字列の書き方はいくつかありますが、簡単な例を 2 つ紹介します。
#
# 文字列を通常のクォーテーション (`"", ''`) の代わりに、`f` がついた `f""` または `f''` で囲みます。
# すると、変数を波括弧で囲んで文字列に挿入すると、その部分に変数の値が埋め込まれます。

d = 1
f'{d}番目'

# 文字列に空の波括弧 `{}` を挿入して、文字列の後ろに `.format()` を続けて書くと、format 関数に渡された変数の値が `{}` の部分に埋め込まれます。

d = 1
'{}番目'.format(d)

# + [markdown] colab_type="text" id="RzvUMnTQv9bz"
# 演算子に話を戻します。`+=` や `-=` もよく使われる演算子です。
# これは、演算と代入を合わせて行うもので、**累積代入文 (augmented assignment statement)** と呼ばれます。
#
# 下記に示すとおり、`+=` では左辺の変数に対して右辺の値を足した結果で、左辺の変数を更新します。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="g7g0hOrOv9b0" outputId="914559f8-251d-4d5c-9edd-6cc9a778c484"
# 累積代入文を使わない場合
count = 0
count = count + 1
count

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="bdgvqEjZv9b2" outputId="0cbef171-cbc1-4cb8-b965-1f52fcd005a6"
# 累積代入文を使う場合
count = 0
count += 1
count

# + [markdown] colab_type="text" id="AZ7QMIt-v9b3"
# 四則演算の全てで累積代入文を利用することができます。
# つまり、`+=`, `-=`, `*=`, `/=` がそれぞれ利用可能です。

# + [markdown] colab_type="text" id="36GMdun-IfFn"
# Python には、他にも幾つかの算術演算子が用意されています。
# 例えば以下の演算子です。
#
# | 演算 | 記号 |
# |------|------|
# | 累乗 | `**` |
# |  剰余　 | `%` |
#
# `**` を使うと、$2^3$ は以下のように記述することができます。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="cK6zHxguIfFo" outputId="eb9bdd74-8294-49f5-aae4-a9566f3d7ddf"
# 累乗
2 ** 3

# + [markdown] colab_type="text" id="g8RG0jTDv9b6"
# `%` を使って、`9` を `2` で割った余りを計算してみましょう。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="CbsiwPcev9b6" outputId="27688f90-fef0-4d2d-8633-960ea0e8b128"
# 剰余
9 % 2

# + [markdown] colab_type="text" id="Z62QzE-4Bc4a"
# ### 比較演算子
#
# 比較演算子は、2 つの値の比較を行うための演算子です。
#
# | 演算 | 記号 |
# |------|------|
# | 小なり | `<` |
# | 大なり | `>` |
# | 以下 | `<=` |
# | 以上 | `>=` |
# | 等しい | `==` |
# | 等しくない | `!=` |
#
# 比較演算子は、その両側に与えられた値が決められた条件を満たしているかどうか計算し、満たしている場合は `True` を、満たしていない場合は `False` を返します。
# `True` や `False` は、**ブール (bool) 型**と呼ばれる型を持った値です。
# ブール型の値は `True` もしくは `False` の 2 つしか存在しません。
#
# いくつかの比較演算子の計算例を示します。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="5AXOptIWCN53" outputId="2525fafa-f2dd-40b6-adaa-9af505b059c4"
1 < 2

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="ETSRMdkDv9b-" outputId="fb2a62ee-87a1-488a-9a77-e99854e5a083"
# 型の確認
type(1 < 2)

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="wR2OPEwiCP5_" outputId="bd6701e6-b948-4ebb-f852-12ac81244631"
2 == 5

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="TfEDslvKCQ7o" outputId="629c30b4-ab73-49be-e8dc-e9bd78ba460b"
1 != 2

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="W1v_F8-7CWI-" outputId="789351f8-d4a5-41a7-8732-72f5ab885abd"
3 >= 3

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="XapxlGSYCSOU" outputId="7f4fac18-bed4-490d-cb25-598737c2f7e2"
'test' == 'test'

# + [markdown] colab_type="text" id="aBzVaMJ1IfF7"
# 等しいかどうかを判定する比較演算子 `==` を使う際は、代入演算子 `=` と間違えないように気をつけてください。

# + [markdown] colab_type="text" id="VsBRE0Wyv9ca"
# ## 複合データ型
#
# これまでは `a = 1` のように 1 つの変数に 1 つの値を代入する場合を扱ってきましたが、複数の値をまとめて取り扱いたい場面もあります。
# Python では複数の変数や値をまとめて扱うのに便利な、以下の 3 つの複合データ型があります。
#
# - リスト (list)
# - タプル (tuple)
# - 辞書 (dictionary)

# + [markdown] colab_type="text" id="S1TLaajMDtmr"
# ### リスト
#
# 複数の変数を `,` （カンマ）区切りで並べ、それらの全体を `[ ]` で囲んだものを **リスト (list)** と言います。
# リストに含まれる値を**要素**と呼び、整数の**インデックス** （要素番号）を使ってアクセスします。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="MJ7ZYj82D-a1" outputId="970de678-1f56-4078-8f10-c7042c0fb8e5"
# リスト型の変数を定義
numbers = [4, 5, 6, 7]

# 値の確認
print(numbers)

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="HH3NT-y4EC4Z" outputId="cbcc163e-040f-4878-d3f5-65b6659bffa3"
# 型の確認
type(numbers)

# + [markdown] colab_type="text" id="Rk_jY_TTIfGY"
# `numbers` には 4 つの数値が入っており、**要素数** は 4 です。
# リストの要素数は、リストの**長さ (length)** とも呼ばれ、組み込み関数の `len()` を用いて取得することができます。
# `len()` はよく使う関数であるため、覚えておきましょう。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="DK6aH0AaoELi" outputId="76d0dab8-bd1b-4c86-95b8-e25d6cca02c5"
# 要素数の確認
len(numbers)

# + [markdown] colab_type="text" id="RiJeRUdrEEUq"
# リストの各要素へアクセスする方法はいくつかあります。
# 最も簡単な方法は `[]` を使ってアクセスしたい要素番号を指定して、リストから値を取り出したり、その位置の値を書き換えたりする方法です。
# ここで、注意が必要な点として、Python では先頭の要素のインデックス番号が `0` である点があります。
# インデックス番号 `1` は 2 番目の要素を指します。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="DeCsf_L1Em29" outputId="4cfc90bc-62e4-466d-ab0d-0a29877decef"
# 先頭の要素にアクセス
numbers[0]

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="ox-Ma4yv5xqO" outputId="7c6ee95d-c6cd-472d-9ea5-c4a44e8d9f0f"
# 先頭から3番目の要素にアクセス
numbers[2]

# + colab={} colab_type="code" id="ve-ETFIrv9cg"
# 2 番目の要素を書き換え
numbers[1] = 10

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="AXpG-tqNv9cg" outputId="1fa368f6-7164-4896-89fd-981d033adaa3"
# 値の確認
numbers

# + [markdown] colab_type="text" id="kOVYiVOwIfGW"
# また、インデックスに負の値を指定すると、末尾からの位置となります。
# 要素番号 `-1` で最後の要素を参照することができます。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="WSaIdvb4IfGX" outputId="5bbb1cee-081d-4a68-a918-ad275b3b1172"
# 末尾の要素にアクセス
numbers[-1]

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="jP5fkl3V54WL" outputId="aaf2ac71-f21a-4c41-aab4-337e25f54331"
# 末尾から3番目の要素にアクセス
numbers[-3]

# + [markdown] colab_type="text" id="DLzLjTQ8EoG9"
# 次に、リストから一度に複数の要素を取り出す操作である**スライス (slice)** を紹介します。
# `開始位置:終了位置` のようにコロン `:` を用いてインデックスを範囲指定し、複数の部分要素にアクセスします。
# このスライスの処理は、この後の章でも多用するため、慣れておきましょう。
#
# 例えば、先頭から 2 つの要素を取り出したい場合、以下のように指定します。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="MPI2H38DEy2N" outputId="623cb4f8-54fc-4f34-924c-7da10dacdeef"
numbers[0:2]

# + [markdown] colab_type="text" id="gK6_JXXTE2AY"
# `開始位置:終了位置` と指定することで、開始位置から**終了位置のひとつ手前**までの要素を抽出します。 
# 終了位置に指定したインデックスの値は含まれないことに注意してください。
#
# また、指定する開始番号が `0` である場合、以下のような略記がよく用いられます。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="hBo2_C5aFPHR" outputId="1b249507-b615-4adf-dd4b-3c399799ba88"
numbers[:2]

# + [markdown] colab_type="text" id="Qqem8sujFQVP"
# このように、先頭のインデックスは省略することができます。
# このような記法を使う場合は、終了位置を示す数字を**取り出したい要素の個数**と捉えて、**先頭から 2 つを取り出す**操作だと考えると分かりやすくなります。
#
# 同様に、ある位置からリストの末尾までを取り出す場合も、終了位置のインデックスを省略することができます。
# 例えば、2 個目の要素から最後までを取り出すには以下のようにします。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="gItFJqoUFYzX" outputId="2bc2f7e8-b6cb-4bbb-8245-ec8835e87447"
numbers[1:]

# + [markdown] colab_type="text" id="RRlf3vqOv9cq"
# この場合は、取り出される要素の個数は `len(numbers) - 1` 個となることに注意してください。  
# 以上から、`numbers[:2]` と `numbers[2:]` は、ちょうど 2 個目の要素を境に `numbers` の要素を 2 分割した前半部分と後半部分になっています。
# ここで、インデックスが 2 の要素自体は**後半部に含まれる**ということに注意してください。
# また、開始位置も終了位置も省略した場合は、すべての要素が選択されます。
#
# 一見ややこしい挙動のようですが、ここで下画像のようにインデックスは要素の間にふられているとすると理解しやすくなります。  
# 例えば `numbers[:2]` は「2の位置"まで"」だから2個目の要素は含まないというわけです。  
# ![indexのイメージ](./images/02/02_indexing.jpg)
#
# ちなみにこれは[Pythonの公式ドキュメント](https://docs.python.org/ja/3/tutorial/introduction.html#strings)で紹介されている覚え方です。
# -

# 全ての要素を選択する場合、下記のように書くこともできます。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="nav8WoxNv9cq" outputId="b35c3b9d-f123-42a4-9d5b-505a31be278e"
numbers[:]

# + [markdown] colab_type="text" id="9qPrP6sYv9cs"
# 現状では、`numbers[:]` と `numbers` の結果が同じであるため、どのように使用するか疑問に思われるかも知れません。  
# しかし、後の章では NumPy というライブラリを用いてリストの中にリストが入ったような**多次元配列 (multidimensional array)** を扱っていきます。  
# そして多次元配列を用いて行列を表す場合には、`0 列目のすべての値`を抽出するために `[:, 0]` のような記法を用いるケースが登場します。  
# これは Python 標準の機能ではありませんが、Python 標準のスライス表記を拡張したものになっています。
#

# + [markdown] colab_type="text" id="AyoiOU5OFfET"
# リストは数値以外に、文字列を扱うこともでき、また複数の型を同一のリスト内に混在させることもできます。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="9JglgRiWFyo8" outputId="f8700d40-519f-4e92-db32-60fcadc145c0"
# 文字列を格納したリスト
array = ['hello', 'world']
array

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="Kcf8MyrBv9cu" outputId="c5f989f4-138a-4a1c-ac4a-60760f318618"
# 複数の型が混在したリスト
array = [1, 1.2, 'Chainer']
array

# + [markdown] colab_type="text" id="9fKT2sjNv9cu"
# リストにリストを代入することもできます。
# また、Python 標準のリストでは入れ子になったリスト内の要素数がばらばらでも問題ありません。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="Q8JxfHS8v9cv" outputId="572e4d48-aae1-46e9-cf6a-f2fbf1d68ac4"
array = [[1, 1.2, 'Chainer', True], [3.2, 'Tutorial']]
array

# + [markdown] colab_type="text" id="5lYy-LP6F3wP"
# リストを使う際に頻出する操作として、**リストへの値の追加**があります。
# リスト型には `append()` というメソッドが定義されており、これを用いてリストの末尾に新しい値を追加することができます。
#
# 上記の `array` に値を追加してみましょう。

# + colab={} colab_type="code" id="RmgtEN8Lv9cw"
# 末尾に 2.5 を追加
array.append(2.5)

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="2E8q5y94v9cx" outputId="c2993fd6-a0f4-4786-b61a-f5462cae0817"
# 値の確認
array

# + [markdown] colab_type="text" id="y5dQJA57v9cz"
# また、今後頻出する処理として、**空のリスト**を定義しておき、そこに後段の処理の中で適宜新たな要素を追加していくという使い方があります。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="00AEmnpxGPky" outputId="7f95e646-3264-4f63-cb58-98fc6bd42e73"
# 空のリストを定義
array = []

# 空のリストに要素を追加
array.append('Chainer')
array.append('チュートリアル')

array

# + [markdown] colab_type="text" id="CV1072C3M7Qy"
# ### タプル
#
# **タプル (tuple)** はリストと同様に複数の要素をまとめた型ですが、リストとは異なる点として、定義した後に**中の要素を変更できない**という性質を持ちます。
#
# タプルの定義には `( )`を用います。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="mo4lGZN6NGAI" outputId="8234b24e-fd6d-4e77-f409-0681ad27c406"
# タプルを定義
array = (4, 5, 6, 7)
array

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="LEUgknZov9c3" outputId="96b964b2-97ef-4312-d552-ee24b5d47238"
# 型の確認
type(array)

# + [markdown] colab_type="text" id="9w2M0A02v9c3"
# タプルの定義する際に `( )` を使用したため、要素へのアクセスも `( )` を使うように感じるかもしれませんが、実際にはリストと同様 `[ ]` を使用します。  

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="Fq7zIHMfNIXG" outputId="8cc0dcde-bfc6-4d74-cb73-6a716394bb98"
# 先頭の要素へアクセス
array[0]

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="3XdB2S5pv9c4" outputId="c270d121-31e8-4b38-f1c7-0f15b49f4b1e"
# リストと同様、スライスも使用可能
array[:3]

# + [markdown] colab_type="text" id="KjdkYtSmNSl3"
# 先述の通り、タプルは各要素の値を変更することができません。
# この性質は、定数項などプログラムの途中で書き換わってしまうことが望ましくないものをまとめて扱うのに便利です。
#
# 実際に、タプルの要素に値の書き換えを行うとエラーが発生します。

# + colab={"base_uri": "https://localhost:8080/", "height": 172} colab_type="code" id="DRoToOjUNI51" outputId="3db3cb2f-673f-4463-dbe3-82ced4e09830"
# error
array[0] = 10

# + [markdown] colab_type="text" id="6aq_3yNZv9c6"
# `tuple` のように中身が変更できない性質のことを**イミュータブル (immutable)**であると言います。反対に、`list` のように中身が変更できる性質のことを**ミュータブル (mutable)**であると言います

# + [markdown] colab_type="text" id="nV8Lp5jLNO66"
# ### 辞書
#
# リストやタプルでは、複数の値をまとめて扱うことができました。
# そこで、定期テストの結果をまとめることを考えてみましょう。
#
# 例えば、数学 90 点、理科 75 点、英語 80 点だったという結果を `scores = [90, 75, 80]` とリストで表してみます。
# しかし、これでは**何番目がどの教科の点数に対応するか**、一見して分かりにくいと思われます。
#
# Python の `dict` 型は、**キー (key)** とそれに対応する**値 (value)** をセットにして格納することができる型であり、このようなときに便利です。
#
# リストやタプルでは、各要素にアクセスする際に整数のインデックスを用いていましたが、辞書ではキーでインデックス化されているため、整数や文字列など、色々なものを使って要素を指定することができます。
#
# 辞書は `{}` を用いて定義し、要素にアクセスする際には、リストやタプルと同様に `[ ]` を使用し、`[ ]` の中にキーを指定して対応する値を取り出します。
# -

# `[ ]` による要素へのアクセスは複数の要素を持つ型において一般的な記法なのがわかると思います。  
# 要素のどれにアクセスするのかを、リストやタプルではインデックスで、辞書ではキーで指定するわけです。

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="NyxphI5fNMO8" outputId="c4d9a198-171f-4c0e-ec96-de8cdc161c0d"
# 辞書を定義
scores = {'Math': 90, 'Science': 75, 'English': 80 }
scores

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="M-V2XOEdNu2a" outputId="ee4bdf90-c4e5-4a92-a6d0-d79e3bcf2b1c"
# key が Math の value にアクセス
scores['Math'] 

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="TA5V7SUBv9c8" outputId="90c16e6d-1de9-4931-efbe-b2164e075b6b"
# key に日本語を使用することも可能
scores = {'数学': 90, '理科': 75, '英語': 80}
scores

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="IL2y81t-v9c9" outputId="7ea8f85a-c3d2-4ad2-cda5-74bd524868f3"
scores['数学']

# + [markdown] colab_type="text" id="Jd_XpPMqfrSL"
# 他の人が定義した辞書に、**どのようなキーが存在するのか**を調べたいときがあります。
# 辞書には、そのような場合に使える便利なメソッドがいくつか存在します。
#
# - `keys()`: キーのリストを取得。`dict_keys` というリストと性質が似た型が返る
# - `values()`: 値のリストを取得。`dict_values` というリストと性質が似た型が返る
# - `items()`: 各要素の `(key, value)` のタプルが並んだリストを取得。`dict_items` というリストと性質が似た型が返る

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="FkJjSlbShKjK" outputId="93597067-1c5e-4ab0-ab5f-3301524f6bff"
# キーのリスト
scores.keys()

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="YOAOTDtUhNBz" outputId="ad624c25-5b59-4544-dde2-94ec3adde7ea"
# 値のリスト
scores.values()

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="mWA7opwAhVEa" outputId="26ee1d21-3011-49df-f1ff-e6188e698b1c"
# (キー, 値)というタプルを要素とするリスト
scores.items()

# + [markdown] colab_type="text" id="I9WEXgSZv9dC"
# `dict_keys`, `dict_values`, `dict_items` と新しい型が登場しましたが、これは辞書型特有の型であり厳密には標準のリストとは異なりますが、リストと性質の似た型であるという程度の認識で問題ありません。

# + [markdown] colab_type="text" id="qpoTmSY8bTDw"
# 辞書に要素を追加する場合は、新しいキーを指定して値を代入します。

# + colab={} colab_type="code" id="nDZ4RRcjnERu"
scores['国語'] = 85

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="P0HJVZJSnKal" outputId="700a1c1a-d175-40c9-c008-56dca29eb5f8"
scores

# + [markdown] colab_type="text" id="NIC2fwAknPf9"
# また、既に存在するキーを指定した場合には、値が上書きされます。

# + colab={} colab_type="code" id="teLZbAHQnUfN"
scores['数学'] = 95

# + colab={"base_uri": "https://localhost:8080/", "height": 35} colab_type="code" id="kQESKoXgnYRN" outputId="1b2e3718-26d7-4d5e-fa90-e7fc4850795a"
scores
