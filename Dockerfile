FROM python:3.6.8-alpine3.9

COPY . /app
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

WORKDIR /app
RUN apk --update add gcc g++ git nginx postgresql-dev \ 
    # if you don't need postgres, remember to remove postgresql-dev and sqlalchemy
    && pip install --no-cache-dir pipenv \
    && pipenv install --system --deploy \
    && apk del gcc git \
    && rm -rf /tmp/* /var/cache/apk/*

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 8000

CMD nginx && gunicorn -b 127.0.0.1:9000 project.app