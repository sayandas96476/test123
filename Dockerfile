FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["sh", "-c", "nohup python app.py > output.log 2>&1 & tail -f output.log"]
