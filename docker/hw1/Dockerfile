# public hub
FROM nginx:latest
# Копируем файлы с хоста в =>образ=>контейнер
# При изменении файлов на хосте, в контейнере файлы не изменятся
COPY ./hw1/static/index.html /usr/share/nginx/html/index.html
