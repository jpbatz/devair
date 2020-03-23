import os, sys
import glob

# for Mike M.: create a list of files to restart voip services
# - input is the directory list of origin and destination pipes
# - each restart command should include the forward and reverse airports
#      in the order listed

# extracts only files with the word AIR, since folder may contain other files and dirs
#files = [f for f in glob.glob("/Users/Mike/TestData/airports/*AIR*")]
files = [f for f in glob.glob("/Users/jph/Documents - jMBP/GitHub/DevAir/*AIR*")]

prefix = 'voip_restart <voice.pipe.AIR-'

airports = []

for file in files:
    # removes the newline and creates a list with 3 items
    # [0] garbage, [1] origin, [2] destination
    parts = file.strip().split(".AIR-")
    airports.append(prefix + parts[1] + '.AIR-' + parts[2] + '>')   # forward
    airports.append(prefix + parts[-1] + '.AIR-' + parts[-2] + '>') # reverse

# displays and runs commands
for airport in airports:
    print('Restarting: ' + airport)
    # cmd = airport
    # os.system(cmd)   # same as os.system(airport)
