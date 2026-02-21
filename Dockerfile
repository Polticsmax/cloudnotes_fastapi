FROM python:3.12-slim


# setting the dir
WORKDIR /app

# intalls python dependencies
COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


# copy the project
COPY . .


#expose port
EXPOSE 8000

#run using gunicorn prod server

CMD ["gunicorn" , "-w" , "2" , "-k" , "uvicorn.workers.UvicornWorker" , "app.main:app" , "--bind" , "0.0.0.0:8000"]
