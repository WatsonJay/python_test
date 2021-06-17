# -*- coding: utf8 -*-
#最低位的亲吻
from PIL import Image

def foo():
	im=Image.open('20191213101808.bmp')
	im2=im.copy()

	pix=im2.load()
	width,height=im2.size

	for x in range(0,width):
		for y in range(0,height):
			#LSB
			if pix[x,y]&0x1==0:
				pix[x,y]=0 #黑
			else:
				pix[x,y]=255
	im2.show()
	pass

if __name__ == '__main__':
	foo()
	print('ok')
	pass
