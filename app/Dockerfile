FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME ["/usr/src/app"]

EXPOSE 5000

ENV FLASK_APP main.py
ENV FLASK_DEBUG 1

CMD ["flask", "run", "--host=0.0.0.0"]

