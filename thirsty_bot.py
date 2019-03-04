# Thirsty Bot: This program gets status from the BCS API, writes it to an InfluxDB database (for external
# visualization (e.g., Grafana) and data-logging purposes), and live-tweets brew session info.
# 0.0) Prerequisites
#    0.1) Python Dependencies:
#        0.1.a) Python package 'influxdb' shall be installed into the active Python environment (e.g., by running
#                'pip install influxdb' in the environment's terminal window).
#                 Tips: 'https://www.influxdata.com/blog/getting-started-python-influxdb/'
#        0.1.b) Python module 'init_influxdb.py' shall be present in the active Python environment path (possibly in
#                a Common directory, since this module is used in other unrelated Projects).
#        0.1.c) Python package 'tweepy' shall be installed into the active Python environment (e.g., by running
#                'pip install tweepy' in the environment's terminal window). This is required for 'init_twitter_api.py'
#                and 'tweet.py'. Tweepy API definition: 'http://docs.tweepy.org/en/latest/api.html'
#        0.1.d) Python module 'init_twitter_api.py' shall be present in the active Python environment path (possibly in
#               a Common directory, since this module is used in other unrelated Projects). This module accepts
#               JSON-formatted Twitter credentials (key:values), and returns a usable Twitter API.
#        0.1.e) Python module 'tweet.py' shall be present in the active Python environment path (possibly in
#               a Common directory, since this module is used in other unrelated Projects). This module accepts
#               the 'api' object (returned by 'init_twitter_api.py) as a required argument, and it accepts N number of
#               additional string-formatted arguments. The 'tweet.py' module concatenates the string-formatted arguments
#               (so be careful about spaces/punctuation in the arguments) and tweets-out the result (using the passed
#               api.
#        0.1.f) Python module 'message_generator.py' shall be present in the active Python environment path (possibly
#               in a Common directory, since this module is used in other unrelated Projects).
#    0.2) Configuration Dependencies:
#        0.2.a) InfluxDB shall be installed; InfluxDB shall be running (e.g., by running this in a terminal window:
#                'C:\Users\User\Downloads\00 Brewing\influxdb-1.5.2-1\influxd.exe'.
#                 For info on where InfluxDB writes data, see:
#                 'https://stackoverflow.com/questions/43644051/influxdb-storage-folder-windows'.
#        0.2.b) If a target InfluxDB schema does not already exist, then the optional 'reset_database' function must
#                first be executed stand-alone.
#        0.2.c) The BCS shall be accessible on the network at a known IP address (e.g., 'http://192.168.1.70').
#        0.2.d) Grafana: Grafana shall be installed; Grafana server shall be running (e.g., by running this in a
#                terminal window: 'C:\Users\User\Downloads\00 Brewing\Grafana\grafana-5.1.3\bin\grafana-server.exe'.
#                The Grafana UI is accessed via 'http://localhost:3000' (default user = admin; default pw = admin).
#        0.2.e) Twitter: The target Twitter account shall be properly setup for app access, with the proper access
#                credentials. For more information, see documentation for the 'init_twitter_api.py' module and these
#                websites for tips/reference:
#                'http://stackabuse.com/accessing-the-twitter-api-with-python/',
#                'http://nodotcom.org/python-twitter-tutorial.html'.
# 1.0) Run-time notes:
#   1.1) Usage:
#       1.1.1) standalone?: Yes.
#           >>> 'exec(open('thirsty_bot.py').read())'
#       1.1.2) call from another module?: No.
# 2.0) Changelog:
#       Version 1.0: Original version.

# ******* SECTION 0 - Program Control *******
tweet_enabled = True  # when "True", program will attempt to Tweet.
debug_enabled = False  # when "True", program will print internal status messages to the screen.
message_generator_debug_enabled = False  # when "True", program will print message_generator to screen every iteration.
first_tweet_flag = 1   # initialize first tweet flag for one-time-only brew tweeting (it later gets set to 0 forever)
loop_delay = 2  # This dictates how many seconds to delay before looping back through the program. This same number
                # is used to set the initial value and decrement amount for brew_tweet_delay and message_delay so that
                # everything decrements in lockset with the loop delay.
