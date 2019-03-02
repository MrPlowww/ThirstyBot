# ThirstyBot
This program gets status from the BCS API, writes it to an InfluxDB database (for external
visualization (e.g., Grafana) and data-logging purposes), and live-tweets brew session info.  ***CAUTION*** This is a work in-progress; some functionality may not be in place yet. Questions/comments are welcome - just message me!

0.0) Prerequisites
    0.1) Python Dependencies:
        0.1.a) Python package 'influxdb' shall be installed into the active Python environment (e.g., by running
                'pip install influxdb' in the environment's terminal window).
                 Tips: 'https://www.influxdata.com/blog/getting-started-python-influxdb/'
        0.1.b) Python package 'tweepy' shall be installed into the active Python environment (e.g., by running
                'pip install tweepy' in the environment's terminal window).
                Tweepy API definition: 'http://docs.tweepy.org/en/latest/api.html'
        0.1.c) Python module 'init_influxdb.py' shall be present in the active Python environment path (possibly in
                a Common directory, since this module is used in other unrelated Projects).
        0.1.d) Python module 'message_generator.py' and 'message_tweeter.py' shall be present
               in the active Python environment path (possibly in a Common directory, since this module is used in
               other unrelated Projects).
        0.1.e) Python module 'init_twitter_api' shall be present in the active Python environment path (possibly in
               a Common directory, since this module is used in other unrelated Projects). This module accepts
               JSON-formatted Twitter credentials (key:values), and returns a usable Twitter API.
    0.2) Configuration Dependencies:
        0.2.a) InfluxDB shall be installed; InfluxDB shall be running (e.g., by running this in a terminal window:
                'C:\Users\User\Downloads\00 Brewing\influxdb-1.5.2-1\influxd.exe'.
                 For info on where InfluxDB writes data, see:
                 'https://stackoverflow.com/questions/43644051/influxdb-storage-folder-windows'.
        0.2.b) If a target InfluxDB schema does not already exist, then the optional 'reset_database' function must
                first be executed stand-alone.
        0.2.c) The BCS shall be accessible on the network at a known IP address (e.g., 'http://192.168.1.70').
        0.2.d) Grafana: Grafana shall be installed; Grafana server shall be running (e.g., by running this in a
                terminal window: 'C:\Users\User\Downloads\00 Brewing\Grafana\grafana-5.1.3\bin\grafana-server.exe'.
                The Grafana UI is accessed via 'http://localhost:3000' (default user = admin; default pw = admin).
        0.2.e) Twitter: The target Twitter account shall be properly setup for app access, with the proper access
                credentials saved into a JSON-formatted file one directory level higher than this Python module
                (e.g., '../''twitter_credentials_thirstybot.json'). See these websites for tips/reference:
                'http://stackabuse.com/accessing-the-twitter-api-with-python/',
                'http://nodotcom.org/python-twitter-tutorial.html'.
 1.0) Run-time notes:
   1.1) Usage:
       1.1.1) standalone?: Yes.
           >>> 'exec(open('writeBCSdata12.py').read())'
       1.1.2) call from another module?: No.
 2.0) Changelog:
       v7: now loops on BCS's 'poll' API call (all  dynamic info obtained via single GET instead of 1 GET per probe).
       v12: Refactored structure for individual modules.
