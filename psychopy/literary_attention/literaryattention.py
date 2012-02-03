#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.71.00), December 11, 2011, at 16:47
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""
import numpy as np  # whole numpy lib is available, pre-pend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os #handy system and path functions
from psychopy import core, data, event, visual, gui
import psychopy.log #import like this so it doesn't interfere with numpy.log
from psychopy.constants import *

#store info about the experiment session
expName='None'#from the Builder filename that created this script
expInfo={'participant':'', 'session':'01'}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName
#setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
filename='data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
psychopy.log.console.setLevel(psychopy.log.WARNING)#this outputs to the screen, not a file
logFile=psychopy.log.LogFile(filename+'.log', level=psychopy.log.INFO)

#setup the Window
win = visual.Window(size=[1280, 800], fullscr=False, screen=1, allowGUI=True, allowStencil=False,
    monitor='CNI_LCD', color='white', colorSpace='rgb', units='norm')

#Initialise components for routine:init
initClock=core.Clock()
import serial
import datetime
import time
device = '/dev/ttyACM1'
try:
    ser = serial.Serial(device, 115200, timeout=1)
    ser.write('[s,{"dev":"eye","cmd":"start","dur":2400,"file":"eye"}]\n')
    ser.close()
except:
    pass

mainClock=core.Clock()


#Initialise components for routine:instruct_green
instruct_greenClock=core.Clock()
instrText_2=visual.TextStim(win=win, ori=0, name='instrText_2',
    text="The following text will be surrounded by a GREEN border. So just relax and read for pleasure. Imagine you just picked up this book off the bookshelf and are reading in your favorite spot. None of this material will be tested. \n\nPress the button with your thumb when you're done with a paragraph.",
    font='Arial',
    pos=[0, 0], height=0.05,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1)


#Initialise components for routine:trial
trialClock=core.Clock()

paragraphs=visual.TextStim(win=win, ori=0, name='paragraphs',
    text='nonsense',
    font='Arial',
    units='pix', pos=[0, 0], height=22,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1)


#Initialise components for routine:instruct_red
instruct_redClock=core.Clock()
instrText_3=visual.TextStim(win=win, ori=0, name='instrText_3',
    text="The following text will be surrounded by a RED border, so please read the novel with heightened attention and do a close reading for literary analysis. You'll be tested on this material when you leave the scanner and asked to write a short literary essay. Focus on literary themes and patterns, word choice, syntax, and the order in which sentences and ideas unfold. Pay attention to how the story's structure is constructed, or crafted, noticing literary details such as setting, narration, tone, and characterization.\n \nPress the button with your thumb when you're done with a paragraph.",
    font='Arial',
    pos=[0, 0], height=0.05,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1)


#Initialise components for routine:trial
trialClock=core.Clock()

paragraphs=visual.TextStim(win=win, ori=0, name='paragraphs',
    text='nonsense',
    font='Arial',
    units='pix', pos=[0, 0], height=22,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1)


#Initialise components for routine:instruct_red
instruct_redClock=core.Clock()
instrText_3=visual.TextStim(win=win, ori=0, name='instrText_3',
    text="The following text will be surrounded by a RED border, so please read the novel with heightened attention and do a close reading for literary analysis. You'll be tested on this material when you leave the scanner and asked to write a short literary essay. Focus on literary themes and patterns, word choice, syntax, and the order in which sentences and ideas unfold. Pay attention to how the story's structure is constructed, or crafted, noticing literary details such as setting, narration, tone, and characterization.\n \nPress the button with your thumb when you're done with a paragraph.",
    font='Arial',
    pos=[0, 0], height=0.05,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1)


#Initialise components for routine:trial
trialClock=core.Clock()

paragraphs=visual.TextStim(win=win, ori=0, name='paragraphs',
    text='nonsense',
    font='Arial',
    units='pix', pos=[0, 0], height=22,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1)


#Initialise components for routine:instruct_green
instruct_greenClock=core.Clock()
instrText_2=visual.TextStim(win=win, ori=0, name='instrText_2',
    text="The following text will be surrounded by a GREEN border. So just relax and read for pleasure. Imagine you just picked up this book off the bookshelf and are reading in your favorite spot. None of this material will be tested. \n\nPress the button with your thumb when you're done with a paragraph.",
    font='Arial',
    pos=[0, 0], height=0.05,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1)


