import requests

def search_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url, timeout=5)
    except requests.RequestException:
        print("Erro de conexão.\n")
        return False
    if not response.ok:
        print("Erro na requisição.\n")
        return False
    dados = response.json()
    if "erro" in dados:
        print("CEP não encontrado.\n")
        return False
    print(f"""
=== RESULTADO ===
Cidade: {dados['localidade']}
Estado: {dados['uf']}
Bairro: {dados['bairro']}
Rua: {dados['logradouro']}
""")
    return True

def get_valid_cep(mensagem):
    while True:
        cep = input(mensagem)
        if not cep.isdigit():
            print("Digite apenas números!\n")
            continue
        if len(cep) != 8:
            print("Digite um CEP válido!\n")
            continue
        return cep

def main():
    while True:
        cep = get_valid_cep("Digite o CEP (Apenas números): ")
        found = search_cep(cep)
        if found:
            break

if __name__ == "__main__":
    main()  