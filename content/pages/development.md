Title: Development
Date: 2026-05-20
Slug: development

A few open-source projects worth a look.

### [portable-argocd](https://github.com/mholzinger/portable-argocd)
An Argo CD API test harness that spins up a disposable kind-based Kubernetes cluster with a full Argo CD install for validating real API behavior. Uncovered (and documents) that the refresh endpoint treats every value except `hard` as cached — a quiet divergence from the docs.

### [reframe](https://github.com/mholzinger/reframe)
Face-recognition photo finder with neighbor expansion — recovers photos of a specific person from large or recovered collections where EXIF and folder structure are gone. Python + Docker, dlib-based, with SQLite caching and parallel workers. Built to run on a Synology NAS.

### [dummypod](https://github.com/mholzinger/dummypod)
A lightweight Flask pod for testing AWS EKS Kubernetes clusters — `/health` and `/metrics` endpoints, Terraform-deployable, designed as a sidekick for blue-green deployments and CI/CD pipelines.
