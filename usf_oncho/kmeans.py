#%%
from collections import namedtuple
import os

import numpy as np
import PIL
from spectral.image import Image, ImageArray

Params = namedtuple('Params', 'nbands nrows ncols dtype')

directory = '/home/daric/dev/data/worldview/cameroon/APMQ9125_2/Area3_3-12-2017_SPOT_Ortho_ColorBalance'
tif = 'Area3_3-12-2017_SPOT_Ortho_ColorBalance.tif'
#directory = '/home/daric/dev/data/worldview/cameroon/Area1_Ortho_Mosaic_ColorBalance_1'
#tif = 'Area1_Ortho_Mosaic_ColorBalance.tif'
PIL.Image.MAX_IMAGE_PIXELS = None
image = PIL.Image.open(os.path.join(directory, tif))
arr = np.array(image)

params = Params(nbands = arr.shape[2],
                nrows = arr.shape[0],
                ncols = arr.shape[1],
                dtype = arr.dtype)
s_image = Image(params)
s_image.filename = 'who cares'
s_image_array = ImageArray(arr, s_image)

from spectral import kmeans

(m, c) = kmeans(s_image_array, nclusters=20, max_iterations=30)

from spectral import imshow

imshow(classes=m, figsize=(100, 100))

# %%
