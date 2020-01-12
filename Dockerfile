FROM tiangolo/uvicorn-gunicorn:python3.7

LABEL maintainer="Fuelsave <areis@fuelsave.io>"

### Copy over and install the requirements
COPY ./app/requirements.txt $DIR/
RUN pip install -r $DIR/requirements.txt

COPY ./app /app
