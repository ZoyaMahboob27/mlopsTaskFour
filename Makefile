build:
    docker build -t my-ml-model .

run:
    docker run -it -p 5000:5000 my-ml-model

push:
    docker push my-ml-model
