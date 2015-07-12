#!/usr/bin/env python

# A python script to check what filesystems are mounted
# Check against the desired network share mounts in myMounts
# For missing entries, call 'open' to re-mount under /Volumes/
# 11-July-2015

import subprocess

myMounts = {
    '/Volumes/backup': False,
    '/Volumes/data': False,
    '/Volumes/media': False
}

for line in subprocess.check_output(['mount']).split('\n'):
    parts = line.split(' ')
    if len(parts) > 2:
        if parts[2] in myMounts:
            myMounts[parts[2]]=True;

for key in myMounts:
    if myMounts[key] is False:
        path = key.split('/');
        # open afp://guest@diskstation.local/$path
        share = "afp://guest@diskstation.local/"+path[2];
        subprocess.call(['open', share]);
        print "Opened: "+share

