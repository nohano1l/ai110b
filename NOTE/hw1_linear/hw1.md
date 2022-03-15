# 習題1-- 利用爬山演算法做線性回歸
我利用老師上課教的[regression.py](https://gitlab.com/ccc110/ai/-/blob/master/_homework/01-regression/regression.py)，並參考[通用的爬山演算法架構](https://kinmen6.com/root/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E8%AA%B2%E7%A8%8B/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/02-optimize/01-hillclimbing/04-framework/%E5%AF%A6%E4%BD%9C%EF%BC%9A%E9%80%9A%E7%94%A8%E7%9A%84%E7%88%AC%E5%B1%B1%E6%BC%94%E7%AE%97%E6%B3%95%E6%9E%B6%E6%A7%8B.md)的方式做出。

[regression.py](https://github.com/nohano1l/ai110b/blob/master/NOTE/hw1_linear/regression.py)
```
def optimize(p, maxGens, maxFails, step = 0.1):
    # 請修改這個函數，自動找出讓 loss 最小的 p
    # p = [2,1] # 這個值目前是手動填的，請改為自動尋找。(即使改了 x,y 仍然能找到最適合的回歸線)
    fails = 0                             # 失敗次數設為 0
    # 當代數 gen<maxGen，且連續失敗次數 fails < maxFails 時，就持續嘗試尋找更好的解。
    for gens in range(maxGens):
        sx = p[0]+step if random.random() > 0.5 else p[0]-step
        sy = p[1]+step if random.random() > 0.5 else p[1]-step
        snew =[sx,sy]       #  取得鄰近的解
        if (loss(snew) <= loss(p)):          #  如果鄰近解比目前解更好
            # print(gens, ':', snew.str())  #    印出新的解
            p = snew                      #    就移動過去
            fails = 0                     #    移動成功，將連續失敗次數歸零
        else:                             #  否則
            fails = fails + 1             #    將連續失敗次數加一
        if (fails >= maxFails):
            break
    return p
```

![執行結果](https://github.com/nohano1l/ai110b/blob/master/NOTE/hw1_linear/demo.png)

![執行圖表](https://github.com/nohano1l/ai110b/blob/master/NOTE/hw1_linear/picture.png)

## 遇到的問題
需下載matplotlib

當我想嘗試像通用的爬山演算法架構一樣使用多個.py，會造成循環導入，造成無法正常執行