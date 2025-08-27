import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

MAX_CONNECTIONS = int(config['FLIGHT_SEARCH']['max_connections'])
MAX_LAYOVER_HOURS = int(config['FLIGHT_SEARCH']['max_layover_hours'])
FOCUS_AIRPORTS = config['FLIGHT_SEARCH']['focus_airports'].split(',')
