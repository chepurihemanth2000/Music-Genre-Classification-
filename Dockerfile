FROM python:3.6
USER root
WORKDIR /usr/app
COPY . /usr/app
RUN pip3 install -r requirements.txt
RUN pip3 install ffmpeg
EXPOSE 8000
RUN python3 manage.py migrate
CMD ["python3", "manage.py", "runserver"]

