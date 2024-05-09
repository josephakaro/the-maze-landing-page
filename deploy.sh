#!/bin/bash

# Install necessary packages
sudo apt-get update
sudo apt-get install -y nginx python3-pip python3-venv

# Create a virtual environment and install Flask and Gunicorn
# python3 -m venv env
source env/bin/activate
pip install flask gunicorn

# Clone your Flask app repository
git clone https://github.com/josephakaro/the-maze.git
cd the-maze

# Install dependencies and set up your Flask app (adjust as needed)
pip install -r requirements.txt
export FLASK_APP=app.py
flask run &  # Start the Flask app as a background process

# Configure Nginx
sudo rm /etc/nginx/sites-enabled/default
sudo touch /etc/nginx/sites-available/the-maze
sudo ln -s /etc/nginx/sites-available/the-maze /etc/nginx/sites-enabled/
sudo tee /etc/nginx/sites-available/the-maze > /dev/null <<EOF
server {
    listen 80;
    server_name themaze.josephakaro.tech;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Test Nginx configuration
sudo nginx -t

# Restart Nginx to apply changes
sudo systemctl restart nginx