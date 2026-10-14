# Project Name

Backend system to ....

# Overview

Explain:

What the project is
What problem it solves
Who it is for
Why it exists

Keep this section concise. A reader should understand the purpose of the project within a few paragraphs.

# Features

# Tech-Stack

Python
uv for dependency management

## Frontend

## Backend

## Database

## Infrastructure

## Other

PODMAN for building containers and runnung containers

# Getting Started

## Pre-Req

1. pip install

   ```
   curl -O https://bootstrap.pypa.io/pip/3.9/get-pip.py
   python3 get-pip.py --user
   ```

1. Podman commands

   Stop podman VM

   ```
   podman machine stop
   ```

   Start podman VM

   ```
   podman machine start
   ```

   ```
   python3 -m pip install --user podman-compose

   ```

   add Python 3.9’s user binaries to your path:

   ```
   echo 'export PATH="$HOME/Library/Python/3.9/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc

   podman-compose --version
   ```

1. UV commands
   Add dependencies to the project using command:

   ```
   uv add fastapi
   ```

   Remove dependencies to the project using command:

   ```
   uv remove requests
   ```

   Update the project env using command:

   ```
   uv sync
   ```

1. Activate the virtual env before dev'ing or running the script:

   ```
   source .venv/bin/activate
   ```

   Alembic commands:

   ```
   alembic upgrade head
   ```

## Installation

## Run the application

Load the docker-compose file using the below command from project root:

```
podman-compose -f docker-compose.yml up -d
```

```
uv run main.py
```

# Testing

# Deployment

# Contact

**Author** : Jay Rajan

- Github: @jayrajan
- Email: jay.rajan27@gmail.com
- Website:

For bugs or feature requests, please open an issue in the repository.
