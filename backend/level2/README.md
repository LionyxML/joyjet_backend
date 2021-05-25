# level 2 - Python Backend

Uma API escrita em Python/Flask para o Desafio JoyJet.

Com base em um POST JSON como o encontrado em rules/data.json , retorna uma resposta semelhante à rules/output.json.

Basicamente calcula o preço de cada item, adiciona uma taxa de entrega e totaliza cada carrinho.


## Instalação
Crie um clone, baixe ou copie esse repositório.

Todos os comandos devem ser enviados à partir da pasta raiz do projeto.

Instale as dependências com:
```
pip3 install requirements.txt
```

Rode a aplicação com:
```
flask run
```

Por padrão a aplicação será servida em localhost (127.0.0.1) na porta
5000. Essa porta, o modo de Debug e o ambiente utilizado podem ser configurados no arquivo .flaskenv

## Utilização
Faça um post JSON no formato encontrado em rules/data.json, utilizando um método POST na URL:
```
localhost:5000/
```

Será retornado uma resposta com o total de cada carrinho de compras.

## Testes
Foi implementada uma rotina de testes que pode ser alterada para incluir testes mais complexos da aplicação.

Rode os testes com:
```
python3 tests.py
```
