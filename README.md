# turingfinance_backend
API escrita em DJANGO para o site TuringFinance.

Python v3.10.6
Pip v23.1.2


## Como executar a aplicação

1. Crie um ambiente virtual: 
```bash
pip install virtualenv
virtualenv venv
```

2. Ative o ambiente virtual:
```bash
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Localize o arquivo `manage.py` e aplique as migrações:
```bash
python3 manage.py makemigrations && python3 manage.py migrate
```

5. Rode o servidor
```bash
python3 manage.py runserver
```

## Estrutura do Projeto

```
.
├── manage.py
├── tfinance_backend/
└── tquant_api/
```

1. **manage.py**: Arquivo principal do projeto, utilizado para rodar comandos Django.
2. **tfinance_backend/** : Pasta principal do projeto, onde ficam as configurações principais.
3. **tquant_api/**: Pasta de uma aplicação Django chamada tquant_api onde estão definidas as views da API relacionada ao _turingquant_.
