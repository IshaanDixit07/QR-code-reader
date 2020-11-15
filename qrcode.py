import pyqrcode

qr = pyqrcode.create('https://lichess.org/')
qr.png('abcde.png', scale=8)

