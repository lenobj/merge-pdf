# Instructions

You may run the code one of 3 ways:

1. Run the python code (Download at least app.py, requirements.txt, alter input and output folder in the code. Run the code)
2. Build and run the image yourself. (Download the content of the repository)
3. Run docker-compose and alter .env file to point to the folder of your choice.

Should you run with docker-compose, you may modify .env as needed.
Where $PWD is the current directory.

```bash
INPUT_PATH=$PWD/input/
OUTPUT_PATH=$PWD/output/
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
