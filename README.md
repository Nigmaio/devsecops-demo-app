# Container Exercise — Day 4

## Goal
Build and run a simple containerised application to practice core Docker workflows: build, run, and inspect.

## Prerequisites
- Docker installed and running
- This repo cloned locally

## Steps

1. Clone (or pull if already cloned):
   git clone "Insert Repo Url"
   cd "Into Repo Folder"

2. Build the image:
   docker build -t hello-app .

3. Run the container:
   docker run hello-app

   You should see: "Congratulations, you ran your first container"

4. Inspect the running container (bonus — try before it exits):
   docker ps
   docker exec -it <container-id> sh

## What just happened?
- `docker build` read the Dockerfile and packaged the app + Python runtime into an image
- `docker run` started a container from that image
- The container ran the script, printed the output, then exited

## Troubleshooting
- "docker: command not found" → Docker isn't installed or isn't running
- Build fails on COPY step → make sure you're running the build command from inside the cloned folder

## Resources
https://docs.docker.com/get-started/tutorials/run-an-app/