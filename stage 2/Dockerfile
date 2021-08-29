FROM debian:latest

ENV USERNAME=ansible

RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install --no-install-recommends -y \
    openssh-server \
    sudo \
    python3-apt\
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash $USERNAME \
 && usermod -aG sudo $USERNAME \
 && touch /var/log/auth.log

USER $USERNAME

RUN mkdir /home/$USERNAME/.ssh
COPY ./keys/id_rsa.pub /home/$USERNAME/.ssh/authorized_keys

CMD  tail -f /var/log/auth.log