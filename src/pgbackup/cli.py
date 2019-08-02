from argparse import Action, ArgumentParser


class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination


def create_parser():
    parser = ArgumentParser(description="""
    Back up PostgreSQL databases locally or to GCP storage"
    """)

    parser.add_argument("-host", help="host IP of database server")
    parser.add_argument("-database", help="database name")
    parser.add_argument("-user", help="username")
    parser.add_argument("-port", help="port number")
    parser.add_argument("--driver", '-d',
                        help="how & where to store backup",
                        nargs=2,
                        metavar=("DRIVER","DESTINATION"),
                        action=DriverAction,
                        required=True)
    return parser


def main():
    import time
    from google.cloud import storage
    from pgbackup import pgdump, storage as st

    args = create_parser().parse_args()
    dump = pgdump.dump(args.host, args.database, args.user, args.port)

    if args.driver == 'googlestorage':
        storage_client = storage.Client.from_service_account_json("fastAI-c0782c1262dd.json")
        timestamp = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        file_name = pgdump.dump_file_name(args.database, timestamp)
        print(f"Backing database up to {args.destination} in Google Cloud Storage as {file_name}")
        st.google_storage(storage_client, dump.stdout, args.destination, file_name)
    else:
        outfile = open(args.destination, 'wb')
        print(f"Backing database up locally to {outfile.name}")
        st.local(dump.stdout, outfile)



