FROM python:3.9-slim
WORKDIR /aPP
COPY  . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "bot.py"]
