# Version 1.0. This module initializes InfluxDB for use by another module.
# 0.0) Prerequisites
#    0.1) Python Dependencies:
#        0.1.a) Python package 'influxdb' shall be installed into the active Python environment (e.g., by running
#                'pip install influxdb' in the environment's terminal window).
#                 Tips: 'https://www.influxdata.com/blog/getting-started-python-influxdb/'
#    0.2) Configuration Dependency - InfluxDB:
#        0.2.a) InfluxDB shall be installed; InfluxDB shall be running (e.g., by running this in a terminal window:
#                'C:\Users\User\Downloads\00 Brewing\influxdb-1.5.2-1\influxd.exe'.
#                 For info on where InfluxDB writes data, see:
#                 'https://stackoverflow.com/questions/43644051/influxdb-storage-folder-windows'.
#        0.2.b) If a target InfluxDB schema does not already exist, then the optional 'reset_database' function must
#                first be executed stand-alone.
#    0.3) Configuration Dependency - None.
# 1.0) Run-time notes:
#    1.1) Usage example (from external Python module:
#           >>> import influxdb_init
#           >>> influxdb_init.init_influxdb('<database_name>') [where <database_name> = GURU1, or BCS5, or etc.]
# 2.0) Changelog:
#    2.1) Version 1.0: created stand-alone module.

def init_influxdb(target_database,host='localhost',port=8086):
    """ This function initializes the InfluxDB session. This assumes that the target database already exists. If it
    does not, then the 'reset_database' function must be executed first(see below).
        Usage ex: '>>> influxdb_init.init_influxdb(target_database='BCS5',host='localhost', port=8086)'
        The target_database key value shall be a string (I typically use GURU1 for BBQing and BCS5 for brewing).
        The host key value shall be a string and match the running InfluxDB session (default = 'localhost').
        The port key value shall be a integer and match the running InfluxDB session (default = 8086).
     """
    from influxdb import InfluxDBClient
    global client
    client = InfluxDBClient(host, port) # For more info: https://influxdb-python.readthedocs.io/en/latest/examples.html
    client.switch_database(target_database) # direct InfluxDB calls to the specified database
    print('Set InfluxDB database to: ' + str(target_database))
    return client


def reset_database(target_database,host='localhost',port=8086):
    """ CAUTION: This function will erase the specified Influx database and re-create it. Only call this function if
    that is the desired outcome."""
    from influxdb import InfluxDBClient
    client = InfluxDBClient(host, port)
    databases = str(client.get_list_database())  # get the list of databases.
    print('Prior to action taken, the current available databases are: ' + databases)
    confirmation = input('Are you sure you want to erase and reinitialize database ' + str(target_database) + '? (enter Y or N)')
    if confirmation == 'Y':
        client.drop_database(target_database)      # eliminates the specified database (and all data within)
        print('Database ' + target_database + ' erased.')
        databases = str(client.get_list_database())  # get the list of databases.
        print('The remaining databases are: ' + databases + '. Re-initializing database ' + target_database + '.')
        client.create_database(target_database)    # creates the specified database
        print('Database ' + target_database + ' re-initialized.')
        databases = str(client.get_list_database())  # get the list of databases.
        return print('After action taken, the curren tavailable databases are: ' + databases)
    else:
        return print('Aborted - no action taken')