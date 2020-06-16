import glob
import os
import time

import torch
from PIL import Image
from vizer.draw import draw_boxes

from ssd.config import cfg
from ssd.data.datasets import COCODataset, VOCDataset
import argparse
import numpy as np

from ssd.data.transforms import build_transforms
from ssd.modeling.detector import build_detection_model
from ssd.utils import mkdir
from ssd.utils.checkpoint import CheckPointer

ssd_model = 'SSDData/model_012500.pth'
ssd_config = 'SSDData/vgg_ssd300_voc0712.yaml'

class SSDSmoke:
    def __init__(self, _device="cuda", _cfg = cfg, _ckpt = ssd_model, _threshold = 0.7):
        print("Init detector")
        self.isReady = False
        self.dataset_type = "voc"
        self.class_names = VOCDataset.class_names
        self.device = _device
        self.config_file = ssd_config
        self.cfg = _cfg
        self.cfg.merge_from_file(self.config_file)
        self.cfg.freeze()
        self.model = build_detection_model(self.cfg)
        self.model = self.model.to(self.device)
        self.ckpt = _ckpt
        self.checkpointer = CheckPointer(self.model, save_dir=self.cfg.OUTPUT_DIR)
        self.checkpointer.load(self.ckpt, use_latest=self.ckpt is None)
        self.weight_file = self.ckpt if self.ckpt else self.checkpointer.get_checkpoint_file()
        self.threshold = _threshold


    def preparingModel(self):
        print('Loaded weights from {}'.format(self.weight_file))
        self.transforms = build_transforms(self.cfg, is_train=False)
        self.model.eval()
        self.isReady = True

    
    def forward(self, batch):
        images_list = []
        height_list = []
        width_list = []
        for image in batch:
            height, width = image.shape[:2]
            height_list.append(height)
            width_list.append(width)
            image = self.transforms(image)[0].unsqueeze(0)
            images_list.append(image)

        images = torch.cat(images_list,0)
        result_cpu = []
        with torch.no_grad():
            results_gpu = self.model(images.to(self.device))
            for id in range(len(results_gpu)):
                result = results_gpu[id].resize((width_list[id], height_list[id])).to('cpu').numpy()    
                result_cpu.append(result)
        
        return result_cpu

    def predict(self, batch):
        probs = self.forward(batch)
        ret = []
        for id in range(len(probs)):
            boxes, labels, scores = probs[id]['boxes'], probs[id]['labels'], probs[id]['scores']
            indices = scores > self.threshold
            boxes = boxes[indices]
            labels = labels[indices]
            scores = scores[indices]
            draw = draw_boxes(batch[id], boxes, labels, scores, self.class_names).astype(np.uint8)
            ret.append(draw)
        return ret

    def predict_boxes(self, batch):
        probs = self.forward(batch)
        ret = []
        for id in range(len(probs)):
            boxes, labels, scores = probs[id]['boxes'], probs[id]['labels'], probs[id]['scores']
            indices = scores > self.threshold
            boxes = boxes[indices]
            ret.append(boxes)
        return ret
        
# if __name__ == "__main__":
#     tmp = SSDSmoke()
#     images_dir = "demo"
#     image_paths = glob.glob(os.path.join(images_dir, '*.png'))
#     image_list = []
#     for i, image_path in enumerate(image_paths):
#         image_name = os.path.basename(image_path)
#
#         image = np.array(Image.open(image_path).convert("RGB"))
#         print(image.shape)
#         image_list.append(image)
#     tmp.predict(image_list)

        
        
