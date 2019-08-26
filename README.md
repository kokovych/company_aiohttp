## Simple aiohttp-based project

This project is created with education purpose: get practice experience
with aiohttp.

Used python 3.5+ (3.7), postgres 11. 

#### Preparation

1. Create and activate virtual environment:

```sh 
$ virualenv -p python3 venv
$ source venv/bin/activate
```

2. Install requirements:
```
(venv)$ pip install  -r requirements.text
```

3. Create database and database user:

```
$ psql -U postgres -h localhost
> CREATE DATABASE aiohttp_company;
> CREATE USER aiohttp_company WITH PASSWORD 'aiohttp_company';
> GRANT ALL PRIVILEGES ON DATABASE aiohttp_company TO aiohttp_company;

```

#### Run

For start project:

```
(venv)$ python common/main.py
```

##### Run tests

```
(venv)$ pytest -vs
```

##### Check code style
```
(venv)$ flake8
```
