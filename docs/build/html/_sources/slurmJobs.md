# The Slurm Workload Manager
Slurm is an open-source load management software that is commonly used by HPC facilities. With Slurm, you can specify the resources your job will use and the partition it will use. HPCs typically use a workload manager so that users use an appropriate amount of resources and as a way to equitably distribute these resources amongst users. 

*Adapted from [https://rc.partners.org/kb/research/computational-resources/erisxdl?article=3719](https://rc.partners.org/kb/research/computational-resources/erisxdl?article=3719)*
## Partitions on ERISXdl
ERISXdl has partitions that you submit to based on the length of your job. Here is a quick summary, but the available partitions can be found using `sinfo`.

| Partion | GPU Limit | Max Time Limit | Memory Limit|
| ---- | ----- | ----- | -------|
Basic (Free tier) |  	8 GPU| 	10 min| 	400G|
Short |  	8 GPU| 	2 hour| 	400G|
Medium |  	8 GPU| 	1 day| 	400G|
Long  | 	8 GPU |	5 days| 	400G|
Mammoth |  	8 GPU| 	2 weeks|	400G |

## Slurm and Slurm-Adjacent Commands
| Action | Tag |
| ------ | ------- |
|Job Name   	| --job-name=My-Job_Name|
|Wall time hours  	| --time=24:0:0   or -t[days-hh:min:sec]|
|Number of nodes   	| --nodes=1|
|Number of proc per node   	| --ntasks-per-node=24|
|Number of cores per task   	| --cpus-per-task=24|
|Number of GPU 	| --gpus=3|
|Send mail at end of the job 	| --mail-type=end|
|User's email address   	| --mail-user=userid@mgb.edu|
|Working Directory  	| --workdir=dir-name|
|Job Restart  	| --requeue|
|Share Nodes  	| --shared|
|Dedicated nodes  	| --exclusive|
|Memory Size    	| --mem=[mem |M|G|T] or --mem-per-cpu|
|Account to Charge   	| --account=[account] (*Not required, unless you are associated with |several accounts and need to specify one in particular*)
|Partition 	| --partition=[name]|
|Quality of Service 	| --qos=[name] (*Not required and should be omitted*)|
|Job Arrays    	| --array=[array_spec]|
|Use specific resource  	| --constraint="XXX"|

You can run your job by calling:

`sbatch <script path>`

The commands `sacct` or `squeue` can be used to confirm job status. With `squeue` you can see the status in the `ST` column where:

- `PD` means pending.
- `R` means running.
- `CG` means completing.

You can cancel the job at any time by calling:

`scancel <jobID>`

### Fairshare and GPU Charges
Jobs are subjec to the FairShare algorithm, which can be viewed using:

`sshare -u <userID> -l`

You can view everyone's score using:

`sshare -al`

Remember that it costs money to use the GPU at a rate of $0.01/min per GPU. You can check your personal charges using `charges -u` and your group charges using `charges -g`. 

# Slurm Examples
The sysadmins have helpfully provided us a few ready-made examples. If you are familiar with Slurm, you will still want to look at the submission scripts because there are ERISXdl-specific commands the *must* be used.
## Using a Customized Image
Copy the first example by calling:

`cp -r /data/erisxdl/publicERISXdlDemoCases/case1-GPU $HOME`

Here are the contents of the job script, `jobScriptBasicP.sh`:

```bash
#!/bin/bash

--partition=Basic
--job-name=exampleCase1
--gpus=1
--ntasks=1
--time=00:10:00
--mem=8G
--output=log.%j
--error=logErrors.%j

## This is a comment

## %j is the id for this job

## Set the docker container image to be used in the job runtime.
export KUBE_IMAGE=erisxdl.partners.org/library/cuda:latestWtestProgs

## Set the script to be run within the specified container - this MUST be a separate script
export KUBE_SCRIPT=$SLURM_SUBMIT_DIR/example-script.sh

## Ensure example-script.sh is executable
chmod a+x  $SLURM_SUBMIT_DIR/example-script.sh

# Define group briefcase (this will provide the GID for the user at runtime)
export KUBE_DATA_VOLUME=/data/<your group's briefcase folder>

# Users can also set the following variable to change the timeout in seconds. It’s 600 by default, but might be useful to change for testing.
export KUBE_INIT_TIMEOUT=300

## Required wrapper script. This must be included at the end of the job submission script.
## This wrapper script mounts /data, and your /PHShome directory into the container 
##
srun  /data/erisxdl/kube-slurm/wrappers/kube-slurm-custom-image-job.sh
```

If you are familiar with Slurm, you might note that there are more than just a few basic commands. In fact, most of this has little to do with your script and you're really just exporting a bunch of seemingly strange values. You may notice that a script is run at the bottom called `kube-slurm-custom-image-job.sh`. If you look at this script you'll see that the exported environment variables are being used by this directly. You will just need to change:

`KUBE_IMAGE` to your Harbor image.

`KUBE_DATA_VOLUME` to your briefcase folder, or alternatively just `/data/`.

and

`KUBE_SCRIPT` to direct to your file. `$SLURM_SUBMIT_DIR` will direct to the directory where you called `sbatch` to submit your job.

Here are the contets of `example-script.sh`:

```bash
#!/bin/bash

# Full path name to the location of folder "cudaTestPrograms".
# Please modify the path accordingly:
cd ~/case1-GPU/cudaTestPrograms


echo "*** Test program compilation ***" 
nvcc vector_add_grid.cu -o vector_add_grid

which vector_add_grid

echo "*** Test program iteration: start***" 

# Loop a number of times 
for i in {1..50}
do
   echo "Iteration $i"
   ./vector_add_grid
done

echo "*** Test program iteration: end***"
```

The contents of the script are not as important, but you should modify the 5th line `cd ~/case1-GPU/cudaTestPrograms` to wherever you stored the example script. 

Finally, run the job:

`sbatch jobScriptBasicP.sh`

## Running a JupyterHub Session
For this example, copy over the second example:
`cp -r /data/erisxdl/publicERISXdlDemoCases/case2-JupyterHub-GPU $HOME`

The job submission script is different this time under the file `jobScriptJupyterHubBasicP.sh`:
```bash
#!/bin/bash

#SBATCH --partition=Basic
#SBATCH --job-name=jupyterHubDemo
#SBATCH --gpus=1
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --mem=8G
#SBATCH --output=log.%j
#SBATCH --error=logErrors.%j

# Base image
export KUBE_IMAGE=erisxdl.partners.org/library/jupyter-minimal-notebook:2023-03-03

# Briefcase path
export KUBE_DATA_VOLUME=/data/<your group's briefcase folder>

# Invoke the Job
srun /data/erisxdl/kube-slurm/wrappers/kube-slurm-jupyter-job.sh
```
Once again we generate environment values for the image and briefcase location. However, our final script is different. If we run the job submission script, we can check the log file and find output similar to:

```
########################################################
Your Jupyter Notebook URL will be: https://erisxdl.partners.org/jupyter/slurm-job-40592?token=980c481b4ce7a73c3ca6843cdb13c296f1450b4e1a4e3430
########################################################
```

```{note}
You may notice that this is a really great way to get a 10 minute (by using the Basic partition) interactive session. You could quickly run through an initial run of your script to see if runs before using money on it!

I haven't played around with this enough yet to know if changing the image has a big effect or not.
```

There are other examples for running proprietary software or RStudio sessions at [https://rc.partners.org/kb/article/3718](https://rc.partners.org/kb/article/3718). 

