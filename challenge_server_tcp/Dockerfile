FROM rcarmo/alpine-python:3.5-onbuild

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
RUN chmod +x ./entrypoint.sh

EXPOSE 27877
EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]
