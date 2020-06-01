FROM python:3.7-stretch

RUN apt-get update && apt-get install -yq \
    chromium=73.0.3683.75-1~deb9u1 \
    git-core=1:2.11.0-3+deb9u7 \
    xvfb=2:1.19.2-1+deb9u5 \
    xsel=1.2.0-2+b1 \
    unzip=6.0-21+deb9u2 \
    libgconf2-4=3.2.6-4+b1 \
    libncurses5=6.0+20161126-1+deb9u2 \
    libxml2-dev=2.9.4+dfsg1-2.2+deb9u2 \
    libxslt-dev \
    libz-dev \
    xclip=0.12+svn84-4+b1

# chromeDriver v83
RUN wget -q "https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip

# xvfb - X server display
ADD build/worker-base/xvfb-chromium /usr/bin/xvfb-chromium
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome \
    && chmod 777 /usr/bin/xvfb-chromium

# create symlinks to chromedriver and geckodriver (to the PATH)
RUN ln /usr/bin/chromium \
    && chmod 777 /usr/bin/chromium

# install python package requirements
COPY build/worker-base/requirements.txt .
RUN pip install -r requirements.txt

# create project folder and set as workspace
RUN mkdir /app
WORKDIR /app