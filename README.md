# Parsing 
мини-проект: парсинг сайта kijiji

## Usage

склонировать репозиторий командой 
```
https://github.com/monorb514/Parsing.git
```
 
создать виртуальное окружение с помощью [pip](https://pypi.org/project/pip/)
```
python3 -m venv {name_venv}
```
активировать 
```
venv (source <name_venv>/bin/activate)
```
установить все зависимости проекта из req.txt 
```
pip install -r req.txt
```
создать и заполнить файл .env данными о [субд](https://docs.sqlalchemy.org/en/14/dialects/) и [user-agent](https://developer.mozilla.org/ru/docs/Glossary/User_agent)
```
URL=postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>
USER_AGENT=your_user_agent
```


