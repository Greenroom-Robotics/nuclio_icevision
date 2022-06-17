# Nuclio Icevision

This repo builds a base image [ghcr.io/greenroom-robotics/nuclio_icevision:latest](https://github.com/Greenroom-Robotics/nuclio_icevision/pkgs/container/nuclio_icevision) which is used to conveniently run icevision Object Detection models in Nuclio / CVAT. It allows you to configure the model `checkpoint_path` from your nuclio `function.yml`

## Usage

* Use [icevision-from-checkpoint](./example/icevision-from-checkpoint) as a reference example
* Modify/create your own as you see fit. Note the `checkpoint_path`
* Deploy it:
```bash
nuctl deploy --project-name cvat \
  --path example/icevision-from-checkpoint \
  --platform local
```


## Development

### Get started

In order to develop you'll want a nuclio instance running on your local machine...

* `docker-compose up` to start nuclio.
* `./scripts/build.sh` to build `ghcr.io/greenroom-robotics/nuclio_icevision:latest`
* Deploy the example to your nuclio instance:

```bash
nuctl deploy --project-name cvat \
  --path example/icevision-from-checkpoint \
  --platform local
```

### Run tests

* `./scripts/build.sh && docker run ghcr.io/greenroom-robotics/nuclio_icevision:latest` to build and run pytests

### Release a version

* Run the [Release](./.github/workflows/release.yml) workflow on github