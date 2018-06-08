FROM python:3.5


WORKDIR /flask-http-api


ADD requirements.txt /flask-http-api/requirements.txt
ADD httpapi.py /flask-http-api/httpapi.py

RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3","httpapi.py"]
