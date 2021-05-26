#!/bin/bash
#
#SBATCH --partition=sequana_cpu_shared  
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=24
#SBATCH --time=08:00:00
#SBATCH -J bied
#SBATCH -o logout_bied
#SBATCH --error=err_bied


####SBATCH --nodelist=xxxxxxxxx
##-------exports------------------

export PATH=/bin:$PATH
module load sequana/current

module load python/3.9.1_sequana

module load quantum-espresso/6.7_intel_sequana

export PWROOT=/scratch/app/quantum-espresso/6.7_intel/bin
##-------- modules --------------------------

ulimit -s unlimited
ulimit -a

echo "SLURM_TASKS_PER_NODE    = " $SLURM_TASKS_PER_NODE  
echo "SLURM_NTASKS_PER_CORE   = " $SLURM_NTASKS_PER_CORE
echo "SLURM_NTASKS_PER_NODE   = " $SLURM_NTASKS_PER_NODE
echo "SLURM_NTASKS_PER_SOCKET = " $SLURM_NTASKS_PER_SOCKET
echo "SLURM_JOB_NUM_NODES     = " $SLURM_JOB_NUM_NODES
echo "SLURM_NNODES            = " $SLURM_NNODES
echo "SLURM_CPUS_PER_TASK     = " $SLURM_CPUS_PER_TASK
echo "SLURM_NPROCS            = " $SLURM_NPROCS
echo "SLURM_JOB_NODELIST"=$SLURM_JOB_NODELIST
echo "SLURM_NNODES"=$SLURM_NNODES
echo "SLURMTMPDIR="$SLURMTMPDIR

#################
cd ${SLURM_SUBMIT_DIR}

python sander.py inicio_bied& 

srun -n $SLURM_NPROCS $PWROOT/pw.x < ag977_bi_ed.ads.in > ag977_bi_ed.ads.out

python sander.py final_bied

wait
