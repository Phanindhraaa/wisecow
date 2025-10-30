FROM ubuntu:22.04

# Install necessary packages: cowsay, fortune, nc
RUN apt-get update && apt-get install -y cowsay fortune netcat

# Set the PATH so /usr/games is in scope for cowsay and fortune
ENV PATH="/usr/games:$PATH"

# Copy your Wisecow bash script into the container
COPY wisecow.sh /wisecow.sh

# Make the script executable
RUN chmod +x /wisecow.sh

# Expose the service port
EXPOSE 4499

# Start the Wisecow application
CMD ["/wisecow.sh"]