#Initialise components for routine:trial
trialClock=core.Clock()

paragraphs=visual.TextStim(win=win, ori=0, name='paragraphs',
    text='nonsense',
    font='Arial',
    units='pix', pos=[0, 0], height=22,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1)


#Initialise components for routine:thanks
thanksClock=core.Clock()
thanksText=visual.TextStim(win=win, ori=0, name='thanksText',
    text='This is the end of the experiment.\n\nThanks!',
    font='arial',
    pos=[0, 0], height=0.3,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1)

#Start of routine init
t=0; initClock.reset()
frameN=-1

#update component parameters for each repeat

#keep track of which have finished
initComponents=[]#to keep track of which have finished
for thisComponent in initComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#start the Routine
continueRoutine=True
while continueRoutine:
    #get current time
    t=initClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    
    #check if all components have finished
    if not continueRoutine:
        break # lets a component forceEndRoutine
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in initComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#end of routine init
for thisComponent in initComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)


#Start of routine instruct_green
t=0; instruct_greenClock.reset()
frameN=-1

#update component parameters for each repeat
ready_2 = event.BuilderKeyResponse() #create an object of type KeyResponse
ready_2.status=NOT_STARTED


#keep track of which have finished
instruct_greenComponents=[]#to keep track of which have finished
instruct_greenComponents.append(instrText_2)
instruct_greenComponents.append(ready_2)
for thisComponent in instruct_greenComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#start the Routine
continueRoutine=True
while continueRoutine:
    #get current time
    t=instruct_greenClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*instrText_2* updates
    if t>=0 and instrText_2.status==NOT_STARTED:
        #keep track of start time/frame for later
        instrText_2.tStart=t#underestimates by a little under one frame
        instrText_2.frameNStart=frameN#exact frame index
        instrText_2.setAutoDraw(True)
    
    #*ready_2* updates
    if t>=0 and ready_2.status==NOT_STARTED:
        #keep track of start time/frame for later
        ready_2.tStart=t#underestimates by a little under one frame
        ready_2.frameNStart=frameN#exact frame index
        ready_2.status=STARTED
        #keyboard checking is just starting
        event.clearEvents()
    if ready_2.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys)>0:#at least one key was pressed
            #abort routine on response
            continueRoutine=False
    
    
    #check if all components have finished
    if not continueRoutine:
        break # lets a component forceEndRoutine
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in instruct_greenComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#end of routine instruct_green
for thisComponent in instruct_greenComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
try:
    ser = serial.Serial(device, 115200, timeout=1)
    ser.write('[t]\n[t]\n')
    ser.close()
except:
    pass

#set up handler to look after randomisation of conditions etc
trials_1=data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('textA.csv'))
thisTrial_1=trials_1.trialList[0]#so we can initialise stimuli with some values
#abbreviate parameter names if possible (e.g. rgb=thisTrial_1.rgb)
if thisTrial_1!=None:
    for paramName in thisTrial_1.keys():
        exec(paramName+'=thisTrial_1.'+paramName)

