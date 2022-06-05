FROM python:3

WORKDIR /app

ADD main.py .
ADD jokes.csv .
ADD templates ./templates

RUN python -m pip install --upgrade pip
RUN pip install wheel
RUN pip install flask
EXPOSE 5000

CMD ["python", "main.py"]