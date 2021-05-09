# Site for Kruzhok Pro

[figma](https://www.figma.com/file/B3nGRDYaMBErwnZUGKozpQ/KruzhokPro?node-id=0%3A1)

[document](https://docs.google.com/document/d/10g8ZfVCprJ3EHGQp-NmC-LqGDdnqVUIMove23L5TXYk)


>>>Версия интрепритатора: python-3.8.x или позже
>Чтобы запустить проект необходимо переименовать файл 'env.example' в '.env' и заполнить данные в этом файле


Можно приписать команду в корневой директории проекта: 
pip3 install -r requirements.txt

или установить пакеты вручную
---------------список пакетов для установки---------------
asgiref==3.3.4
Authlib==0.15.3
certifi==2020.12.5
cffi==1.14.5
chardet==4.0.0
cryptography==3.4.7
Django==3.2.1
djangorestframework==3.12.4
idna==2.10
pycparser==2.20
python-dotenv==0.17.1
pytz==2021.1
requests==2.25.1
sqlparse==0.4.1
typing-extensions==3.10.0.0
urllib3==1.26.4
-----------------------------------------------------------


Чтобы запустить файл на localhost, необходимо прописать команду в терминале, в корневой директории проекта:
python3 manage.py runserver --insecure
