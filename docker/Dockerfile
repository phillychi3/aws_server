FROM python:3.9.1
WORKDIR /app
ADD . /app
RUN pip3 install -r requirements.txt
EXPOSE 80
CMD ["python","./server.py"]