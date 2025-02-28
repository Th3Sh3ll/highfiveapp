FROM python:alpine3.19

COPY . /HighFiveApp

WORKDIR /HighFiveApp

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["./startApp.sh"]