**Steps**

1. Log in to your IGX Orin Machine

2. Create `mlperf_data` directory in the home directory and then export the data environment variable to this location

```
export MLPERF_SCRATCH_PATH=/home/nvidia/mlperf_data/
```

Create empty directories:

```
mkdir $MLPERF_SCRATCH_PATH/data $MLPERF_SCRATCH_PATH/models $MLPERF_SCRATCH_PATH/preprocessed_data
```

3. Launch the container (this assumes that you have access to Holoscan NGC container, if not follow steps here: https://docs.nvidia.com/launchpad/ai/base-command-coe/latest/bc-coe-docker-basics-step-02.html)

**clone this repo and go inside the NVIDIA directory**
```
git clone git@github.com:sohamm17/inference_results_v3.1.git
cd inference_results_v3.1/closed/NVIDIA
```

**launch the container:**
```
SKIP_DRIVER_CHECK=1 EXTERNAL_USER=1 PARTNER_DROP=0 OUTSIDE_MLPINF_ENV=1 make prebuild IS_SOC=1 SOC_SM=87 DOCKER_ARGS="--security-opt systempaths=unconfined"
```

Run the following commands to link all the directories inside the container (this needs to be done every time you are outside the container): 

```
$ echo $MLPERF_SCRATCH_PATH
$ ls -al $MLPERF_SCRATCH_PATH
$ make clean
$ make link_dirs
$ ls -al build/  # You should see output like the following:
total 8
drwxrwxr-x  2 user group 4096 Jun 24 18:49 .
drwxrwxr-x 15 user group 4096 Jun 24 18:49 ..
lrwxrwxrwx  1 user group   35 Jun 24 18:49 data -> $MLPERF_SCRATCH_PATH/data
lrwxrwxrwx  1 user group   37 Jun 24 18:49 models -> $MLPERF_SCRATCH_PATH/models
lrwxrwxrwx  1 user group   48 Jun 24 18:49 preprocessed_data -> $MLPERF_SCRATCH_PATH/preprocessed_data
```

4. Build the code

```
SKIP_DRIVER_CHECK=1 EXTERNAL_USER=1 PARTNER_DROP=0 make build BENCHMARKS="resnet50 retinanet" IS_SOC=1 SOC_SM=87
```

5. Download datasets

`resnet50` download is a manual process
`ResNet50`: Download the ImageNet 2012 Validation Set and unzip the files to `$MLPERF_SCRATCH_PATH/data/imagenet/`

`retinanet` can be downloaded via the following script
```
Inside the container:
SKIP_DRIVER_CHECK=1 EXTERNAL_USER=1 PARTNER_DROP=0 make download_data IS_SOC=1 SOC_SM=87 BENCHMARKS="retinanet"
```

6. Download Models

```
SKIP_DRIVER_CHECK=1 EXTERNAL_USER=1 PARTNER_DROP=0 make download_model BENCHMARKS="resnet50 retinanet" IS_SOC=1 SOC_SM=87
```

7. Preprocess Data

```
SKIP_DRIVER_CHECK=1 EXTERNAL_USER=1 PARTNER_DROP=0 make preprocess_data BENCHMARKS="resnet50 retinanet" IS_SOC=1 SOC_SM=87
```

8. Run the benchmarks

For a quick run of the benchmarks:
```
make run RUN_ARGS="--benchmarks=resnet50,retinanet --scenarios=singlestream --fast" IS_SOC=1 SOC_SM=87
```

The above command is the combination of the following two steps:

```
make generate_engines RUN_ARGS="--benchmarks=resnet50,retinanet --scenarios=singlestream --fast" IS_SOC=1 SOC_SM=87
make run_harness RUN_ARGS="--benchmarks=resnet50,retinanet --scenarios=singlestream --fast" IS_SOC=1 SOC_SM=87
```

You can remove `--fast` variable to get the full benchmark.
