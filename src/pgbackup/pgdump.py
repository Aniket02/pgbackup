import subprocess
import sys
from urllib.parse import urlparse


def dump(host, database, user, port):
    try:
        return subprocess.Popen(['pg_dump', '-h', host, '-d', database, '-U', user, '-p', port], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"ErrorL {err}")
        sys.exit(1)
