from processamento_imagens.ocr import extrair_texto_imagem
from processamento_imagens.utils import extrair_dados_fatura

caminho = r'C:\Users\acsca\Desktop\PROJETOS PYTHON\ProcessImagens\boleto.jpg'
texto = extrair_texto_imagem(caminho)
dados = extrair_dados_fatura(texto)

print("Texto extraído:")
print(texto)
print("\nDados da fatura:")
print(dados)
