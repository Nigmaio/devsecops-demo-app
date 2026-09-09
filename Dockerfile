FROM python:3.12-slim
WORKDIR /app
COPY hello.py .
CMD ["python", "hello.py"]
RUN apt-get update && apt-get install -y python3-tk
