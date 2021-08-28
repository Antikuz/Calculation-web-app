FROM debian:latest as builder

# Install requirements for python
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
        python3-dev \
        python3-pip 

COPY ./requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt

    
FROM debian:latest

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
        apache2 \
        libapache2-mod-wsgi-py3 \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

# Copy python requirements from builder
COPY --from=builder /usr/local /usr/local

COPY ./app.conf /etc/apache2/sites-available/app.conf

RUN a2dissite 000-default.conf \
 && a2ensite app

# link apache config to docker logs
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
    ln -sf /proc/self/fd/1 /var/log/apache2/error.log

WORKDIR /var/www/app
COPY . .

CMD  /usr/sbin/apache2ctl -D FOREGROUND
