# https://www.learnopencv.com/pytorch-for-beginners-image-classification-using-pre-trained-models/
import sys
import torch
from torchvision import models
from torchvision import transforms

# print('models=', dir(models))

model = sys.argv[1]
imgFile = sys.argv[2]

if model == 'alexnet':
    net = models.alexnet(pretrained=True)   #載入
elif model == 'resnet18':
    net = models.resnet18(pretrained=True)
else:
    raise Exception('Error', 'model='+model)

transform = transforms.Compose([            #[1]
 transforms.Resize(256),                    #[2]
 transforms.CenterCrop(224),                #[3]
 transforms.ToTensor(),                     #[4]
 transforms.Normalize(                      #[5] RGB 三種顏色的正規化
 mean=[0.485, 0.456, 0.406],                #[6]
 std=[0.229, 0.224, 0.225]                  #[7]
 )])

# Import Pillow
from PIL import Image
img = Image.open(imgFile)
# print('img=', img)

img_t = transform(img)
print('img_t.shape=', img_t.shape)
# print('img_t=', img_t)

batch_t = torch.unsqueeze(img_t, 0)
print('batch_t.shape=', batch_t.shape)
# print('batch_t=', batch_t)

net.eval()  #預測

preds = net(batch_t)
print('preds.shape=', preds.shape)
# print('preds=', preds)

with open('imagenet_classes.txt') as f:
    labels = [line.strip() for line in f.readlines()]

pred, class_idx = torch.max(preds, dim=1)  #優先預測類
print(labels[class_idx]) # Labrador retriever 代表成功辨識為『拉布拉多拾獵犬』

