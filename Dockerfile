FROM python:3.8
# ENV PYTHONUNBUFFERED 1 ensures that Python output is logged to the terminal, making it possible to monitor Django logs in realtime.
ENV PYTHONUNBUFFERED 1
# ENV PYTHONDONTWRITEBYTECODE 1 prevents Python from copying pyc files to the container.
ENV PYTHONDONTWRITEBYTECODE 1

# create root directory for our project in the container
RUN mkdir /code

# Set the working directory to /code
WORKDIR /code
# Copy the current directory contents into the container at /code
COPY . /code/

# installs and upgrades the pip version that is in the container.
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000
CMD ["python","manage.py","runserver", "0.0.0.0:8000"]