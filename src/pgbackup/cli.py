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

    parser.add_argument("-h", help="host IP of database server")
    parser.add_argument("-d", help="database name")
    parser.add_argument("-U", help="username")
    parser.add_argument("-p", help="port number")
    parser.add_argument("--driver",
                        help="how & where to store backup",
                        nargs=2,
                        action=DriverAction,
                        required=True)
    return parser

