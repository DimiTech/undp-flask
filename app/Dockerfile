FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME ["/usr/src/app"]

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["main.py"]

