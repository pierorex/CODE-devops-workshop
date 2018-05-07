FROM python:3
# Install the required python packages 
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Copy flask app source code to the /app dir on the container
WORKDIR /app/
COPY app/ .
# Start the calculator app when you run this container
CMD ["python", "calculator/app.py"]
