import re

def extrair_dados_fatura(texto):
    valor_total = re.search(r"Total.*?R\$ ?([\d,.]+)", texto, re.IGNORECASE)
    data = re.search(r"Data.*?: ?(\d{2}/\d{2}/\d{4})", texto)

    return {
        "valor_total": valor_total.group(1) if valor_total else None,
        "data": data.group(1) if data else None
    }