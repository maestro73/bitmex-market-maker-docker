FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt &&\
	  marketmaker setup

COPY settings.py ./

CMD [ "marketmaker" ]
