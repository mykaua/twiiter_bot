FROM python:2
WORKDIR telegram
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY tel_twi.py ./
COPY twitter_tokens.py ./
COPY tweet.txt ./

CMD ["python", "/telegram/tel_twi.py"]
