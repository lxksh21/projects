#this is a program for creating QR code using Python
import pyqrcode 
from pyqrcode import QRCode 
s = "https://github.com/lxksh21/Python.git"
  
url = pyqrcode.create(s) 
url.svg("myqr.svg", scale = 8) 
