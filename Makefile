build:
    docker build -t my-ml-model .

run:
    docker run -it -p 5000:5000 my-ml-model

push:
    docker login  # Log in to your Docker registry
    docker push my-ml-model