for thisTrial_1 in trials_1:
    currentLoop = trials_1
    #abbrieviate parameter names if possible (e.g. rgb=thisTrial_1.rgb)
    if thisTrial_1!=None:
        for paramName in thisTrial_1.keys():
            exec(paramName+'=thisTrial_1.'+paramName)
    
    #Start of routine trial
    t=0; trialClock.reset()
    frameN=-1
    
    #update component parameters for each repeat
    try:
        ser = serial.Serial(device, 115200, timeout=1)
        ser.write('[s,{"dev":"eye","cmd":"mark","val":"read '+currentLoop.thisIndex():+'"}]\n')
        ser.close()
    except:
        pass
    
    paragraphs.setText(text)
    resp = event.BuilderKeyResponse() #create an object of type KeyResponse
    resp.status=NOT_STARTED
    print 'begin text ('+str(mainClock.getTime())+')'
    #keep track of which have finished
    trialComponents=[]#to keep track of which have finished
    trialComponents.append(paragraphs)
    trialComponents.append(resp)
    for thisComponent in trialComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #start the Routine
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=trialClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        
        #*paragraphs* updates
        if t>=8 and paragraphs.status==NOT_STARTED:
            #keep track of start time/frame for later
            paragraphs.tStart=t#underestimates by a little under one frame
            paragraphs.frameNStart=frameN#exact frame index
            paragraphs.setAutoDraw(True)
        
        #*resp* updates
        if t>=1 and resp.status==NOT_STARTED:
            #keep track of start time/frame for later
            resp.tStart=t#underestimates by a little under one frame
            resp.frameNStart=frameN#exact frame index
            resp.status=STARTED
            #keyboard checking is just starting
            resp.clock.reset() # now t=0
            event.clearEvents()
        if resp.status==STARTED:#only update if being drawn
            theseKeys = event.getKeys(keyList=['1', 'n'])
            if len(theseKeys)>0:#at least one key was pressed
                resp.keys=theseKeys[-1]#just the last key pressed
                resp.rt = resp.clock.getTime()
                #abort routine on response
                continueRoutine=False
        if (t >= 5):
            visual.ShapeStim(win=win, units='norm', lineWidth=5, lineColor=itemColor, vertices=((.5,.8),(.5,-.8),(-.5,-.8), (-.5,.8))).draw()
        if (t < 5):
            visual.ShapeStim(win=win, units='norm', lineWidth=5, lineColor='gray', vertices=((.5,.8),(.5,-.8),(-.5,-.8), (-.5,.8))).draw()
        
        #check if all components have finished
        if not continueRoutine:
            break # lets a component forceEndRoutine
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]): core.quit()
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #end of routine trial
    for thisComponent in trialComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    try:
        ser = serial.Serial(device, 115200, timeout=1)
        ser.write('[s,{"dev":"eye","cmd":"mark","val":"done"}]\n')
        ser.close()
    except:
        pass
    time.sleep(0.1)
    #check responses
    if len(resp.keys)==0: #No response was made
       resp.keys=None
    #store data for trials_1 (TrialHandler)
    trials_1.addData('resp.keys',resp.keys)
    if resp.keys != None:#we had a response
        trials_1.addData('resp.rt',resp.rt)
    print "key=%s, rt=%f" % (resp.keys,resp.rt)
    print 'end text ('+str(mainClock.getTime())+')'
    

#completed 1.0 repeats of 'trials_1'

trials_1.saveAsPickle(filename+'trials_1')
trials_1.saveAsExcel(filename+'.xlsx', sheetName='trials_1',
    stimOut=trials_1.trialList[0].keys(),
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_1.saveAsText(filename+'trials_1.csv', delim=',',
    stimOut=trials_1.trialList[0].keys(),
    dataOut=['n','all_mean','all_std', 'all_raw'])

#Start of routine instruct_red
t=0; instruct_redClock.reset()
frameN=-1

#update component parameters for each repeat
ready_3 = event.BuilderKeyResponse() #create an object of type KeyResponse
ready_3.status=NOT_STARTED


#keep track of which have finished
instruct_redComponents=[]#to keep track of which have finished
instruct_redComponents.append(instrText_3)
instruct_redComponents.append(ready_3)
for thisComponent in instruct_redComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#start the Routine
continueRoutine=True
while continueRoutine:
    #get current time
    t=instruct_redClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*instrText_3* updates
    if t>=0 and instrText_3.status==NOT_STARTED:
        #keep track of start time/frame for later
        instrText_3.tStart=t#underestimates by a little under one frame
        instrText_3.frameNStart=frameN#exact frame index
        instrText_3.setAutoDraw(True)
    
    #*ready_3* updates
    if t>=0 and ready_3.status==NOT_STARTED:
        #keep track of start time/frame for later
        ready_3.tStart=t#underestimates by a little under one frame
        ready_3.frameNStart=frameN#exact frame index
        ready_3.status=STARTED
        #keyboard checking is just starting
        event.clearEvents()
    if ready_3.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys)>0:#at least one key was pressed
            #abort routine on response
            continueRoutine=False
    
    
    #check if all components have finished
    if not continueRoutine:
        break # lets a component forceEndRoutine
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in instruct_redComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#end of routine instruct_red
for thisComponent in instruct_redComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
try:
    ser = serial.Serial(device, 115200, timeout=1)
    ser.write('[t]\n[t]\n')
    ser.close()
