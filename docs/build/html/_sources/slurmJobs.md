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
| Action | Command |
| ------ | ------- |
|Job Name   	| #SBATCH --job-name=My-Job_Name|
|Wall time hours  	| #SBATCH --time=24:0:0   or -t[days-hh:min:sec]|
|Number of nodes   	| #SBATCH --nodes=1|
|Number of proc per node   	| #SBATCH --ntasks-per-node=24|
|Number of cores per task   	| #SBATCH --cpus-per-task=24|
|Number of GPU 	| #SBATCH --gpus=3|
|Send mail at end of the job 	| #SBATCH --mail-type=end|
|User's email address   	| #SBATCH --mail-user=userid@mgb.edu|
|Working Directory  	| #SBATCH --workdir=dir-name|
|Job Restart  	| #SBATCH --requeue|
|Share Nodes  	| #SBATCH --shared|
|Dedicated nodes  	| #SBATCH --exclusive|
|Memory Size    	| #SBATCH --mem=[mem |M|G|T] or --mem-per-cpu|
|Account to Charge   	| #SBATCH --account=[account] (*Not required, unless you are associated with |several accounts and need to specify one in particular*)
|Partition 	| #SBATCH --partition=[name]|
|Quality of Service 	| #SBATCH --qos=[name] (*Not required and should be omitted*)|
|Job Arrays    	| #SBATCH --array=[array_spec]|
|Use specific resource  	| #SBATCH --constraint="XXX"|

You can run your job by calling:

`sbatch <script path>`

The commands `sacct` or `squeue` can be used to confirm job status.

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

```
#!/bin/bash

#SBATCH --partition=Basic
#SBATCH --job-name=exampleCase1
#SBATCH --gpus=1
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --mem=8G
#SBATCH --output=log.%j
#SBATCH --error=logErrors.%j

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

```
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

The contents are not as important, but you should modify the line `cd ~/case1-GPU/cudaTestPrograms` to wherever you stored the example script. 