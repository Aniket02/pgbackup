import subprocess
import sys
from urllib.parse import urlparse


def dump(host, database, user, port):
    try:
        return subprocess.Popen(['pg_dump', '-h', host, '-d', database, '-U', user, '-p', port], stdout=subprocess.PIPE, shell=True)
    except OSError as err:
        print(f"ErrorL {err}")
        sys.exit(1)


def dump_file_name(database, timestamp=None):
    if timestamp:
        return f"{database}-{timestamp}.sql"
    else:
        return f"{database}.sql"
