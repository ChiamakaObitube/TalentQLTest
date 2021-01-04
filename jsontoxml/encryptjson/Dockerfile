FROM python:3.8.5
RUN pip3 install json2xml
RUN pip3 install cryptography
WORKDIR /home
RUN mkdir encryptjson
COPY jsontoxml.py ./
COPY sample.json ./encryptjson
CMD ["python3", "jsontoxml.py"]