FROM python:3.8.3

# update packages
RUN apt-get update -y && apt-get upgrade -y && apt-get autoremove && \
    apt-get autoclean && apt-get -y install netcat

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project files
COPY . .

# DATABASE IS COPIED INTO CONTAINER
# TODO: When copying project, ignore node cache + db
# then, makemigration + migrate + createsuperuser + npm i's
#RUN python3.8 manage.py makemigrations
#RUN python3.8 manage.py migrate

# run entrypoint.sh
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]