FROM python:3.8-slim-buster
RUN pip3 install json2xml
RUN pip3 install cryptography
WORKDIR /home
COPY decryptxml.py ./
CMD ["python3", "decryptxml.py"]