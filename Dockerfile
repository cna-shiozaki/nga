FROM python:3.10-slim-buster

COPY ./ /nga/

WORKDIR /nga/

RUN pip install -r nga/requirements.txt

ENTRYPOINT [ "/bin/sh" ]