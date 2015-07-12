#!/usr/bin/env python

# A python script for OS X to check what network shares are mounted.
# Automatically re-mount unmounted shares which you would like mounted.
# Can be run from cron.
#
# 1) Check against the desired network share mounts in myMounts
# 2) For missing entries, call 'open' to re-mount under /Volumes/

import subprocess

# Change this dictionary to reflect the shares you want always mounted
# Set to False initially. They will be set to True if they are found
# in the mounts list.
myMounts = {
    '/Volumes/backup': False,
    '/Volumes/data': False,
    '/Volumes/media': False
}

# A variable for the network share prefix you wish to use. This
# should be a CIFs, AFP etc. share for a server on your network
# This is an example and should be changed
myNASprefix = "afp://guest@diskstation.local/";

# Check the current mounts to see if the shares are mounted
for line in subprocess.check_output(['mount']).split('\n'):
    parts = line.split(' ')
    if len(parts) > 2:
        if parts[2] in myMounts:
            myMounts[parts[2]]=True;

# Go through the dictionary, see what is still False and re-mount it
# We use 'open' here because it's a simple way of re-mounting in OS X
for key in myMounts:
    if myMounts[key] is False:
        path = key.split('/');
        share = myNASprefix+path[2];
        subprocess.call(['open', share]);
        print "Re-mounted: "+share

