FROM alpine:latest
RUN apk add --no-cache g++
WORKDIR /app
COPY . /app
RUN g++ -o solve solve.cpp
ENTRYPOINT ["./solve"]
