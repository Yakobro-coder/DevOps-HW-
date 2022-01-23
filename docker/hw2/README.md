####1. Собираем образ по "Dockerfile" из текущей директории
`docker build -t serv_nginx .`  
######Имя образа - _serv_nginx_
####2. Запускаем контейнер с образа
`docker run --name my_nginx -d -p 80:80 serv_nginx`
######Имя контейнера - _my_nginx_

------

**Доп.Ифо**  
Так как по командам из _Dockerfile_ файлы копируются с хоста 
в образ и более их изменить с хоста нельзя, есть альтернатива  

`docker run --name my_nginx -d -v ./hw1/static/index.html:/usr/share/nginx/html/index.html -p 80:80 serv_nginx`  

После чего любые изменения сделаные на хосте, повлеяют на работу контейнера.