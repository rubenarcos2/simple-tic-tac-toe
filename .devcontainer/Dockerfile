FROM python:3.9-slim

# Install basic tools
RUN apt-get update && apt-get install -y bash-completion git git-core curl nano
RUN rm /etc/apt/apt.conf.d/docker-clean

SHELL ["/bin/bash", "-c"]

# enable bash completion
RUN git clone --depth=1 https://github.com/Bash-it/bash-it.git ~/.bash_it && \
    ~/.bash_it/install.sh --silent && \
    rm ~/.bashrc.bak && \
    echo "source /usr/share/bash-completion/bash_completion" >> ~/.bashrc && \
    bash -i -c "bash-it enable completion git"

# cool terminal
RUN git clone --depth 1 https://github.com/b4b4r07/enhancd.git ~/.enhancd && \
    echo "source ~/.enhancd/init.sh" >> ~/.bashrc

# install python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt