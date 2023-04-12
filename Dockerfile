FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt

# install the dependencies and packages in the requirements file
WORKDIR /app
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]
CMD ["app.py" ]