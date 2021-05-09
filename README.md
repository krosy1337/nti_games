# Site for Kruzhok Pro

[figma](https://www.figma.com/file/B3nGRDYaMBErwnZUGKozpQ/KruzhokPro?node-id=0%3A1)

[document](https://docs.google.com/document/d/10g8ZfVCprJ3EHGQp-NmC-LqGDdnqVUIMove23L5TXYk)

[site](https://kr0sy.pythonanywhere.com)


Версия интрепритатора: python-3.8.x или позже.
Чтобы запустить проект необходимо переименовать файл 'env.example' в '.env' и заполнить данные в этом файле


Можно приписать команду в корневой директории проекта: 
`pip3 install -r requirements.txt`

*или установить пакеты вручную:

asgiref==3.3.4<br>
Authlib==0.15.3<br>
certifi==2020.12.5<br>
cffi==1.14.5<br>
chardet==4.0.0<br>
cryptography==3.4.7<br>
Django==3.2.1<br>
djangorestframework==3.12.4<br>
idna==2.10<br>
pycparser==2.20<br>
python-dotenv==0.17.1<br>
pytz==2021.1<br>
requests==2.25.1<br>
sqlparse==0.4.1<br>
typing-extensions==3.10.0.0<br>
urllib3==1.26.4


Чтобы запустить файл на localhost, необходимо прописать команду в терминале, в корневой директории проекта:
`python3 manage.py runserver --insecure`
