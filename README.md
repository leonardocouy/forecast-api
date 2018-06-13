# API

**Status:** WIP (WORK-IN-PROGRESS)

## A Arquitetura

### Entidades

#### Usuário (User)

Terá as informações básicas necessárias e por uma boa prática, sua senha será salva criptografada no banco de dados.

#### Eventos de Previsão do Usuário (UserForecastEvent)

O usuário pode ter **one-to-many** eventos, isto é, ele poderá criar eventos com a data de início e com a data de término deste evento, e também a hora em que ele deseja receber este evento durante sua validação.

- start_at (data e hora do início do evento): A partir de que dia ele deseja receber notificações.
- ends_at (data e hora do término do evento): É opcional, se for nulo, o evento prevalecerá até que seja colocado um término.
- timetable (horário que deseja receber a notificação do evento): Isto é, todo dia durante um evento válido, neste horário, será verificado a previsão do tempo.

#### Endereço do Usuário (Address)

Por definição de um escopo limitado, consideraremos, apenas o CEP que é um valor único e consistente. O CEP pode ser de muitos usuários, desta forma, evitamos inconsistências tais como: nome errado de cidade (béuzonte, bh, belo horizonte e etc), de endereço.

### Serviços de Previsão de Tempo

#### Interface

Para não depender de apenas um serviço, a ideia é usar o padrão **Adapter**, desta forma abstraímos em uma classe o que precisamos que o serviço traga para nossa aplicação e os **Adapters** (adaptadores, melhor rs) de cada serviço de previsão, irá conter sua lógica para trazer o resultado que precisamos.

#### OpenWeatherMapAdapter

WIP

#### YahooWeatherAdapter

WIP

## Como rodar?

### Requisitos
- Python 3.6+
- Virtualenv

### Projeto

1. Instale as dependências (preferencialmente, usando o Virtualenv), encorajo também o uso do docker se necessário.

**e.g.**
```shell
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
2. Execute as migrations do banco

```shell
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
