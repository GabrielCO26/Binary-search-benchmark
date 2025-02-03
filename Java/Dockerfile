FROM openjdk
WORKDIR /app
COPY . /app/
RUN javac solve.java
ENTRYPOINT ["java", "solve"]
