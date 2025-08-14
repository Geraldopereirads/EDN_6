import random
import string
import requests


# 1 - Gerador de senha aleatória
def gerar_senha(tamanho: int) -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def senha_interativa():
    qtd = int(input("Digite a quantidade de caracteres da senha: "))
    senha = gerar_senha(qtd)
    print("Senha gerada:", senha)


# 2 - Gerar perfil aleatório (Random User Generator)
def gerar_usuario():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()["results"][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados["email"]
        pais = dados["location"]["country"]
        print(f"Nome: {nome}\nEmail: {email}\nPaís: {pais}")
    else:
        print("Erro ao gerar usuário.")


# 3 - Consulta endereço pelo CEP (ViaCEP)
def consultar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            print("CEP inválido.")
        else:
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
    else:
        print("Erro ao consultar o CEP.")


def cep_interativo():
    cep = input("Digite o CEP (somente números): ").strip()
    consultar_cep(cep)


# 4 - Cotação de moeda (AwesomeAPI)
def consultar_cotacao(moeda: str):
    """Consulta cotação de uma moeda em relação ao Real (BRL)."""
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = moeda + "BRL"
        if chave in dados:
            info = dados[chave]
            print(f"Cotação atual: R$ {info['bid']}")
            print(f"Máximo: R$ {info['high']}")
            print(f"Mínimo: R$ {info['low']}")
            print(f"Última atualização: {info['create_date']}")
        else:
            print("Moeda não encontrada.")
    else:
        print("Erro ao consultar a cotação.")


def cotacao_interativa():
    moeda = input(
        "Digite o código da moeda (ex: USD, EUR, GBP): "
        ).upper().strip()
    consultar_cotacao(moeda)


if __name__ == "__main__":
    print("=== GERADOR DE SENHA ===")
    senha_interativa()

    print("\n=== PERFIL ALEATÓRIO ===")
    gerar_usuario()

    print("\n=== CONSULTA DE CEP ===")
    cep_interativo()

    print("\n=== COTAÇÃO DE MOEDA ===")
    cotacao_interativa()
