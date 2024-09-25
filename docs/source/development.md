# Using Containers
If you want to run code in a reproducible, easy to share environment, Docker containers and images are excellent vehicles for running this code. Briefly and non-technically, running a Docker container is like running a computationally inexpensive isolated computer inside of your computer. The instructions for making the container come from the image. For more information on Docker containers and images, check out [this article from AWS](https://aws.amazon.com/compare/the-difference-between-docker-images-and-containers/). For a brief primer on making your own Docker images, check out [this article from TACC](https://containers-at-tacc.readthedocs.io/en/latest/containerize-your-code/overview.html). 


## Podman and Harbor
*Adapted from [https://rc.partners.org/kb/article/3718](https://rc.partners.org/kb/article/3718)*

Docker can be extremely [insecure and dangerous to run](https://docs.docker.com/engine/security/). So exercise caution when pulling a new Docker image. Because of this, ERISXdl uses a tools called [podman](https://podman.io/). Other groups use apptainer/singularity as well. For our purposes, these are virtually the same as Docker as we are not concerned with root access. 

Harbor is a private container registry used by ERISXdl that you can use to push images. Harbor is used because ERISXdl is not connected to the internet. 


# Submitting Jobs