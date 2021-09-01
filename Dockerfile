FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN apt install && python3 -m pip install --upgrade pip && python3 -m pip install -U requests && python3 -m pip install -U discord.py && python3 -m pip install -U python-dotenv
CMD ["main.py"]
ENTRYPOINT ["python3"]