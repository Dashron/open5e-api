FROM python:3.11-alpine

RUN mkdir -p /opt/services/open5e-api
WORKDIR /opt/services/open5e-api
# copy our project code

# install our dependencies
RUN pip install pipenv gunicorn
COPY . /opt/services/open5e-api

RUN pipenv install

# migrate the db, load content, and index it
RUN pipenv run python manage.py quicksetup

# Create the self-signed certs for gunicorn.
RUN apk add openssl
RUN pipenv run sh ./scripts/generate_self_signed_cert.sh

#run gunicorn.
CMD ["pipenv", "run", "gunicorn","--certfile=${CERTFILE}", "--keyfile=${KEYFILE}","-b", ":8888", "server.wsgi:application"]
