FROM python:3.9.7-alpine3.14
WORKDIR /app
COPY ./get_dolar_blue.py /app/get_dolar_blue.py
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
ENTRYPOINT ["python3", "/app/get_dolar_blue.py"]