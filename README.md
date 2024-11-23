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

- DB_USER=your_db_user
- DB_PASS=your_db_pass
- DB_HOST=localhost
- DB_PORT=5432
- DB_NAME=your_db_name

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

<br><br>

> [!NOTE]
> If you want to run it locally on your machine, just follow the next instructions:
> 
### install the required dependencies:
```
pip install -r requirements.txt
```
### Create a .env file in the project root and add the following environment variables:

- DB_USER=your_db_user
- DB_PASS=your_db_pass
- DB_HOST=localhost
- DB_PORT=5432
- DB_NAME=your_db_name

> [!WARNING]
> _If you are working on a Windows OS, follow these steps:_
>```
> pip install asyncio aiohttp
>```

### Run the database migration:
```
alembic upgrade head
```

### And finally run the project:
> _From the project's root directory, run the following command:_
> ```
> uvicorn app.main:app
> ```

Thank you!
