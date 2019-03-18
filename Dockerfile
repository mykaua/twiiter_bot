FROM python:2

WORKDIR telegram

ADD . /telegram/
RUN pip install --no-cache-dir -r requirements.txt

#twitter
ENV consumer_key=xxxxx
ENV consumer_secret=xxxxx
ENV access_token_key=xxxxx
ENV access_token_secret=xxxxx
ENV twitter_user=@user
#telegram
ENV telegram_token=xxxxx

CMD ["python", "/telegram/main.py"]
