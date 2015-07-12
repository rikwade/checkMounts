# checkMounts

A python script for OS X to check what network shares are mounted.
It will automatically re-mount unmounted shares which you would 
like mounted. Can be run from cron.

1) Check against the desired network share mounts in myMounts
2) For missing entries, call 'open' to re-mount under /Volumes/

Author: Rik Wade (rik@rikwade.com)
