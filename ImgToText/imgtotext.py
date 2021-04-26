# =============================================================================
# Converting Image To Text Program
# =============================================================================

#Importing Libarires
import pytesseract as tess
from PIL import Image

#Tesseract location
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while(True):

    print('\n\tPress Enter to Exit\n')
    
    #importing imgage file
    Img = Image.open(input('Enter The Full Path Of Img :'))
    if not Img:
        break
    
    print('\n')
    
    #converting img to text
    text = tess.image_to_string(Img)
    print(text)