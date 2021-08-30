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
 && echo "$USERNAME ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USERNAME \
 && touch /var/log/auth.log

USER $USERNAME

RUN mkdir /home/$USERNAME/.ssh
COPY ./keys/id_rsa.pub /home/$USERNAME/.ssh/authorized_keys
RUN sudo chown -R $USERNAME:$USERNAME /home/$USERNAME/.ssh/ && \
    sudo chmod 600 /home/$USERNAME/.ssh/authorized_keys

CMD sudo service ssh start && tail -f /var/log/auth.log
