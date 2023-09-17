FROM caddy:latest

RUN apk add --no-cache python3 py3-pip

RUN pip install flask
RUN pip install requests

WORKDIR /srv

COPY app/ /srv
COPY Caddyfile /etc/caddy/Caddyfile

COPY bootstrap.sh .
RUN chmod +x bootstrap.sh

ENV SECRET="oh no! you exposed my secrets!"

CMD ["/bin/sh", "/srv/bootstrap.sh"]
