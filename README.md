# Instructions

Modify config.env as needed.

```bash
INPUT_PATH=input/
OUTPUT_PATH=output/
```

## Docker Build

```bash
DOCKER_BUILDKIT=1 \
docker build \
--squash \
--no-cache \
-t lenobj/merge-pdf .
```

## Docker TAG

```bash
docker tag \
lenobj/merge-pdf \
lenobj/merge-pdf:1.0
```

## Docker Run

```bash
docker run \
-v $PWD/:/app/output \
-v $PWD/input:/app/input \
--name merge \
-id merge-pdf:1.0
```

## Docker Compose

```bash
docker compose up
```

```bash
docker compose down
```
