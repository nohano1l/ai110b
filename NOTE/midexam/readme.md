# 數位影像處理
本程式修改自[nicktien007的 github 專案](https://github.com/nicktien007/Nick.NCHU.DIP)及[[2020鐵人賽Day30]糊裡糊塗Python就上手-體驗 OpenCV 人臉辨識](https://ithelp.ithome.com.tw/articles/10251665)，經過自己理解後做的筆記。

### 授權聲明
* 本專案中的程式採用[MIT 授權](https://zh.wikipedia.org/wiki/MIT%E8%A8%B1%E5%8F%AF%E8%AD%89)
* 文章部分衍生自維基百科，採用 [CC:BY-SA](https://zh.wikipedia.org/zh-hant/Wikipedia%3ACC_BY-SA_3.0%E5%8D%8F%E8%AE%AE%E6%96%87%E6%9C%AC) 授權
* [LICENSE](https://github.com/nohano1l/ai110b/blob/master/NOTE/midexam/LICENSE)
* 若有用到非以上授權之參考資料及圖片，將會在每週的筆記內皆有標示出處

以下程式碼皆有import cv2，需安裝OpenCV
```
pip install opencv-python
```
### What is OpenCV?
OpenCV（Open Source Computer Vision）是一個跨平台的電腦視覺庫，包含許多電腦視覺相關演算處理的Open Source Library，而且支援多種開法語言，同時 OpenCV 也可以在手機APP(Android、iOS)上開發。
## 透視變形校正 Perspective Distortion Correction
在攝影和電影拍攝中，透視變形指的是是一個物體及其周圍區域與標準鏡頭中看到的相比完全不同，由於遠近特徵的相對比例變化，發生了彎曲或變形。透視變形是由拍攝和觀看圖像的相對距離決定的，因為成像的視角也許會比觀看物體的視角更窄或是更廣，這樣看上去的相對距離就會與所期待的不一樣。

[perspective.py](https://github.com/nohano1l/ai110b/blob/master/NOTE/midexam/perspective.py)

### 程式說明

輸入一張圖，輸入x1,x2,x3,x4,y1,y2,y3,y4 八個點位做透視變形校正

參數:

position1: `input_image_path`

position2: `x1,x2,x3,x4,y1,y2,y3,y4`

![Ax=b](https://github.com/nohano1l/ai110b/blob/master/NOTE/midexam/img/Axb.png)

最主要是要解`Ax=b`這個問題

執行
```
cxz1d@MSI MINGW64 ~/OneDrive/桌面/nohano1l/ai110b/NOTE/midexam (master)
$ python perspective.py ./test/5.png 258,247,650,633,271,555,261,534
b[0]=-0.038869257950530034
b[1]=1.0481283422459893
b[2]=-5.6688271196689403e-05
b[3]=258.0
b[4]=1.0035335689045937
b[5]=-0.026737967914438502
b[6]=-0.00010392849719393057
b[7]=271.0
```
![透視變形](https://github.com/nohano1l/ai110b/blob/master/NOTE/midexam/output/1.png)
## 人臉辨識

[humanface.py](https://github.com/nohano1l/ai110b/blob/master/NOTE/midexam/humanface.py)

detectMultiScale函數，它可以偵測出圖片中所有的人臉，其參數為：

![detectMultiScale參數](https://github.com/nohano1l/ai110b/blob/master/NOTE/midexam/img/參數.png)
```
# 調用偵測識別人臉函式
faceRects = face_classifier.detectMultiScale(grayImg, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
```
執行
```
cxz1d@MSI MINGW64 ~/OneDrive/桌面/nohano1l/ai110b/NOTE/midexam (master)
$ python humanface.py
```
![人臉辨識](https://github.com/nohano1l/ai110b/blob/master/NOTE/midexam/output/human_face.jpg)

## 參考資料
[維基百科_透視變形](https://zh.wikipedia.org/zh-tw/%E9%80%8F%E8%A7%86%E5%8F%98%E5%BD%A2)