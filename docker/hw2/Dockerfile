# public hub
FROM python:3.8

# Копируем файлы с хоста в =>образ=>контейнер(точка стоит)
# При изменении файлов на хосте, в контейнере файлы не изменятся
COPY /test/3.docker/hw2/stocks_products /stocks_products
ENTRYPOINT ["apt update", "apt install python3-pip"]
RUN pip install -r ./stocks_products/requirements.txt
CMD python ./stocks_products/manage.py runserver 0.0.0.0:8000


