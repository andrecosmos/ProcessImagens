import pytesseract
from PIL import Image
import numpy as np
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extrair_texto_imagem(caminho_imagem):
    imagem = cv2.imread(caminho_imagem)

    if imagem is None:
        raise FileNotFoundError(f"Imagem não encontrada no caminho: {caminho_imagem}")

    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    _, imagem_tratada = cv2.threshold(imagem_cinza, 150, 255, cv2.THRESH_BINARY)

    texto = pytesseract.image_to_string(imagem_tratada, lang='por')

    return texto
