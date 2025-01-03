# Connect to Postgres database from Python application deployed on Kubernetes

## Description
A brief description of what the project does and who it's for.

## Installation
Instructions on how to install and set up the project.

```bash
# Clone the repository
git clone https://github.com/yourusername/python-db-k8s.git

# Navigate to the project directory
cd python-db-k8s

# Install dependencies
pip install -r requirements.txt
```

## Usage
Instructions on how to use the project.

```bash
# Example command to run the project
python main.py
```

## Deployment to EKS
Steps to deploy the application to Amazon EKS.

1. **Create an EKS Cluster:**
   ```bash
   eksctl create cluster --name my-cluster --region us-west-2
   ```

2. **Configure kubectl:**
   ```bash
   aws eks --region us-west-2 update-kubeconfig --name my-cluster
   ```

3. **Deploy the application:**
   ```bash
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   ```

## Establish PostgreSQL DB Connection in RDS
Steps to establish a PostgreSQL database connection in Amazon RDS.

1. **Create a PostgreSQL DB Instance:**
   - Go to the RDS console.
   - Click on "Create database".
   - Select "PostgreSQL" and configure the instance settings.

2. **Configure Security Group:**
   - Ensure the security group allows inbound traffic on the PostgreSQL port (default 5432).

3. **Connect to the DB:**
   ```python
   import psycopg2

   connection = psycopg2.connect(
       host="your-rds-endpoint",
       database="your-database-name",
       user="your-username",
       password="your-password"
   )
   ```

## Accessibility
Ensure the application is accessible.

**Access the Application:**
   - Retrieve the external IP address of the service.
   - Open a web browser and navigate to the external IP.
     http://<external-ip>

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
