FROM nginx:latest

ADD nginx.conf /etc/nginx/nginx.conf

RUN mkdir /static
WORKDIR /static
ADD /static var/www/static/

