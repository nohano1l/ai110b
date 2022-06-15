# 影像辨識
[predict.py](https://github.com/nohano1l/ai110b/blob/master/NOTE/week17/01-classify/predict.py)

執行
```
cxz1d@MSI MINGW64 ~/OneDrive/桌面/nohano1l/ai110b/NOTE/week17 (master)
$ python predict.py alexnet img/cat.jpg
img_t.shape= torch.Size([3, 224, 224])
batch_t.shape= torch.Size([1, 3, 224, 224])
preds.shape= torch.Size([1, 1000])
Egyptian cat

cxz1d@MSI MINGW64 ~/OneDrive/桌面/nohano1l/ai110b/NOTE/week17 (master)
$ python predict.py alexnet img/dog.jpg
img_t.shape= torch.Size([3, 224, 224])
batch_t.shape= torch.Size([1, 3, 224, 224])
preds.shape= torch.Size([1, 1000])
Labrador retriever
```

[segment.py](https://github.com/nohano1l/ai110b/blob/master/NOTE/week17/02-semantic/segment.py)

執行
```
$ python segment.py fnc img/horse.jpg
```
會顯示動物的位置

![馬的位置](https://github.com/nohano1l/ai110b/blob/master/NOTE/week17/02-semantic/1.png)