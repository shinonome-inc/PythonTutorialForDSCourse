# 【確認課題】Python 入門 

## 問 1. 計算

提出ファイル：`quadratic_formula.py`

2 次方程式 $ax^2+bx+c=0$ の解 $x$ は、下式で求めることができます:

$x = \dfrac{-b\pm \sqrt{b^2 - 4ac}}{2a}$

この解の公式を実装して、次の 2 次方程式の解が得られるかを確認しましょう。

(1) $x^2-6x+9=0$ の解は $3$  
(2) $x^2+2x-8=0$ の解は $2$ と $-4$  
(3) $8x^2-6x-35=0$ の解は $5/2$ と $-7/4$  
(4) $x^2+1=0$ の解は $j$ と $-j$ &nbsp; ( $j$ は虚数単位)

<!-- (x-3)^2 -->
<!-- (x-2)(x+4) -->
<!-- (2x-5)(4x+7) -->
<!-- (x+j)(x-j) -->

### 補足

- ルート（ $\sqrt{a}$ ）は、2 分の 1 乗（ $a^{1/2}$ ）として計算できます。
- (4) の解には計算誤差が含まれると思います。Python がどこまで正しい精度で計算できるかは『[制御構文 問 4. マシンイプシロン][eps]』を解くと分かります。（お楽しみに）

[eps]: https://shinonome.io/PythonTutorialForDSCourse/exercise/02_02_Basics_of_Python_control.html#id5

---

## 問 2. 文字列

提出ファイル：`pi.py`

`How I want a drink, alcoholic` の英単語の文字数を並べると 314159 になり、円周率の数字の並びと同じになります。

この問題で実装するのは、24 単語からなる下の英文:

```
How I want a drink, alcoholic of course, after the heavy chapters involving
quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
```

の文字数を並べた文字列 (str 型) を出力するプログラムです。
実行結果は円周率 24 桁目までの `314159265358979323846264` になるはずです。

### 補足

- 求めるのは「英単語の文字数」なので記号は無視する必要があります。
-  ヒント。下のコードのように `list, map, len` 関数を用いると、与えられたリストの各要素の文字数を得ることができます。
    ```python
    >>> list(map(len, ["a", "bc", "def"]))
    [1, 2, 3]
    ```
    つまり、区切って文字を数えてくっつければ解けそう…？