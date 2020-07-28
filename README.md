# Populate local elastic search script

Populate local elastic search from json

## Getting Started

### Prerequisites

Python > v.3.7.4

### Installing

After clone.

Create virtual environment inside project folder.

```
python -m venv venv
```

Activate virtual env in Windows cmd.exe

```
venv\Scripts\activate.bat
```

Activate virtual env in Linux bash

```
venv/bin/activate
```

After activate virtual env, install dependecies with pip.

```
pip install -r requirements.txt
```

## Configuration

Change the variables inside the file for your values.

```python
file_name = 'example.json' #json file name
elasticsearch_index_to_insert = 'crm_fac' #elastic search index name
id_field = 'id' #id field from file to use as id in elastic search document
```
## Running it

```
python indexBulkInEls.py
```