message_delay = loop_delay  # initially set random message delay; this gets reset to the 'static_message_generator_tweet_delay' value once it hits 0.
brew_tweet_delay = loop_delay  # initially set brew tweet delay; this gets reset to the 'static_brew_tweet_delay' value once it hits 0.
static_message_generator_tweet_delay = 500  # Recommended value = 500 (in seconds, a.k.a. 8.3 minutes)
static_brew_tweet_delay = 600               # Recommended value = 600 (in seconds, a.k.a. 10 minutes)
BCS_IP = 'http://192.168.1.150' # Network IP for BCS (e.g., 'http://192.168.1.150', 'http://192.168.1.70')
beer_type = str(input("Enter the beer type (e.g., 'stout') and press enter: "))  # used for live-tweeting
if beer_type == "":  # used to handle case in which user enters nothing into the beer-type prompt.
    beer_type = 'beer.'
else:
    beer_type = beer_type + '.'


# ******* SECTION 1: Initialize InfluxDB session: *******
import init_influxdb  # See Prerequisite 0.1.a and 0.1.b.
init_influxdb.init_influxdb(target_database='BCS5',host='localhost', port=8086)


# ******* SECTION 2 - Initialize Twitter API *******
import json  # required to parse Twitter credentials file
import init_twitter_api  # see Prerequisite 0.1.d (Twitter API init module), 0.1.c ('tweepy' package), & 0.2.e (Twitter)
with open('../twitter_credentials_thirstybot.json') as file:  # see Prerequisites 0.2.e (@thirstybot's Twitter keys)
    twitter_credentials = json.load(file)
api = init_twitter_api.init_twitter_api(twitter_credentials) # create object ('api') portal to Twitter API


# ******* SECTION 3 - Initialize Message Generator *******
import tweet  # See Prerequisite 0.1.e ('tweet.py' module).
import message_generator  # See Prerequisite 0.1.f ('message_generator' module).


