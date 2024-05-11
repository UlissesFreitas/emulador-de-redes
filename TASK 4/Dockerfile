FROM python:3.9

COPY . .

RUN pip install -r req.txt

EXPOSE 8000

WORKDIR /Entrega

ENTRYPOINT ["gunicorn"]
CMD ["main:myapp"]