except:
    pass

#set up handler to look after randomisation of conditions etc
trials_2=data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('textB.csv'))
thisTrial_2=trials_2.trialList[0]#so we can initialise stimuli with some values
#abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
if thisTrial_2!=None:
    for paramName in thisTrial_2.keys():
        exec(paramName+'=thisTrial_2.'+paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    #abbrieviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
    if thisTrial_2!=None:
        for paramName in thisTrial_2.keys():
            exec(paramName+'=thisTrial_2.'+paramName)
    
    #Start of routine trial
    t=0; trialClock.reset()
    frameN=-1
    
    #update component parameters for each repeat
    try:
        ser = serial.Serial(device, 115200, timeout=1)
        ser.write('[s,{"dev":"eye","cmd":"mark","val":"read '+currentLoop.thisIndex():+'"}]\n')
        ser.close()
    except:
        pass
    
    paragraphs.setText(text)
    resp = event.BuilderKeyResponse() #create an object of type KeyResponse
    resp.status=NOT_STARTED
    print 'begin text ('+str(mainClock.getTime())+')'
    #keep track of which have finished
    trialComponents=[]#to keep track of which have finished
    trialComponents.append(paragraphs)
    trialComponents.append(resp)
    for thisComponent in trialComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #start the Routine
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=trialClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        
        #*paragraphs* updates
        if t>=8 and paragraphs.status==NOT_STARTED:
            #keep track of start time/frame for later
            paragraphs.tStart=t#underestimates by a little under one frame
            paragraphs.frameNStart=frameN#exact frame index
            paragraphs.setAutoDraw(True)
        
        #*resp* updates
        if t>=1 and resp.status==NOT_STARTED:
            #keep track of start time/frame for later
            resp.tStart=t#underestimates by a little under one frame
            resp.frameNStart=frameN#exact frame index
            resp.status=STARTED
            #keyboard checking is just starting
            resp.clock.reset() # now t=0
            event.clearEvents()
        if resp.status==STARTED:#only update if being drawn
            theseKeys = event.getKeys(keyList=['1', 'n'])
            if len(theseKeys)>0:#at least one key was pressed
                resp.keys=theseKeys[-1]#just the last key pressed
                resp.rt = resp.clock.getTime()
                #abort routine on response
                continueRoutine=False
        if (t >= 5):
            visual.ShapeStim(win=win, units='norm', lineWidth=5, lineColor=itemColor, vertices=((.5,.8),(.5,-.8),(-.5,-.8), (-.5,.8))).draw()
        if (t < 5):
            visual.ShapeStim(win=win, units='norm', lineWidth=5, lineColor='gray', vertices=((.5,.8),(.5,-.8),(-.5,-.8), (-.5,.8))).draw()
        
        #check if all components have finished
        if not continueRoutine:
            break # lets a component forceEndRoutine
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]): core.quit()
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #end of routine trial
    for thisComponent in trialComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    try:
        ser = serial.Serial(device, 115200, timeout=1)
        ser.write('[s,{"dev":"eye","cmd":"mark","val":"done"}]\n')
        ser.close()
    except:
        pass
    time.sleep(0.1)
    #check responses
    if len(resp.keys)==0: #No response was made
       resp.keys=None
    #store data for trials_2 (TrialHandler)
    trials_2.addData('resp.keys',resp.keys)
    if resp.keys != None:#we had a response
        trials_2.addData('resp.rt',resp.rt)
    print "key=%s, rt=%f" % (resp.keys,resp.rt)
    print 'end text ('+str(mainClock.getTime())+')'
    

#completed 1 repeats of 'trials_2'

