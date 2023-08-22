#!/bin/bash

# Copy project files to EC2 instance
scp -i /path/to/your/key.pem -r /path/to/your/project user@ec2-instance-ip:/path/on/ec2/

# SSH into the EC2 instance and perform deployment steps
ssh -i /path/to/your/key.pem user@ec2-instance-ip << EOF
    cd /path/on/ec2/
    source venv/bin/activate
    pip install -r requirements.txt
    python app.py  # Start your FastAPI app here
EOF
