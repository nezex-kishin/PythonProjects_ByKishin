import cv2
import qrcode

img = qrcode.make(f'{input('Введите инфу в код: ')}')
name = input('Как назвать файл: ')
img.save(f"{name}.png")

qr = cv2.imread(f'{name}.png')
detect = cv2.QRCodeDetector()
value, _, _ = detect.detectAndDecode(qr)
print(value)

