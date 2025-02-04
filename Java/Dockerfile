FROM openjdk
COPY . /app
WORKDIR /app
RUN javac solve.java
ENTRYPOINT ["java", "solve"]
