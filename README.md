# phonic
[![Generic badge](https://img.shields.io/badge/Python-3.7.9-<COLOR>.svg)](https://shields.io/) 
[![Generic badge](https://img.shields.io/badge/TestCoverage-96percent-<COLOR>.svg)](https://shields.io/)

A Flask API that simulates the behavior of an audio file server while using a SQL database.

## Setup Instructions: 

### Clone/Fork Repo
> git clone https://github.com/abhijitpai000/phonic.git

### For Linux:
1. **Create a Python virtual environment**
> python3 -m venv phonic_env

2. **Activate Virtual Environment**
> source phonic_env/bin/activate

3. **Install Project requirements**
> pip install -r requirements.txt

OR

4. **Using Setup.py**
> pip install -e

5. **Setup Flask Configuration & Run.**

> export FLASK_APP=phonic

> export FLASK_ENV=development

> flask run

**Check:** [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


### For Windows:
1. **Create a Python virtual environment**
> python -m venv phonic_env

2. **Activate Virtual Environment**
> .\phonic_env\Scripts\activate

3. **Install Requirements**
> pip install -r requirements.txt

OR

4. **Using Setup.py**
> pip install -e

5. **Setup Flask Configuration & Run.**
> set FLASK_APP=phonic

> set FLASK_ENV=development

> flask run

**Check:** [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## API Usage Guide
* API URI = "/api/audioFileType/audioFileID"
*                 |                 └── Integer
                  └── song, podcast or audiobook

**Example 1: Add a Song to the Database using POST**

```
import requests
import json

url = "http://127.0.0.1:5000/api/song/1"

payload = json.dumps({
  "name": "Song 1",
  "duration": 100
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

**Example 2: Obtain all Songs stored in the Database using GET**
```

import requests
import json

url = "http://127.0.0.1:5000/api/song"

payload = json.dumps({
  "name": "Song 1",
  "duration": 100
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

**Example 3: Change Song 1 name using PUT**
```
import requests
import json

url = "http://127.0.0.1:5000/api/song/1"

payload = json.dumps({
  "name": "Song One",
  "duration": 100
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

**Example 4: Delete Song 1 name using DELETE**
```
import requests
import json

url = "http://127.0.0.1:5000/api/song/1"

payload = json.dumps({
  "name": "Song One",
  "duration": 100
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

```

## Testing:

1. **Run all tests**

> python -m pytest -vv

2. **Run all tests with coverage**

> coverage -m pytest

3. **Generate Coverage Report**
> coverage report

Note: delete the phonic_test_db.sqlite file before Setup 1 always.

## Repository Structure
    .
    └── phonic/                    # phonic application directory.
        ├── __init__.py            # phonic Flask Application Factory.
        ├── audio.py               # API Blueprint with views.
        ├── models.py              # Backend Data Models.
        └── schema.py              # Marshmallow Schema Parser init.
    ├── tests/                     # Automated Test Cases.
        ├── conftest.py            # pytest testing fixtures configuration.
        ├── test_api_delete.py     # Test Cases for DELETE (DELETE Operation) of the API.
        ├── test_api_get.py        # Test Cases for GET (READ Operation) of the API.
        ├── test_api_post.py       # Test Cases for POST (CREATE Operation) of the API.
        ├── test_api_put.py        # Test Cases for PUT (UPDATE Operation) of the API.
        ├── test_database.py       # Test Case for checking if Database file is created.
        └── test_factory.py        # Test Case for checking if Application Factory accepts external configuration.
    ├── setup.cfg                  # Setup Configuration File for testing & development.   
    ├── setup.py                   # Setup file for distribution file generation.
    └── requirements.txt           # Project Requirements
