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

#### Local Development

Then activate:

    source bin/activate

Install the requirements:

    pip install -U -r requirements.txt

To directly run the server backend:

    fastapi dev backend/main.py

To exit the VENV:

    deactivate

#### Container

    docker build -t kmoo:0.1.0 -t kmoo:latest .

Then you can

    docker run --rm -p 80:80 kmoo:latest

or similar. You should not have a webserver running on your host listening on port 80 or you will need to change the above.

You can then goto http://localhost or http://localhost/docs

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
