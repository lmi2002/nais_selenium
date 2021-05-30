FROM ubuntu:18.04
FROM python:3

# Packages for Google Chrome
RUN apt-get update
RUN apt-get install -y  \
    gconf-service \
    libasound2 \
    libatk1.0-0 \
    libcairo2 \
    libcups2 \
    libfontconfig1 \
    libgdk-pixbuf2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libpango-1.0-0 \
    libxss1 \
    fonts-liberation \
    libappindicator1 \
    libnss3 \
    lsb-release \
    xdg-utils \
    libgbm1

# Install Google Chrome
RUN wget https://dhl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt-get remove google-chrome-stable_current_amd64

RUN \
  CHROMEDRIVER_VERSION = curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE && \
  curl -s -o chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION)/chromedriver_linux64.zip && \
  unzip -q chromedriver -d /usr/local/bin && rm chromedriver.zip

WORKDIR /home/lmi/

RUN pip3 install -r ./nais_selenium/requirements.txt

WORKDIR ./nais_selenium/tests

CMD ["pytest", "-m", "first"]