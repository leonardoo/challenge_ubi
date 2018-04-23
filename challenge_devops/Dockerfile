FROM golang:1.9-alpine

RUN apk add --update --no-cache git
RUN go get github.com/julienschmidt/httprouter
RUN go get github.com/rs/cors
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN go build -o challenge_devops
RUN chmod +x ./challenge_devops

EXPOSE 8080

ENTRYPOINT ["./challenge_devops"]