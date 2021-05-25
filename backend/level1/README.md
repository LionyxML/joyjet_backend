# level 1 - Python Backend

# PT
Uma API escrita em Python/Flask para o Desafio JoyJet.

Com base em um POST JSON como o encontrado em rules/data.json , retorna uma resposta semelhante à rules/output.json.

Basicamente calcula o preço de cada item e totaliza cada carrinho.


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


# EN
An API written in Python / Flask for the JoyJet Challenge.

Client should do a JSON POST like the one found in rules/data.json, the API then will
return a response similar to the rules/output.json file.

Basically calculates the price of each item and totals each cart.


## Install
Clone, download or copy this repository.

All commands must be issued from the project's root folder.

Install the dependencies with:
```
pip3 install requirements.txt
```

Run the application with:
```
flask run
```

By default the application will be served on localhost (127.0.0.1) on the port
5000. This port number, the Debug mode and the environment used can be configured in the .flaskenv file


## Usage
Make a JSON post in the format found in rules / data.json, using a POST method at the URL:
```
localhost:5000/
```

A response will be returned with the total for each shopping cart.

## Testing
A test routine has been implemented that can be customized to include more complex tests of the application.

You may run the tests using:
```
python3 tests.py
```
