# Using Containers
If you want to run code in a reproducible, easy to share environment, Docker containers and images are excellent vehicles for running this code. Briefly and non-technically, running a Docker container is like running a computationally inexpensive isolated computer inside of your computer. The instructions for making the container come from the image. For more information on Docker containers and images, check out [this article from AWS](https://aws.amazon.com/compare/the-difference-between-docker-images-and-containers/). For a brief primer on making your own Docker images, check out [this article from TACC](https://containers-at-tacc.readthedocs.io/en/latest/containerize-your-code/overview.html). 


## Podman and Harbor
```{important}
A lot of the official documentation is __very__ loose with the terms container and image. When you are on ERISXdl, the end point is building an image which will in turn make a container that runs your code. Remember that images are templates for building containers. This might seem pedantic but is important when communicating to other technical people and important for not confusing new users. As a general rule:
✅ You can push and pull a docker image and use it to make a container. 
❌ You can't push and pull a docker container, but you can use it to run code.
```
*Adapted from [https://rc.partners.org/kb/article/3718](https://rc.partners.org/kb/article/3718)*

### Pulling an Existing Image
Docker can be extremely [insecure and dangerous to run](https://docs.docker.com/engine/security/). So exercise caution when pulling a new Docker image. Because of this, ERISXdl uses a tools called [podman](https://podman.io/). Other groups use apptainer/singularity as well. For our purposes, these are virtually the same as Docker as we are not concerned with root access. 

Harbor is a private container registry used by ERISXdl that you can use to push images. Harbor is used because ERISXdl is not connected to the internet but you will still want to access images. Let's practice by grabbing an image, tagging it, then uploading it to Harbor.

1. Login to the registry you want to use:

    You can use dockerhub directly:

    `podman login docker.io`

    or use Harbor: 

    `podman login erisxdl.partners.org`

2. Search for an image (in this case a lightweight Linux distribution, Alpine Linux):

    `podman search docker.io/alpine`

3. Pull the image

    `podman pull docker.io/library/alpine`

    We can view the image with `podman images` or `podman image ls`. It will look something like this:
    
    ```
    REPOSITORY                 TAG      IMAGE ID       CREATED       SIZE
    docker.io/library/alpine   latest   91ef0af61f39   2 weeks ago   8.09 MB
    ```

4. Tag the image:

    `podman tag d4ff818577bc erisxdl.partners.org/<PAS Group Name in lowercase>/alpine:demo-copy`

5.  Push the image to Harbor

    `podman push erisxdl.partners.org/<PAS Group Name in lowercase>/alpine:demo-copy`

If you wanted to, you could use this image for running your code.

### Customizing an Existing Image
If you spin up a container from an image, this gives you root access to the container. This means you could install python, a package manager, etc inside the container. You could then commit these changes to a new image, then upload this to Harbor and use it.

```{warning}
__Author's Note__
Customizing an existing image is an extremely convenient feature. However, other than a record of file changes, there is very little reproducibility in this. It is highly recommended (by me) that you create dockerfiles that generate images you can use.
```
Here is an example of getting a CUDA image from NVIDIA and adding opengl to it:

1. Pull the container from Harbor:
    `podman pull erisxdl.partners.org/abc123/cuda:latest`

    Again we can view the container with `podman images`
    ```
    REPOSITORY                         TAG      IMAGE ID       CREATED       SIZE
    erisxdl.partners.org/abc123/cuda   latest   979cd1f9e2c8   2 weeks ago   4.24 GB
    ```

    Note the image ID.
2. Run the container:
    `podman run -it 979cd1f9e2c8 /bin/bash`

    The `-it` flag opens and interactive terminal and is very common.

    Then install OpenGL:
    ```
    root@54116e44f656:/# apt-get upgrade
    root@54116e44f656:/# apt-get install opengl
    root@54116e44f656:/# exit
    ```

# Submitting Jobs