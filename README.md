# nuwest
NNSA-University Workshop on Exascale Simulation Technologies (NUWEST)

## Docker images
The [Dockerfile](https://https://docs.docker.com/engine/reference/builder/) can be used to build a [Docker](https://www.docker.com/) image containing the Merge and Parsl hands on tutorial code. The image contains all of the dependencies needed to run any of these codes. To build the Docker image:

```bash
docker build -t nuwest:1.0 .
```

and to run the image:

```bash
docker run -p 8888:8888 nuwest:1.0
```

then cut and paste the link from your terminal into a browser.
