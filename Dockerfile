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

WORKDIR /docker-for-http
# Remove python source
RUN rm -rf /tmp/Python-3.5.0.tar.xz /tmp/Python-3.5.0


ADD requirements.txt /docker-for-http/requirements.txt
ADD httpapi.py /docker-for-http/httpapi.py
ADD test_users_api.py /docker-for-http/test_users_api.py

RUN pip3 install -r requirements.txt
CMD ["mongod"]
CMD ["python3 httpapy.py"]

