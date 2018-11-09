FROM python:3.6-alpine
 
COPY . /crawler
WORKDIR /crawler
 
RUN apk add --update --no-cache g++ gcc libxslt-dev
 
RUN pip install -r requirements.txt
 
CMD ["python","main.py"]