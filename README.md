# Consulta de CEP

Este projeto é um simples script em Python para consulta de endereço a partir de um CEP utilizando a API do ViaCEP.

## Descrição

O script recebe um CEP (Código de Endereçamento Postal), formata-o removendo caracteres indesejados e, se o CEP for válido,
faz uma requisição para a API do ViaCEP para obter o endereço correspondente.
Se o CEP for inválido (não possuir 8 dígitos após a formatação), o script retorna uma mensagem de erro.

## Requisitos

- Python 3.x
- Biblioteca `requests`

## Instalação

1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Instale a biblioteca `requests` utilizando o seguinte comando:

```bash
pip install requests
```

## Exemplo de saida

```
CEP: 83085-110, Endereço: Rua Exemplo, Bairro: Centro, Cidade: Curitiba, Estado: PR.
```

