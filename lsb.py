from PIL import Image

def changeData(data):

		newData = []

		for i in data:
			newData.append(format(ord(i), '08b'))
		return newData

def changePixel(pix, data):

	listData = changeData(data)
	panjangData = len(listData)
	imData = iter(pix)

	for i in range(panjangData):

		pix = [value for value in imData.__next__()[:3] +
								imData.__next__()[:3] +
								imData.__next__()[:3]]

		for j in range(0, 8):
			if (listData[i][j] == '0' and pix[j]% 2 != 0):
				pix[j] -= 1

			elif (listData[i][j] == '1' and pix[j] % 2 == 0):
				if(pix[j] != 0):
					pix[j] -= 1
				else:
					pix[j] += 1

		if (i == panjangData - 1):
			if (pix[-1] % 2 == 0):
				if(pix[-1] != 0):
					pix[-1] -= 1
				else:
					pix[-1] += 1

		else:
			if (pix[-1] % 2 != 0):
				pix[-1] -= 1

		pix = tuple(pix)
		yield pix[0:3]
		yield pix[3:6]
		yield pix[6:9]

def sisipPesan(newPicture, data):
	w = newPicture.size[0]
	(x, y) = (0, 0)

	for pixel in changePixel(newPicture.getdata(), data):

		newPicture.putpixel((x, y), pixel)
		if (x == w - 1):
			x = 0
			y += 1
		else:
			x += 1

def sisip(data, gbr):
	gambar = Image.open(gbr, 'r')

	newPicture = gambar.copy()
	sisipPesan(newPicture, data)

	namaNewPicture = input("Nama file output gambar (dengan ekstensi) : ")
	namaNewPicture = "tempat_gambar/"+namaNewPicture
	newPicture.save(namaNewPicture, str(namaNewPicture.split(".")[1].upper()))

def ekstraksi(gbr):
	gambar = Image.open(gbr, 'r')

	data = ''
	datagambar = iter(gambar.getdata())

	while (True):
		pixels = [value for value in datagambar.__next__()[:3] +
								datagambar.__next__()[:3] +
								datagambar.__next__()[:3]]

		binstr = ''

		for i in pixels[:8]:
			if (i % 2 == 0):
				binstr += '0'
			else:
				binstr += '1'

		data += chr(int(binstr, 2))
		if (pixels[-1] % 2 != 0):
			return data

