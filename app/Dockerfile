FROM tv_env

WORKDIR /usr/src/app

COPY . .
EXPOSE 8080
CMD [ "gunicorn", "--bind", "0.0.0.0:8080","wsgi:app" ]
