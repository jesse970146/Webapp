FROM python:3.9
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD [ "/bin/sh", "docker-entrypoint.sh"]