trials_2.saveAsPickle(filename+'trials_2')
trials_2.saveAsExcel(filename+'.xlsx', sheetName='trials_2',
    stimOut=trials_2.trialList[0].keys(),
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_2.saveAsText(filename+'trials_2.csv', delim=',',
    stimOut=trials_2.trialList[0].keys(),
    dataOut=['n','all_mean','all_std', 'all_raw'])

#Start of routine instruct_red
t=0; instruct_redClock.reset()
frameN=-1

#update component parameters for each repeat
ready_3 = event.BuilderKeyResponse() #create an object of type KeyResponse
ready_3.status=NOT_STARTED


#keep track of which have finished
instruct_redComponents=[]#to keep track of which have finished
instruct_redComponents.append(instrText_3)
instruct_redComponents.append(ready_3)
for thisComponent in instruct_redComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#start the Routine
continueRoutine=True
while continueRoutine:
    #get current time
    t=instruct_redClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*instrText_3* updates
    if t>=0 and instrText_3.status==NOT_STARTED:
        #keep track of start time/frame for later
        instrText_3.tStart=t#underestimates by a little under one frame
        instrText_3.frameNStart=frameN#exact frame index
        instrText_3.setAutoDraw(True)
    
    #*ready_3* updates
    if t>=0 and ready_3.status==NOT_STARTED:
        #keep track of start time/frame for later
        ready_3.tStart=t#underestimates by a little under one frame
        ready_3.frameNStart=frameN#exact frame index
        ready_3.status=STARTED
        #keyboard checking is just starting
        event.clearEvents()
    if ready_3.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys)>0:#at least one key was pressed
            #abort routine on response
            continueRoutine=False
    
    
    #check if all components have finished
    if not continueRoutine:
        break # lets a component forceEndRoutine
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in instruct_redComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#end of routine instruct_red
for thisComponent in instruct_redComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
try:
    ser = serial.Serial(device, 115200, timeout=1)
    ser.write('[t]\n[t]\n')
    ser.close()
except:
    pass

#set up handler to look after randomisation of conditions etc
trials_3=data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('textC.csv'))
thisTrial_3=trials_3.trialList[0]#so we can initialise stimuli with some values
#abbreviate parameter names if possible (e.g. rgb=thisTrial_3.rgb)
if thisTrial_3!=None:
    for paramName in thisTrial_3.keys():
        exec(paramName+'=thisTrial_3.'+paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    #abbrieviate parameter names if possible (e.g. rgb=thisTrial_3.rgb)
    if thisTrial_3!=None:
        for paramName in thisTrial_3.keys():
            exec(paramName+'=thisTrial_3.'+paramName)
    
    #Start of routine trial
    t=0; trialClock.reset()
    frameN=-1
    
    #update component parameters for each repeat
    try:
        ser = serial.Serial(device, 115200, timeout=1)
        ser.write('[s,{"dev":"eye","cmd":"mark","val":"read '+currentLoop.thisIndex():+'"}]\n')
        ser.close()
    except:
        pass
    
    paragraphs.setText(text)
    resp = event.BuilderKeyResponse() #create an object of type KeyResponse
    resp.status=NOT_STARTED
    print 'begin text ('+str(mainClock.getTime())+')'
    #keep track of which have finished
    trialComponents=[]#to keep track of which have finished
    trialComponents.append(paragraphs)
    trialComponents.append(resp)
    for thisComponent in trialComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #start the Routine
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=trialClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        
        #*paragraphs* updates
        if t>=8 and paragraphs.status==NOT_STARTED:
            #keep track of start time/frame for later
            paragraphs.tStart=t#underestimates by a little under one frame
            paragraphs.frameNStart=frameN#exact frame index
            paragraphs.setAutoDraw(True)
        
        #*resp* updates
        if t>=1 and resp.status==NOT_STARTED:
            #keep track of start time/frame for later
            resp.tStart=t#underestimates by a little under one frame
            resp.frameNStart=frameN#exact frame index
            resp.status=STARTED
            #keyboard checking is just starting
            resp.clock.reset() # now t=0
            event.clearEvents()
        if resp.status==STARTED:#only update if being drawn
            theseKeys = event.getKeys(keyList=['1', 'n'])
            if len(theseKeys)>0:#at least one key was pressed
                resp.keys=theseKeys[-1]#just the last key pressed
                resp.rt = resp.clock.getTime()
                #abort routine on response
                continueRoutine=False
        if (t >= 5):
            visual.ShapeStim(win=win, units='norm', lineWidth=5, lineColor=itemColor, vertices=((.5,.8),(.5,-.8),(-.5,-.8), (-.5,.8))).draw()
        if (t < 5):
            visual.ShapeStim(win=win, units='norm', lineWidth=5, lineColor='gray', vertices=((.5,.8),(.5,-.8),(-.5,-.8), (-.5,.8))).draw()
        
        #check if all components have finished
        if not continueRoutine:
            break # lets a component forceEndRoutine
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]): core.quit()
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #end of routine trial
    for thisComponent in trialComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    try:
        ser = serial.Serial(device, 115200, timeout=1)
        ser.write('[s,{"dev":"eye","cmd":"mark","val":"done"}]\n')
        ser.close()
    except:
        pass
    time.sleep(0.1)
    #check responses
    if len(resp.keys)==0: #No response was made
       resp.keys=None
    #store data for trials_3 (TrialHandler)
    trials_3.addData('resp.keys',resp.keys)
    if resp.keys != None:#we had a response
        trials_3.addData('resp.rt',resp.rt)
    print "key=%s, rt=%f" % (resp.keys,resp.rt)
    print 'end text ('+str(mainClock.getTime())+')'
    

