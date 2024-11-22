# Insurance Cost Calculation Service

## How to Use It


### First step:
```
git clone https://github.com/M4inkun/SMIT-test-task.git SMIT-test-task
```
Enter the new directory 
```
cd SMIT-test-task
```
### Second step:

Create a .env file in the project root and add the following environment variables:

- DB_USER=postgres
- DB_PASS=8148
- DB_HOST=db
- DB_PORT=5432
- DB_NAME=SMIT-insurance

### Third step:

Run the project using Docker Compose:
```
docker-compose up --build
```
The application will be available at http://localhost:8000

> [!TIP]
> ## To manage services, use the following commands:
to stop container:
```
docker-compose down
```
to restart and rebuild the container:
```
docker-compose up --build
```

The Project is ready to go now!
