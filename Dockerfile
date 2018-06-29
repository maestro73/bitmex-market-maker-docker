FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt &&\
marketmaker setup

COPY config/settings-append.py ./config/
RUN cat config/settings-append.py >> settings.py &&\
tail settings.py

COPY custom_strategy.py ./
CMD [ "python", "custom_strategy.py" ]
