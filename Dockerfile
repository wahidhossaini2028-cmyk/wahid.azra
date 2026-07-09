FROM python:3.9-slim
WORKDIR /APP
COPY  . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "bot.py"]
