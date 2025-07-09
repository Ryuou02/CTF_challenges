FROM python:3.11-slim-buster

WORKDIR /app

RUN pip3 install flask

COPY . .

EXPOSE 5000

ENV flag "flag{Th!s_1s_l444Ast}"

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]