from barcode import EAN13
from barcode.writer import ImageWriter

#Construção do Código de barras
with open (r'barcode.png', 'wb')as f:
    EAN13('1536954861', writer=ImageWriter()).write(f)