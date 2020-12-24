#%%
import os

import numpy as np
from PIL import Image

from usf_oncho.pyradar_isodata import isodata_classification

directory = '/home/daric/dev/data/worldview/cameroon/APMQ9125_2/Area3_3-12-2017_SPOT_Ortho_ColorBalance'
tif = 'Area3_3-12-2017_SPOT_Ortho_ColorBalance.tif'
#directory = '/home/daric/dev/data/worldview/cameroon/Area1_Ortho_Mosaic_ColorBalance_1'
#tif = 'Area1_Ortho_Mosaic_ColorBalance.tif'
Image.MAX_IMAGE_PIXELS = None
image = Image.open(os.path.join(directory, tif)).convert('L')
img = np.array(image)

class_map = isodata_classification(img, k=20)

from spectral import imshow

imshow(classes=class_map, figsize=(100, 100))
#%%