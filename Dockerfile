FROM python:3.11.14-alpine3.23
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "server.py"]
