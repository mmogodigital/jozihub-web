FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
COPY docker/django/start.sh /app/start.sh
RUN chmod +x start.sh
RUN pip install -r requirements.txt
ADD . /app/
ADD ./docker /docker
ADD ./static /static
RUN chmod +x /docker/django/start.sh
CMD ["/docker/django/start.sh"]

