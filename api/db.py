import psycopg2
import os

conn = psycopg2.connect(
    host="localhost",
    database="jobpulse_db",
    user="jobpulse",
    password="jobpulse"
)

cursor = conn.cursor()