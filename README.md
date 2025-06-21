# kmoo

Please review the [LICENSE].

## Development

### Requirements

We will not describe how to install these as there is plenty of documentation already.

* Python 3.13+
* Local Conatiner Environment
  * [Kubernetes]
    * [Docker Desktop] + Kubernetes
    * [Minikube] (MacOS)

### Getting Started

Is best done in a 'nix like environment such as MacOS or Linux.

Clone this repo:

    git clone git@github.com:ianmariano/kmoo.git

A [VENV] should be used to keep things clean. `cd kmeoo` then:

    python3 -m venv --symlinks --without-scm-ignore-files .

Then activate:

    source bin/activate

(To leave the environment: `deactivate`)

Install the requirements:

    pip install -U -r requirements.txt

### Technical notes

* Parsing library for MOO code: [Lark]
* Web Framework: [FastAPI]

[LICENSE]: LICENSE
[Kubernetes]: https://kubernetes.io
[Docker Desktop]: https://docs.docker.com/desktop/
[Minikube]: https://github.com/kubernetes/minikube
[VENV]: https://docs.python.org/3/library/venv.html
[Lark]: https://lark-parser.readthedocs.io/en/stable/
[FastAPI]: https://fastapi.tiangolo.com
