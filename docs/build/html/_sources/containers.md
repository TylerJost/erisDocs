<!-- # Using Containers -->
If you want to run code in a reproducible, easy to share environment, Docker containers and images are excellent vehicles for running this code. Briefly and non-technically, running a Docker container is like running a computationally inexpensive isolated computer inside of your computer. The instructions for making the container come from the image. For more information on Docker containers and images, check out [this article from AWS](https://aws.amazon.com/compare/the-difference-between-docker-images-and-containers/). For a brief primer on making your own Docker images, check out [this article from TACC](https://containers-at-tacc.readthedocs.io/en/latest/containerize-your-code/overview.html). 


## Podman and Harbor
```{important}
A lot of the official documentation is __very__ loose with the terms container and image. When you are on ERISXdl, the end point is building an image which will in turn make a container that runs your code. Remember that images are templates for building containers. This might seem pedantic but is important when communicating to other technical people and important for not confusing new users. As a general rule:

✅ You can push and pull a docker image and use it to make a container. 

❌ You can't push and pull a docker container, but you can use it to run code.
```

ERISXdl uses two services called podman and Harbor. Podman is used because it provides extra security. For all intents and purposes, its syntax is largely interchangeable with docker's commands.

Harbor is a private container registry used by ERISXdl that you can use to push images. Harbor is used because ERISXdl is not connected to the internet but you will still want to access images.

When you submit your job, you will specify the image you want by using a Harbor location. A wrapper script will be run that spins up a container using this image, then subsequently runs your job in that container. With podman/docker on the command line, Harbor will be referred to as erisxdl.partners.org. 

*Adapted from [https://rc.partners.org/kb/article/3718](https://rc.partners.org/kb/article/3718)*
### Pulling an Existing Image
Docker can be extremely [insecure and dangerous to run](https://docs.docker.com/engine/security/). So exercise caution when pulling a new Docker image, especially if you are on your personal machine and not using podman.

Let's practice using podman by grabbing an image, tagging it, then uploading it to Harbor.

1. Login to the registry you want to use:

    You can use dockerhub directly:

    `podman login docker.io`

    or use Harbor: 

    `podman login erisxdl.partners.org`

    Remember: erisxdl.partners.org == Harbor

2. Search for an image (in this case a lightweight Linux distribution, Alpine Linux):

    `podman search docker.io/alpine`

3. Pull the image

    `podman pull docker.io/library/alpine`

    We can view the image with `podman images` or `podman image ls`. It will look something like this:
    
    ```bash
    REPOSITORY                 TAG      IMAGE ID       CREATED       SIZE
    docker.io/library/alpine   latest   91ef0af61f39   2 weeks ago   8.09 MB
    ```

4. Tag the image:

    `podman tag 91ef0af61f39 erisxdl.partners.org/<PAS Group Name in lowercase>/alpine:demo-copy`

    Notice that we are specifying our image using its `IMAGE ID` and specifying Harbor as the registry.

5.  Push the image to Harbor

    `podman push erisxdl.partners.org/<PAS Group Name in lowercase>/alpine:demo-copy`

If you wanted to, you could now use this image for running your code through a submitted job.

### Customizing an Existing Image
If you spin up a container from an image, this gives you root access to the container. This means you could install python, a package manager, etc inside the container. You could then commit these changes to a new image, then upload this to Harbor and use it.

```{warning}
__Author's Note__: Customizing an existing image is an extremely convenient feature. However, other than a record of file changes, there is very little reproducibility in this. It is highly recommended (by me) that you create dockerfiles that generate images you can use.
```
Here is an example for getting a basic Ubuntu image and adding `curl` to it:

1. Pull the container from Harbor:

    `podman pull docker.io/ubuntu:22.04`

    Again we can view the container with `podman images`
    ```text
    REPOSITORY                 TAG     IMAGE ID       CREATED       SIZE
    docker.io/library/ubuntu   22.04   97271d29cb79   2 weeks ago   80.4 MB
    ```
2. Run the container:

    `podman run -it 97271d29cb79 /bin/bash`

    The `-it` flag opens an interactive terminal where you are the root user. Note that we are running the image based on its `IMAGE ID`. 

    Then install curl and verify it's working:
    ```text
    root@54116e44f656:/# apt-get upgrade
    root@54116e44f656:/# apt-get install curl
    root@54116e44f656:/# curl cht.sh/docker
    root@54116e44f656:/# exit
    ```

    Now we have a running container that has both Ubuntu and `curl`. 
3. View the running containers:

    `podman ps -a`

    ```text
    CONTAINER ID  IMAGE                           COMMAND    CREATED         STATUS                    PORTS  NAMES
    1af08557edbe  docker.io/library/ubuntu:22.04  /bin/bash  11 minutes ago  Exited (0) 6 seconds ago         eager_blackburn
    ```

    You might note that containers have both a `CONTAINER ID` and a `NAME`.
4. Commit the container to a new image:

    `podman commit 1af08557edbe erisxdl.partners.org/<PAS Group Name in lowercase>/ubuntu:now-with-curl`

    Our image should be named ubuntu:now-with-curl. 

    Remember: Your tag gives information but it will be hard to keep up with things like versioning and encompassing all changes through a tag alone. 

### Podman Settings
*This comes directly from partners*

On ERISXdl there are three login nodes, erisxdl1, erisxdl2 and erisxdl3 and where each will contain differing collections of locally-stored images stored under

`/erisxdl[1-3]/local/storage`

In order to ensure the user has access to the images on a given node please locate the following file in the home directory

`~/.config/containers/storage.conf`

and make the following change using your favorite text editor: 

`graphroot = "/erisxdl/local/storage/abc123"`

where abc123 corresponds to the userid. By this means podman will operate normally on all 3 login nodes, even in the case of node failure. However, the images available on each node will be different. The image is stored in Harbor at 

`erisxdl.partners.org/<PAS Group Name in lowercase>`

will of course always be available. If there is trouble please submit a request to hpcsupport to run

`sudo ./podman_reset.sh <userID> /erisxdl/local/storage`

Finally, please note that on each of the login nodes erisxdl[1-3] a user will have a quota of 50GB (as of 2024/01) for the storage of local images. The current consumption of storage under 

`/erisxdl[1-3]/local/storage/<userID>`

can be displayed with the following terminal command:

`quota -vs`