# ******* SECTION 4: Main - continuously get BCS data, write data to InfluxDB, and tweet!  *******
import requests  # needed for 'get' method.
from time import gmtime, strftime, sleep  # needed for processing GMT/current time and for loop delay (sleep)
probe0_json = requests.get(BCS_IP + '/api/temp/0').json() # get temperature probe 0 (HLT) semi-static data (not polled from BCS) and store in JSON string.
probe1_json = requests.get(BCS_IP + '/api/temp/1').json() # get temperature probe 1 (HERMS) semi-static data (not polled from BCS) and store in JSON string.
probe2_json = requests.get(BCS_IP + '/api/temp/2').json() # get temperature probe 2 (Boil) semi-static data (not polled from BCS) and store in JSON string.
probe7_json = requests.get(BCS_IP + '/api/temp/7').json() # get temperature probe 7 (MLT) semi-static data (not polled from BCS) and store in JSON string.
while True:  # loop forever (until manually stopped), pausing for duration=loop_delay (i.e., 2 sec) between loops
    poll = requests.get(BCS_IP + '/api/poll').json()
    process_0 = requests.get(BCS_IP + '/api/process/0').json()
    process_1 = requests.get(BCS_IP + '/api/process/1').json()
    ## start: load active process data
    if process_0['running'] == True and process_1['running'] == False:
        active_process_name = process_0['name']                                        # grab active process name
        current_state_number = process_0['current_state']['state']                     # grab active process number
        current_state_name = process_0['states'][process_0['current_state']['state']]  # grab current state name
        process_0_timer_json = requests.get(BCS_IP + '/api/process/0/timer').json()    # get process 0 timer data
        process_timer0_name = process_0_timer_json[0]['name']
        process_timer0_value = process_0_timer_json[0]['value']
        process_timer1_name = process_0_timer_json[1]['name']
        process_timer1_value = process_0_timer_json[1]['value']
        process_timer2_name = process_0_timer_json[2]['name']
        process_timer2_value = process_0_timer_json[2]['value']
        active_process = 'Process 0 is running'
    elif process_1['running'] == True and process_0['running'] == False:
        active_process_name = process_1['name']                                        # grab active process name
        current_state_number = process_1['current_state']['state']                     # grab active process number
        current_state_name = process_1['states'][process_1['current_state']['state']]  # grab current state name
        process_1_timer_json = requests.get(BCS_IP + '/api/process/1/timer').json()    # get process 1 timer data
        process_timer0_name = process_1_timer_json[0]['name']
        process_timer0_value = process_1_timer_json[0]['value']
        process_timer1_name = process_1_timer_json[1]['name']
        process_timer1_value = process_1_timer_json[1]['value']
        process_timer2_name = process_1_timer_json[2]['name']
        process_timer2_value = process_1_timer_json[2]['value']
        active_process = 'Process 1 is running'
    elif process_1['running'] == True and process_0['running'] == True:  # If two processes running (can't handle this yet)
        active_process_name = 'multiple'                                                   
        current_state_number = None                                
        current_state_name = 'multiple'
        process_timer0_name = 'multiple'
        process_timer0_value = None
        process_timer1_name = 'multiple'
        process_timer1_value = None
        process_timer2_name = 'multiple'
        process_timer2_value = None
        active_process = 'MULTIPLE PROCESSES ARE RUNNING'
    else:  # clears the variable states when neither Process 1 nor Process 2 are running
        active_process_name = 'none'
        current_state_number = None
        current_state_name = 'none'
        process_timer0_name = 'none'
        process_timer0_value = None
        process_timer1_name = 'none'
        process_timer1_value = None
        process_timer2_name = 'none'
        process_timer2_value = None
        active_process = 'No Process is running'
    ## end loading active process name data
    json_body = [{
        "measurement": "BCS_events",  # measurements for all data
        "tags": {
            "tag_brewer": "Jon",
            "tag_probe0_name": probe0_json['name'], # used by Grafana (e.g., variable var_probe0_name)
            "tag_probe1_name": probe1_json['name'], # used by Grafana (e.g., variable var_probe1_name)
            "tag_probe2_name": probe2_json['name'], # used by Grafana (e.g., variable var_probe2_name)
            "tag_probe7_name": probe7_json['name'], # used by Grafana (e.g., variable var_probe3_name)
            "tag_process_timer0_name": process_timer0_name,
            "tag_process_timer1_name": process_timer1_name,
            "tag_process_timer2_name": process_timer2_name
        },
        "time": strftime("%Y-%m-%d %H:%M:%S", gmtime()),
        "fields": {
            "probe0_name": probe0_json['name'],             # probe name not polled
            "probe0_temperature": poll['temp'][0] / 10,     # HLT probe temperature
            "probe0_setpoint": poll['setpoint'][0],         # HLT probe setpoint
            "probe1_name": probe1_json['name'],             # probe name not polled
            "probe1_temperature": poll['temp'][1] / 10,     # HERMS probe temperature
            "probe1_setpoint": poll['setpoint'][1],         # HERMS probe setpoint
            "probe2_name": probe2_json['name'],             # probe name not polled
            "probe2_temperature": poll['temp'][2] / 10,     # BK probe temperature
            "probe2_setpoint": poll['setpoint'][2],         # BK probe setpoint
            "probe7_name": probe7_json['name'],             # probe name not polled
            "probe7_temperature": poll['temp'][7] / 10,     # MLT probe temperature
            "probe7_setpoint": poll['setpoint'][7],         # MLT probe setpoint
            "output0": poll['output'][0],                   # HLT element (returns 0 for off, 1 for on)
            "output1": poll['output'][1],                   # BK element (returns 0 for off, 1 for on)
            "output6": poll['output'][6],                   # water pump (returns 0 for off, 1 for on)
            "output7": poll['output'][7],                   # wort pump (returns 0 for off, 1 for on)
            "output8": poll['output'][8],                   # alarm (returns 0 for off, 1 for on)
            "active_process_name": active_process_name,     # active process (e.g., Strike/Mash, Boil)
            "current_state_name": current_state_name,       # current state w/in active process (e.g, Heat Strike)
            "process_timer0_name": process_timer0_name,
            "process_timer0_value": process_timer0_value,
            "process_timer1_name": process_timer1_name,
            "process_timer1_value": process_timer1_value,
            "process_timer2_name": process_timer2_name,
            "process_timer2_value": process_timer2_value,
            "local_time": strftime("%Y-%m-%d %H:%M:%S")
        }
    }]
    init_influxdb.client.write_points(json_body)  # writes the JSON object to InfluxDB
    if tweet_enabled == True:
        if first_tweet_flag == 1:
            first_tweet_flag = 0  # reset first_tweet_flag to 0 to prevent repetition until program restart
            requested_tweet = 'Bleep Blorp. I am programed to brew beer and to love. Today I am brewing a ' + beer_type
            tweet.post_tweet(api,requested_tweet)
        else:
            if debug_enabled == True:
                print('better not be first tweeting because first_tweet_flag = ' + str(first_tweet_flag))
            else:
                pass
        if brew_tweet_delay <= 0:
            brew_tweet_delay = static_brew_tweet_delay # reset brew tweet delay to value specified in program control
            tweet_part_1 = 'My active brew process step is ' + active_process_name
            tweet_part_2 = ' and my active brew process name is ' + current_state_name + '. '
            tweet_part_3 = 'HLT = ' + str(json_body[0]['fields']['probe0_temperature']) + '\u00b0F. '
            tweet_part_4 = 'HERMS output = ' + str(json_body[0]['fields']['probe1_temperature']) + '\u00b0F. '
            tweet_part_5 = 'Mash Tun = ' + str(json_body[0]['fields']['probe7_temperature']) + '\u00b0F. '
            tweet_part_6 = 'Boil Kettle = ' + str(json_body[0]['fields']['probe2_temperature']) + '\u00b0F. '
            requested_tweet = tweet_part_1 + tweet_part_2 + tweet_part_3 + tweet_part_4 + tweet_part_5 + tweet_part_6
            tweet.post_tweet(api,requested_tweet)  # Tweet about brewing
        else:
            brew_tweet_delay = brew_tweet_delay - loop_delay
            if debug_enabled == True:
                print('not supposed to brew tweet now because brew_tweet_delay is ' + str(brew_tweet_delay))
            else:
                pass
        if message_delay <= 0:  # if delay has decremented to 0, then try tweeting (and reset delay)
            message_delay = static_message_generator_tweet_delay # reset message delay to value specified in program control
            words = message_generator.define_words()  # Initializes the word dictionary.
            all_jobs = message_generator.message(words)  # Builds list of jobs (w/o preable) from random words in word dictionary
            requested_tweet = message_generator.respond_one(all_jobs)  # Returns a single randomly chosen message from the message list (with default reamble) and store it in "message"
            tweet.post_tweet(api, requested_tweet)
        else:
            message_delay = message_delay - loop_delay
            if debug_enabled == True:
                print('not supposed to tweet message now because message_delay is ' + str(message_delay))
            else:
                pass
    sleep(loop_delay)  # pause for duration of loop_delay (i.e., 2 sec); will then loop
    #
    # Debug-only functions
    #
    if debug_enabled == True:
        print('Debug enabled...message_delay = ' + str(message_delay))  # debug: monitor the message tweet counter value
        print('Debug enabled...brew_tweet_delay = ' + str(brew_tweet_delay))  # debug: monitor the brew tweet counter value
        print('As of ' + strftime("%Y-%m-%d %H:%M:%S") + ' ' + active_process)
    if message_generator_debug_enabled == True: # only for troubleshooting (or up-sampling) message_generator outputs
        words = message_generator.define_words()  # Initializes the word dictionary.
        all_jobs = message_generator.message(words)  # Builds list of jobs (w/o preable) from random words in word dictionary
        message = message_generator.respond_one(all_jobs)  # Returns a single randomly chosen message from the message list (with default reamble) and store it in "message"
        print('Message debug enabled...message_generator screen-output (not to Twitter): ' + str(message))