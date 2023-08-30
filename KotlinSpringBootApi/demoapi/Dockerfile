# Use the official image as a parent image
FROM openjdk:21-ea-17-slim-buster

# Set the working directory in docker
WORKDIR /app

# Copy the jar file into the docker image
COPY target/*.jar app.jar

# Set the startup command to execute your binary
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
