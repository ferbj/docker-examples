FROM ubuntu
WORKDIR /app
# Install Nginx
RUN apt-get -y update && apt-get -y install nginx
COPY . .
COPY ./nginx.conf /etc/nginx/nginx.conf

# Expose the port for access
EXPOSE 8080

# Run the Nginx server
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]