FROM python:3.13-alpine3.21

WORKDIR /kmoo

RUN addgroup -g 1000 kmoo \
    && adduser -D -u 1000 -G kmoo kmoo

COPY requirements.txt /kmoo/
COPY backend/ /kmoo/

RUN pip3 install --no-cache-dir -r /kmoo/requirements.txt \
    && chown -R kmoo:kmoo /kmoo

ENV PYTHONPATH=/kmoo

USER kmoo

CMD ["fastapi", "run", "/kmoo/main.py", "--port", "80" ]
