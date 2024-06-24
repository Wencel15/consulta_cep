import requests


cep = "83.085-110"
cep = cep.replace(".", "").replace("-", "").replace(" ", "") # Tratar as informações adicionadas, retirando caracteres indesejados.

if len(cep) == 8: # Verifica se a informação contem 8 caracteres.
    link = f'https://viacep.com.br/ws/{cep}/json/' # Link para pesquisa do CEP.
    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()
    cep = dic_requisicao['cep']
    rua = dic_requisicao['logradouro']
    bairro = dic_requisicao['bairro']
    cidade = dic_requisicao['localidade']
    uf = dic_requisicao['uf']
    print(f'CEP: {cep}, Endereço: {rua}, Bairro: {bairro}, Cidade: {cidade}, Estado: {uf}.')
else:

    print("CEP invalido")   
