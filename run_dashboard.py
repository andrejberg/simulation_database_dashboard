from __future__ import print_function
from os import environ
from sys import exit

from simulation_database_dashboard.config import config_dict
from simulation_database_dashboard import create_app

get_config_mode = environ.get('SIMDB_CONFIG_MODE', 'Debug')

try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid SIMDB_CONFIG_MODE environment variable entry.')

app = create_app(config_mode)


if __name__ == '__main__':

    # empty log
    with open("error.log", "w") as log:
        log.write("")

    # Start app
    app.run(debug=True)
