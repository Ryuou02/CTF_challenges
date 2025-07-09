FROM python:3.11-slim-buster

WORKDIR /app

RUN pip3 install flask

COPY . .

EXPOSE 5000

ENV flag "flag{test_flag}"

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]