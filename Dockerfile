FROM python:3.12-slim

# ? Setup application directory
COPY src/ /app
COPY dist.env /app/.env
COPY entrypoint.sh pyproject.toml poetry.lock LICENSE.md README.md /app/

# ? Set cwd to app
WORKDIR /app

# ? Setup package management
RUN apt-get update && apt-get install --no-install-suggests --no-install-recommends --yes pipx
ENV PATH="${PATH}:/root/.local/bin"
RUN pipx install poetry

# ? Install dependencies
RUN poetry install

# ? Setting up global app variables
ENV DB_CONFIG_PATH "config/databases.py"
ENV PYTHONPATH "${PYTHONPATH}:/app"

# ? Run app
ENTRYPOINT [ "sh", "entrypoint.sh" ]

# ? Expose app to internet
EXPOSE 80
