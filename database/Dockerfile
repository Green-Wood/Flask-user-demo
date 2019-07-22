FROM postgres:latest
WORKDIR /usr/app
COPY ./database.sql /.
RUN psql -U postgres -d postgres -a -f database.sql