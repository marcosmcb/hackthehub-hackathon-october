# Backend

## Installation

In order to run this program, please make sure you execute the following commands:

PS: If you don't have **virtualenv** installed, please follow these instructions [Installing virtualenv via pip](https://virtualenv.pypa.io/en/latest/installation.html#via-pip)

```bash
cd backend # if in the root directory, navigate into the backend one

virtualenv venv
source venv/bin/activate  
pip install -r requirements.txt
```

## How to run it

Once you installed the project dependencies, you can start the API by running:

```sh
uvicorn main:app --reload
```

If uvicorn started successfully, you should see logs similar to the ones below

![](../docs/images/uvicorn-running.jpg)
