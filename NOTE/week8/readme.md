## 執行結果
### textgen
[textgen2.py](https://github.com/nohano1l/ai110b/blob/master/NOTE/week8/textgen/textgen2.py)

[結果](https://github.com/nohano1l/ai110b/blob/master/NOTE/week8/textgen/text.out)
### eliza
[eliza.py](https://github.com/nohano1l/ai110b/blob/master/NOTE/week8/eliza.py)
```
cxz1d@MSI MINGW64 ~/OneDrive/桌面/nohano1l/ai110b/NOTE/week8 (master)
$ python eliza.py 
你好，我是 Eliza ! 
> 你好
你好，有甚麼問題嗎?
> 沒有
可以說的更詳細一點嗎?
> 就沒有啊
這樣喔! 我知道!
> 你在幹嘛?
別說我了，談談你吧!
> 我沒什麼要說的  
為何不問問別人?
> 問你你會說不知道
在想想看，有沒有甚麼可能性?
> 你覺得呢?
你自己覺得呢
> 我不知道才問你啊
在想想看，有沒有甚麼可能性?
> 你打第二次了
別說我了，談談你吧!
> 晚餐要吃甚麼?
你認為答案是甚麼呢?
> 我還沒吃
再來呢? 可以多說一些嗎
> 我在想，所以問你的意見
真的想，所以問我的意見?
> 對阿
我了解!
> 你可以說說看
不要再說我了，談談你吧!
> 笨機器人
多談談有關你的事，好嗎?
> 你生氣喔
別說我了，談談你吧!
> 我很聰明
再來呢? 可以多說一些嗎
> 你很笨
你自己很笨
```

### jieba
[jieba2.py](https://github.com/nohano1l/ai110b/blob/master/NOTE/week8/jieba2.py)
```
$ pip install jieba     //先下載Jieba

cxz1d@MSI MINGW64 ~/OneDrive/桌面/nohano1l/ai110b/NOTE/week8 (master)
$ python jieba2.py "喜歡上一個人"
Building prefix dict from the default dictionary ...
Loading model from cache C:\Users\cxz1d\AppData\Local\Temp\jieba.cache
Loading model cost 0.521 seconds.
Prefix dict has been built successfully.
斷詞結果: 喜歡/ 上/ 一個/ 人

cxz1d@MSI MINGW64 ~/OneDrive/桌面/nohano1l/ai110b/NOTE/week8 (master)
$ python jieba2.py "不要用壞了"
Building prefix dict from the default dictionary ...
Loading model from cache C:\Users\cxz1d\AppData\Local\Temp\jieba.cache
Loading model cost 0.520 seconds.
Prefix dict has been built successfully.
斷詞結果: 不要/ 用壞/ 了
```