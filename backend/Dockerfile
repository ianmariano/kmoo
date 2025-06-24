FROM python:3.13.5-bookworm

WORKDIR /kmoo

RUN addgroup -g 1000 kmoo \
    && adduser -D -u 1000 -G kmoo kmoo

COPY requirements.txt requirements.txt
COPY main.py /kmoo/main.py
COPY ./common /kmoo/common
COPY ./server /kmoo/server

RUN pipi3nstall --no-cache-dir -r requirements.txt \
    && chown -R kmoo:kmoo /kmoo

ENV PYTHONPATH=/kmoo

USER kmoo

EXPOSE 8000

CMD ["fastapi", "run", "--workers 4", "/kmoo/main.py" ]
