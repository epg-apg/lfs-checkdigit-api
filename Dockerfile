FROM python:3.11-alpine

COPY ./requirements.txt /app/requirements.txt

# install the dependencies and packages in the requirements file
WORKDIR /app
RUN pip install -r requirements.txt

# install runtime environment
RUN pip install waitress

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
CMD ["waitress-serve", "--call", "lfscheckdigitapi:create_app"]

EXPOSE 8080