# 爬山演算法
在數值分析中，爬山是一種數學優化技術，屬於局部搜索家族。它是一種迭代算法，從問題的任意解決方案開始，然後嘗試通過對解決方案進行增量更改來找到更好的解決方案。如果更改產生了更好的解決方案，則對新解決方案進行另一個增量更改，依此類推，直到找不到進一步的改進。

[一維爬山演算法](https://github.com/nohano1l/ai110b/blob/master/NOTE/week3/hillclimbing1.py)

透過往左或往右走一小步，跟自己原本的位置比較高度，並往高度比較高的地方移動，直到自己的位置比左右兩邊高。

[二維爬山演算法](https://github.com/nohano1l/ai110b/blob/master/NOTE/week3/hillclimbing2.py)

與一維爬山演算法類似，多了前後(y)方向的比較。

[二維爬山演算法_改良版](https://github.com/nohano1l/ai110b/blob/master/NOTE/week3/hillclimbing2r.py)

由於前兩者的方式，在n維度的情況下，每次移動最多需比較2n次，改良版是透過隨機與附近的一點比較高度的方法，找出最高點。當與亂數產生的點比較許多次，還是沒有比目前的位置高時，該位置即是最高點。

[二維爬山演算法_架構版](https://github.com/nohano1l/ai110b/blob/master/NOTE/week3/hillclimbing3)

執行hillClimbingNumber.py，但它會呼叫hillClimbing.py及SolutionNumber.py，SolutionNumber.py會再呼叫Solution.py
## Question(In my opinion)
爬山演算法是最佳解嗎?
```
不一定是，爬山演算法因為不是全面搜尋，所以結果可能不是最佳。
```
爬山演算法只能算最高點嗎?
```
我覺得不是，在算最高點及最低點的方式基本上是一樣的。
```
## 參考資料
[維基百科](https://en.wikipedia.org/wiki/Hill_climbing)
[什麼是hill-climbing演算法？？](https://www.itread01.com/content/1543233666.html)