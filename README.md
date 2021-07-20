╔═══╗  
║╔═╗║  
║║─╚╬══╦╗╔╦══╗  
║║╔═╣╔╗║╚╝║║═╣  
║╚╩═║╔╗║║║║║═╣  
╚═══╩╝╚╩╩╩╩══╝  
╔═══╗╔╗───╔╗  
║╔═╗╠╝╚╗─╔╝╚╗  
║╚══╬╗╔╬═╩╗╔╬══╗  
╚══╗║║║║╔╗║║║══╣  
║╚═╝║║╚╣╔╗║╚╬══║  
╚═══╝╚═╩╝╚╩═╩══╝  

[figma](https://www.figma.com/file/B3nGRDYaMBErwnZUGKozpQ/KruzhokPro?node-id=0%3A1)

[document](https://docs.google.com/document/d/10g8ZfVCprJ3EHGQp-NmC-LqGDdnqVUIMove23L5TXYk)

[site](https://kr0sy.pythonanywhere.com)


##### Версия интрепритатора: python-3.8.x или более поздняя.

##### Для начала работы рекомендуется создать папку для проекта и открыть три окна терминала в этой директории

>##### Код для 1 окна терминала:  
`pip3 install virtualenv`  
`virtualenv venv`  
`git clone https://github.com/krosy1337/nti_games.git`  
Необходимо переименовать файл '.env.example' в '.env' и заполнить данные в этом файле  
`pip3 install -r nti_games/requirements.txt `  
`pip3 install virtualenv`  
`python3 nti_games/manage.py collectstatic`  
`python3 nti_games/manage.py migrate`  
Эту команду следует вводить самой последней (когда все команды в другий терминалах уже введены)  
`python3 nti_games/manage.py runserver --insecure`   

>##### Код для 2 окна терминала:  
`sudo apt install redis`   
`sudo apt install redis-server`  
`sudo apt install php-redis`  
`redis-cli`  
`ping`  
Если вывелось `PONG` то можно выйти из интерфса Redis

>##### Код для 3 окна терминала:  
`source venv/bin/activate`   
`cd nti_games/`  
`sudo systemctl enable redis-server`  
`sudo systemctl restart redis-server`  
`celery -A nti_games worker -l info -P threads`  
Если Celery запустился, то можно вернуться к 1 окну терминала  

░░░░░░░█▐▓▓░████▄▄▄█▀▄▓▓▓▌█  
░░░░░▄█▌▀▄▓▓▄▄▄▄▀▀▀▄▓▓▓▓▓▌█  
░░░▄█▀▀▄▓█▓▓▓▓▓▓▓▓▓▓▓▓▀░▓▌█  
░░█▀▄▓▓▓███▓▓▓███▓▓▓▄░░▄▓▐█▌  
░█▌▓▓▓▀▀▓▓▓▓███▓▓▓▓▓▓▓▄▀▓▓▐█  
▐█▐██▐░▄▓▓▓▓▓▀▄░▀▓▓▓▓▓▓▓▓▓▌█▌  
█▌███▓▓▓▓▓▓▓▓▐░░▄▓▓███▓▓▓▄▀▐█  
█▐█▓▀░░▀▓▓▓▓▓▓▓▓▓██████▓▓▓▓▐█  
▌▓▄▌▀░▀░▐▀█▄▓▓██████████▓▓▓▌█▌  
▌▓▓▓▄▄▀▀▓▓▓▀▓▓▓▓▓▓▓▓█▓█▓█▓▓▌█▌  
█▐▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓█▓█▓█▓█▓▓▓▐█  

#### Всё должно получиться, если следовали инструкции
