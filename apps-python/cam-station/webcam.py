import cv2
from torchvision import transforms

import torch
import numpy as np

import skimage
from skimage import io, transform

def load_image(image_path):
    """Code from Loading_Pretrained_Models.ipynb - a Caffe2 tutorial"""
    img = skimage.img_as_float(skimage.io.imread(image_path))
    if len(img.shape) == 2:
        img = np.array([img, img, img]).swapaxes(0,2)
    return img

def rescale(img, input_height, input_width):
    """Code from Loading_Pretrained_Models.ipynb - a Caffe2 tutorial"""
    aspect = img.shape[1]/float(img.shape[0])
    if(aspect>1):
        # landscape orientation - wide image
        res = int(aspect * input_height)
        imgScaled = skimage.transform.resize(img, (input_width, res))
    if(aspect<1):
        # portrait orientation - tall image
        res = int(input_width/aspect)
        imgScaled = skimage.transform.resize(img, (res, input_height))
    if(aspect == 1):
        imgScaled = skimage.transform.resize(img, (input_width, input_height))
    return imgScaled

def crop_center(img,cropx,cropy):
    """Code from Loading_Pretrained_Models.ipynb - a Caffe2 tutorial"""
    y,x,c = img.shape
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)
    return img[starty:starty+cropy,startx:startx+cropx]

def normalize(img, mean=128, std=128):
    img = (img * 256 - mean) / std
    return img

def prepare_input(img_uri):
    img = load_image(img_uri)
    img = rescale(img, 300, 300)
    img = crop_center(img, 300, 300)
    img = normalize(img)

    return img

def prepare_tensor(inputs):
    NHWC = np.array(inputs)
    NCHW = np.swapaxes(np.swapaxes(NHWC, 2, 3), 1, 2)
    tensor = torch.from_numpy(NCHW)
    tensor = tensor.cuda()
    tensor = tensor.half()

    return tensor


precision = 'fp32'
ssd_model = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd', model_math=precision)
ssd_model.to('cuda')
ssd_model.eval()

uris = [
    'http://images.cocodataset.org/val2017/000000397133.jpg',
    'http://images.cocodataset.org/val2017/000000037777.jpg',
    'http://images.cocodataset.org/val2017/000000252219.jpg'
]

inputs = [prepare_input(uri) for uri in uris]
tensor = prepare_tensor(inputs)

# ... # ... # ... # ... # ...
# ... # ... # ... # ... # ...

cap = cv2.VideoCapture(0)
xres = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
yres = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(xres, yres)

normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
tensor = transforms.ToTensor()

# model = torch.load(args.model, map_location=lambda storage, loc: storage)
# model = model.module
# model = model.cuda()

while (True):

    ret, frame = cap.read()
    if not ret: break

    # if xres > yres:
    #    frame = frame[:,int((xres - yres)/2):int((xres+yres)/2),:]
    # else:
    #    frame = frame[int((yres - xres)/2):int((yres+xres)/2),:,:]
    # frame = cv2.resize(frame, dsize=(args.size, args.size))

    # img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # pred = pred.data.max(0)[0].numpy()
    # pred = cv2.resize(pred, dsize=(xres, yres), interpolation=cv2.INTER_CUBIC)

    # frame[:, :, 1] += pred

    cv2.imshow('frame', frame)
    # cv2.imshow('pred', pred)
    # cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cv2.destroyAllWindows()