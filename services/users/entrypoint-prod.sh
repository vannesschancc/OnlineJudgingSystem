#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z users-db 5432; do
    sleep 01
done 

echo "PostgresSQL started"

gunicorn -b 0.0.0.0:5000 manage:app