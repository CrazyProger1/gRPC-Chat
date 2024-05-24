FROM python:3.12.1

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APPNAME=gRPC-Chat

WORKDIR /usr/src/${APPNAME}

COPY . /usr/src/${APPNAME}

RUN pip install -r ./requirements.txt

EXPOSE 50052

RUN chmod +x /usr/src/${APPNAME}/entrypoint.sh

ENTRYPOINT ["/usr/src/gRPC-Chat/entrypoint.sh"]