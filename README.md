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

3. Launch the container (this assumes that you have access to Holoscan NGC container)

```
SKIP_DRIVER_CHECK=1 EXTERNAL_USER=1 PARTNER_DROP=0 OUTSIDE_MLPINF_ENV=1 make prebuild IS_SOC=1 SOC_SM=87 DOCKER_ARGS="--security-opt systempaths=unconfined"
```

4. Download datasets

`resnet50` download is a manual process
`ResNet50`: Download the ImageNet 2012 Validation Set and unzip the files to `$MLPERF_SCRATCH_PATH/data/imagenet/`

`retinanet` can be downloaded via the following script
```
Inside the container:
SKIP_DRIVER_CHECK=1 EXTERNAL_USER=1 PARTNER_DROP=0 make download_data IS_SOC=1 SOC_SM=87 BENCHMARKS="retinanet"
```

5. Download Models

```
SKIP_DRIVER_CHECK=1 EXTERNAL_USER=1 PARTNER_DROP=0 make download_model BENCHMARKS="resnet50 retinanet" IS_SOC=1 SOC_SM=87
```

6. Build the code

```
SKIP_DRIVER_CHECK=1 EXTERNAL_USER=1 PARTNER_DROP=0 make build BENCHMARKS="resnet50 retinanet" IS_SOC=1 SOC_SM=87
```

7. Run the benchmarks

```
make run_harness RUN_ARGS="--benchmarks=resnet50,retinanet --scenarios=singlestream --fast" IS_SOC=1 SOC_SM=87
```

You can remove `--fast` variable to get the full benchmark.
