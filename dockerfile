FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
  gcc \
  libffi-dev \
  build-essential \
  python3-dev \
  && rm -rf /var/lib/apt/lists/*

# Copy the entire project into the container (including voxelbot directory)
COPY . /app/

# Install the dependencies using pip
RUN pip install .

ENV PYTHONUNBUFFERED=1

CMD [ "python", "-m", "voxelbot", "run" ]
