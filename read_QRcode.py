# -*- coding: utf-8 -*

from pyzbar.pyzbar import decode
from PIL import Image

data=decode(Image.open('/home/ilya/Downloads/hlam/ctf/qr_code.png'))
print(len(data))
for i in data:
    for ii in i:
        print(ii)