#completed 1 repeats of 'trials_3'

trials_3.saveAsPickle(filename+'trials_3')
trials_3.saveAsExcel(filename+'.xlsx', sheetName='trials_3',
    stimOut=trials_3.trialList[0].keys(),
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_3.saveAsText(filename+'trials_3.csv', delim=',',
    stimOut=trials_3.trialList[0].keys(),
    dataOut=['n','all_mean','all_std', 'all_raw'])

#Start of routine instruct_green
t=0; instruct_greenClock.reset()
frameN=-1

#update component parameters for each repeat
ready_2 = event.BuilderKeyResponse() #create an object of type KeyResponse
ready_2.status=NOT_STARTED


#keep track of which have finished
instruct_greenComponents=[]#to keep track of which have finished
instruct_greenComponents.append(instrText_2)
instruct_greenComponents.append(ready_2)
for thisComponent in instruct_greenComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#start the Routine
continueRoutine=True
while continueRoutine:
    #get current time
    t=instruct_greenClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*instrText_2* updates
    if t>=0 and instrText_2.status==NOT_STARTED:
        #keep track of start time/frame for later
        instrText_2.tStart=t#underestimates by a little under one frame
        instrText_2.frameNStart=frameN#exact frame index
        instrText_2.setAutoDraw(True)
    
    #*ready_2* updates
    if t>=0 and ready_2.status==NOT_STARTED:
        #keep track of start time/frame for later
        ready_2.tStart=t#underestimates by a little under one frame
        ready_2.frameNStart=frameN#exact frame index
        ready_2.status=STARTED
        #keyboard checking is just starting
        event.clearEvents()
    if ready_2.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys)>0:#at least one key was pressed
            #abort routine on response
            continueRoutine=False
    
    
    #check if all components have finished
    if not continueRoutine:
        break # lets a component forceEndRoutine
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in instruct_greenComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#end of routine instruct_green
for thisComponent in instruct_greenComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
try:
    ser = serial.Serial(device, 115200, timeout=1)
    ser.write('[t]\n[t]\n')
    ser.close()
except:
    pass

