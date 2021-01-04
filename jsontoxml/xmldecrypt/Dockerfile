FROM python:3.8.5
RUN pip3 install json2xml
RUN pip3 install cryptography
WORKDIR /home
COPY decryptxml.py ./
EXPOSE 21
CMD ["python3", "decryptxml.py"]