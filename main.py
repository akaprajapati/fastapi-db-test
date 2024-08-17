from fastapi import FastAPI, HTTPException
import psycopg2
from psycopg2 import OperationalError

app = FastAPI()

# Database configuration details (you can adjust these)
DATABASE_HOST = "your_database_host"
DATABASE_PORT = "5432"
DATABASE_NAME = "your_database_name"
DATABASE_USER = "your_database_user"
DATABASE_PASSWORD = "your_database_password"

@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

@app.get("/test-db")
async def test_db():
    try:
        # Try connecting to the database
        connection = psycopg2.connect(
            host=DATABASE_HOST,
            port=DATABASE_PORT,
            dbname=DATABASE_NAME,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 1;")
        connection.close()

        return {"message": "Successfully connected to the database!"}
    
    except OperationalError as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")
