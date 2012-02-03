#!/usr/bin/env python

import sys,math

tr = 2.0

if __name__ == "__main__":
    if len(sys.argv)==2:
        inFileName = sys.argv[1]
    else:
        print("ERROR: you must specify a Psychopy log file to parse!")
        sys.exit(1)

    # number of seconds of data that will be chopped off from the beginning of each block:
    startChopSecs = 6
    blockTypes = ['normal','attentive','attentive','normal']
    trialTimes = {'normal':[], 'attentive':[]}

    with open(inFileName, 'r') as f:
        # Run through the file to parse all the trial times and extract condition names.
        textStartTimes = []
        textEndTimes = []
        scanStartTimes = []
        curBlockNum = -1
        for l in f.readlines():
           w = l.split('\t');
           if w[1]=='DATA' and w[2].startswith('Keypress: space'):
               scanStartTimes.append(float(w[0]))
               curBlockNum = curBlockNum+1
               textStartTimes.append([])
               textEndTimes.append([])
           elif w[1]=='EXP':
               if w[2].startswith("Started presenting paragraphs"):
                   textStartTimes[curBlockNum].append(float(w[0]))
               elif w[2].startswith("Stopped presenting paragraphs"):
                   # We assume that there must be a "stop" following each start!
                   textEndTimes[curBlockNum].append(float(w[0]))

    start = 0
    duration = 0
    blockDuration = []
    prevEndTime = 0
    for b in range(len(blockTypes)):
        # we'll need the total block duration to know how to chop the timeseries:
        curBlockDuration = textEndTimes[b][-1] - scanStartTimes[b] - startChopSecs
        # round up to the next nearest tr
        curBlockDuration = math.ceil(curBlockDuration/tr)*tr
        blockDuration.append(curBlockDuration) 
        for t in range(len(textStartTimes[b])):
            start = textStartTimes[b][t] - (scanStartTimes[b]+startChopSecs) + prevEndTime
            duration = textEndTimes[b][t] - textStartTimes[b][t]
            trialTimes[blockTypes[b]].append("%f %f 1\n" % (start,duration))
        prevEndTime = prevEndTime + curBlockDuration

    with open('normal.txt','w') as f:
        f.writelines(trialTimes['normal'])
    
    with open('attentive.txt','w') as f:
        f.writelines(trialTimes['attentive'])

    print "Block durations (sec): " + str(blockDuration)
    print "Block durations (trs): " + str([t/tr for t in blockDuration])
    print "Start chop secs: " + str(startChopSecs)
    
    for curDur in blockDuration:
        print "fslroi fmri.nii.gz fmri_chopped.nii.gz -1 -1 -1 -1 -1 -1 " + str(int(startChopSecs/tr)) + " " + str(int(curDur/tr))

# *** TODO: the timeseries will be chopped to eliminate the dead time at the end of each block.
# Thus, the "prevEndTime" should be rounded up to the next TR.

    print 'Finished.'
    exit(0)

