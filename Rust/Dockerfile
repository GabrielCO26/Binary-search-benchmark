FROM rust:alpine
RUN apk add --no-cache build-base
WORKDIR /usr/src/app
COPY solve.rs .
RUN rustc solve.rs
CMD ["./solve"]
