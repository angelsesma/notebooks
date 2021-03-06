data_path = "REPLACE/WITH/_PATH_/TO/IMAGE/FOLDER" #@param
output_res = 256 #@param {type:'number'}
import numpy as np
from PIL import Image, ImageOps
from tqdm import tqdm
import os 
import time
image_channels=3
for filename in tqdm(os.listdir(data_path)):
      path = os.path.join(data_path,filename)
      image = Image.open(path).convert('RGB').resize((output_res, output_res),Image.ANTIALIAS)
      image_22 = image.rotate(22)
      image_45 = image.rotate(45)
      image_90 = image.rotate(90)
      image_bw = image.convert('L')
      image_cw = image_bw.convert('1')
      im_sol130 = ImageOps.solarize(image, threshold =130) 
      im_sol170 = ImageOps.solarize(image, threshold =170)
      im_sol110 = ImageOps.solarize(image, threshold =110)
      im_sol70 = ImageOps.solarize(image, threshold =70)
      im_sol10 = ImageOps.solarize(image, threshold =10)
      im_sol10 = im_sol10.save(f"{data_path}/{int(time.time()) }_s1.png")
      im_sol70 = im_sol70.save(f"{data_path}/{int(time.time()) }_s7.png")
      im_sol110 = im_sol130.save(f"{data_path}/{int(time.time()) }_s11.png")
      im_sol170 = im_sol130.save(f"{data_path}/{int(time.time()) }_s17.png")
      im_sol130 = im_sol130.save(f"{data_path}/{int(time.time()) }_s13.png")
      image_cw = image_cw.save(f"{data_path}/{int(time.time()) }_cw.png")
      image_bw = image_bw.save(f"{data_path}/{int(time.time()) }_bw.png")
      image_90 = image_90.save(f"{data_path}/{int(time.time()) }_90.png")
      image_45 = image_45.save(f"{data_path}/{int(time.time()) }_45.png")
      image_22 = image_22.save(f"{data_path}/{int(time.time()) }_22.png")
      image = image.save(f"{data_path}/{int(time.time()) }_.png")
      os.remove(path)