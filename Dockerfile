FROM python:3.6-alpine

# Copy dependencies/configurations
RUN mkdir -p /app

WORKDIR /app

COPY . /app/

RUN cd /app \
&& pip3 install -r requirements.txt

# Define the url as the healthcheck
CMD ["python", "test.py"]