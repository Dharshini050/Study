# FROM jenkins/jenkins:lts

# # Switch to root to install Docker
# USER root

# # Install Docker in Jenkins container
# RUN apt-get update && apt-get install -y docker.io

# # Allow Jenkins user to use Docker
# RUN usermod -aG docker jenkins

# # Expose Jenkins port
# EXPOSE 8080
FROM jenkins/jenkins:lts

# Switch to root to install Docker
USER root

# Install Docker in Jenkins container
RUN apt-get update && apt-get install -y docker.io

# Allow Jenkins user to use Docker
RUN usermod -aG docker jenkins

# Expose Jenkins port
EXPOSE 8080

# Mount Docker socket
VOLUME /var/run/docker.sock:/var/run/docker.sock

USER jenkins
