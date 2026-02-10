# Sistema de gestão de pedidos (teste Brascomm)


# --- Tecnologias e requisitos ---

*Python : 3.12+
*Django: 6.0.2
*Banco de dados: SQLite
*Frontend: HTML5,CSS3 e JavaScript (ES6+)


# Sobre o projeto:

Autenticação via Sessão: Utilizei o sistema nativo do Django, onde o servidor cria um ID da sessão após o login e armazena um cooke no navegador. Marcando com o decorador @login_required já garante aquela rota só pode ser acessada pelo usuário que esta logado

Uso do csrf_exempt : Algumas rotas de API foram marcadas com @csrf_exempt para facilitar testes via Insomnia/Postman sem necessidade de passar o cabeçalho X-CSRFToken.
Tenho total ciência que em um cenário de produção isso não poderia ser feito, utilizei apenas para demonstração.

Fiz paginas simples em HTMl e CSS com pouca estilização para poupar tempo e focar nas funcionalidades

Docker: Como não tenho por hora muita prática com Docker, me permitir usar a IA para gerar o arquivo e facilitar na hora de rodar em suas maquinas 



# Usuario:
    admin
    admin123



# Demo do projeto privado no Youtube (irei retirar do ar em 1 semana)

https://youtu.be/RygzmRooKJ0



# Clonar
    git clone https://github.com/viniciuswilker/projeto-brascomm.git

    cd projeto-brascomm


# Para rodar via DOCKER: 
    docker compose up --build

OU

# AMBIENTE PYTHON:

comandos :
    python -m venv venv

    -Ativar ambiente:
            #Linux
            source venv/bin/activate

            #windows
            venv/scripts/activate


    pip install -r requirements.txt

    python manage.py migrate

    python manage.py seed

    python manage.py runserver

    estará disponível em : http://0.0.0.0:8000/