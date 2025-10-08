import requests

def fazer_requisicao(url:str) -> str:
    resultado = requests.get(url)
    return resultado

if __name__ == "__main__":
    url = "https://google.com"
    resultado = fazer_requisicao(url)