#set up handler to look after randomisation of conditions etc
trials_4=data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('textD.csv'))
thisTrial_4=trials_4.trialList[0]#so we can initialise stimuli with some values
#abbreviate parameter names if possible (e.g. rgb=thisTrial_4.rgb)
if thisTrial_4!=None:
    for paramName in thisTrial_4.keys():
        exec(paramName+'=thisTrial_4.'+paramName)

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    #abbrieviate parameter names if possible (e.g. rgb=thisTrial_4.rgb)
    if thisTrial_4!=None:
        for paramName in thisTrial_4.keys():
            exec(paramName+'=thisTrial_4.'+paramName)
    
    #Start of routine trial
    t=0; trialClock.reset()
    frameN=-1
    
    #update component parameters for each repeat
    try:
        ser = serial.Serial(device, 115200, timeout=1)
        ser.write('[s,{"dev":"eye","cmd":"mark","val":"read '+currentLoop.thisIndex():+'"}]\n')
        ser.close()
    except:
        pass
    
    paragraphs.setText(text)
    resp = event.BuilderKeyResponse() #create an object of type KeyResponse
    resp.status=NOT_STARTED
    print 'begin text ('+str(mainClock.getTime())+')'
    #keep track of which have finished
    trialComponents=[]#to keep track of which have finished
    trialComponents.append(paragraphs)
    trialComponents.append(resp)
    for thisComponent in trialComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #start the Routine
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=trialClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        
        #*paragraphs* updates
        if t>=8 and paragraphs.status==NOT_STARTED:
            #keep track of start time/frame for later
            paragraphs.tStart=t#underestimates by a little under one frame
            paragraphs.frameNStart=frameN#exact frame index
            paragraphs.setAutoDraw(True)
        
        #*resp* updates
        if t>=1 and resp.status==NOT_STARTED:
            #keep track of start time/frame for later
            resp.tStart=t#underestimates by a little under one frame
            resp.frameNStart=frameN#exact frame index
            resp.status=STARTED
            #keyboard checking is just starting
            resp.clock.reset() # now t=0
            event.clearEvents()
        if resp.status==STARTED:#only update if being drawn
            theseKeys = event.getKeys(keyList=['1', 'n'])
            if len(theseKeys)>0:#at least one key was pressed
                resp.keys=theseKeys[-1]#just the last key pressed
                resp.rt = resp.clock.getTime()
                #abort routine on response
                continueRoutine=False
        if (t >= 5):
            visual.ShapeStim(win=win, units='norm', lineWidth=5, lineColor=itemColor, vertices=((.5,.8),(.5,-.8),(-.5,-.8), (-.5,.8))).draw()
        if (t < 5):
            visual.ShapeStim(win=win, units='norm', lineWidth=5, lineColor='gray', vertices=((.5,.8),(.5,-.8),(-.5,-.8), (-.5,.8))).draw()
        
        #check if all components have finished
        if not continueRoutine:
            break # lets a component forceEndRoutine
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]): core.quit()
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #end of routine trial
    for thisComponent in trialComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    try:
        ser = serial.Serial(device, 115200, timeout=1)
        ser.write('[s,{"dev":"eye","cmd":"mark","val":"done"}]\n')
        ser.close()
    except:
        pass
    time.sleep(0.1)
    #check responses
    if len(resp.keys)==0: #No response was made
       resp.keys=None
    #store data for trials_4 (TrialHandler)
    trials_4.addData('resp.keys',resp.keys)
    if resp.keys != None:#we had a response
        trials_4.addData('resp.rt',resp.rt)
    print "key=%s, rt=%f" % (resp.keys,resp.rt)
    print 'end text ('+str(mainClock.getTime())+')'
    

#completed 1 repeats of 'trials_4'

trials_4.saveAsPickle(filename+'trials_4')
trials_4.saveAsExcel(filename+'.xlsx', sheetName='trials_4',
    stimOut=trials_4.trialList[0].keys(),
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_4.saveAsText(filename+'trials_4.csv', delim=',',
    stimOut=trials_4.trialList[0].keys(),
    dataOut=['n','all_mean','all_std', 'all_raw'])

#Start of routine thanks
t=0; thanksClock.reset()
frameN=-1

#update component parameters for each repeat
#keep track of which have finished
thanksComponents=[]#to keep track of which have finished
thanksComponents.append(thanksText)
for thisComponent in thanksComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#start the Routine
continueRoutine=True
while continueRoutine:
    #get current time
    t=thanksClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*thanksText* updates
    if t>=0.0 and thanksText.status==NOT_STARTED:
        #keep track of start time/frame for later
        thanksText.tStart=t#underestimates by a little under one frame
        thanksText.frameNStart=frameN#exact frame index
        thanksText.setAutoDraw(True)
    elif thanksText.status==STARTED and t>=(0.0+2.0):
        thanksText.setAutoDraw(False)
    
    #check if all components have finished
    if not continueRoutine:
        break # lets a component forceEndRoutine
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#end of routine thanks
for thisComponent in thanksComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)














#Shutting down:
win.close()
core.quit()
