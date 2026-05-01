FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    libeccodes0 \
    libeccodes-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src/ ./src/
COPY config/ ./config/

RUN pip install --no-cache-dir -e .

ENV PYTHONUNBUFFERED=1
ENV MPLBACKEND=Agg

ENTRYPOINT ["gfs-pipeline"]
CMD ["--help"]
