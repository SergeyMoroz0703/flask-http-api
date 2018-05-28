FROM mongo:3.7-xenial

# Compile python3 
RUN apt-get update && \
    apt-get install -y \
                    wget \
                    xz-utils \
                    build-essential \
                    libsqlite3-dev \
                    libreadline-dev \
                    libssl-dev \
                    screen \
                    openssl
WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tar.xz
RUN tar -xf Python-3.5.0.tar.xz
WORKDIR /tmp/Python-3.5.0
RUN ./configure
RUN make
RUN make install

WORKDIR /flask-http-api
# Remove python source
RUN rm -rf /tmp/Python-3.5.0.tar.xz /tmp/Python-3.5.0


ADD requirements.txt /flask-http-api/requirements.txt
ADD httpapi.py /flask-http-api/httpapi.py
EXPOSE 80

RUN pip3 install -r requirements.txt
CMD ["mongod"]
CMD ["python3","httpapi.py"]

