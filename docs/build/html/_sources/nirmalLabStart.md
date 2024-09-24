# Preliminary Steps for Nirmal Lab Members

1. First, request an account using this link: [https://rc.partners.org/scic-cluster-account-request](https://rc.partners.org/scic-cluster-account-request)
2. *Requesting an account does not give you access to ERISXdl*. To remedy this, you need to ask Jay Omobono (IT support) at [jomobono@bwh.harvard.edu](jomobono@bwh.harvard.edu) and CC Dr. Nirmal to request access for this machine. 
3. Verify your access to the group by calling `groups` from the command line. 

# System Architecture
*Adapted from https://rc.partners.org/kb/computational-resources/erisxdl?article=3650*

ERIS Scientific Computing has implemented a new deep learning GPU Cluster, ERISXdl (ERIS Extreme Deep Learning). This system is built with NVIDIA DGX-1, an integrated system that includes high-performance GPU interconnects which deliver industry-leading performance for AI and deep learning. The current system includes 5 nodes each containing 8 X NVIDIA Tesla V100 GPUs with an aggregate of more than 200 thousand CUDA cores, 25600 Tensor cores, 1280 GB of GPU memory, and 35TB of local storage for data processing, to allow the user to more quickly train larger models as part of a wider series of experiments.
 
Increased productivity and performance benefits come from the fact that ERISXdl is an integrated and NVIDIA-supported hardware-software system that is tuned for deep learning. This platform is therefore ideal for addressing deeper and more complex neural networks which offer dramatic increases in accuracy but at a cost of longer compute times and increased latency. In general ERISXdl represents a good fit for the requirements of Deep Learning and Neural Network modelling more generally. 
 
ERISXdl platform provides:

- Efficient, high-bandwidth streaming of training data. Each system comes configured with a single 480 GB boot OS SSD, and four 1.92 TB SAS SSDs (7.6 TB total) configured as a RAID 0 striped volume for high-bandwidth performance.
- Multi-gpu and multi-system with GPU performance designed for HPC and Deep Learning applications. Multi-system scaling of Deep Learning computational workloads, both inside the system and between systems, to match the significant GPU performance of each system.
- The system memory capacity is higher than the GPU memory capacity to enable simplified buffer management and balance for deep learning workloads.
- Kubernetes and Docker containerized environments to easily emulate the entire software workflow and maintain portability and reproducibility.
- Jupyter notebooks for rapid development, integration with Github and HPC scheduler Slurm to distribute the workload across the system.
- Access to high-bandwidth, low-latency Briefcase storage (__Authors Note: I'll explain what this is later__).
