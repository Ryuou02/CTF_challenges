FROM php:8.2-apache

# Set the working directory in the container
WORKDIR /var/www/html

# Copy the current directory contents into the container at /var/www/html
COPY . /var/www/html

# Install required PHP extensions including MySQL driver
RUN apt-get update && \
    apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libzip-dev \
        && docker-php-ext-install -j$(nproc) mysqli pdo_mysql zip
# Expose port 80 to the outside world
EXPOSE 80

# Define environment variables for database connection
ENV DB_HOST sql.freedb.tech
ENV DB_USER freedb_chall2
ENV DB_PASSWORD DDyce!5nhyCYmr&
ENV DB_NAME freedb_challenge

# Apache configurations
RUN a2enmod rewrite

# Start Apache
CMD ["apache2-foreground"]
