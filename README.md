pgbackup
========

CLI for backing up remote PostgreSQL databases locally or to GCP Storage.

## Usage

Pass in a host ip, database name, user, port, the storage driver, and destination.

GCP Storage Example with bucket name as the destination:

```
$ pgbackup -host 18.255.255.255 -database sample -user demo -port 80 --driver googlestorage python-pgbackup
```

Local Example with local path as the destination:

```
$ pgbackup -host 18.255.255.255 -database sample -user demo -port 80 --driver local ./local-dump.sql
```

## Installation From Source

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:

```
$ pip install -e .
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone git@github.com:Aniket02/pgbackup`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`