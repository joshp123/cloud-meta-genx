GenX Architecture and structre
==============================

####_Insights gained from analysis of GenX to help further dev work_

I guess this is a code reveiw against best practices - SOLID, GRASP, and various software development "anti-patterns" (dumb things programmers still do).

This is basically the hard bit of being a developer. If you don't think a bunch about conceptualizing your code and fitting it in with SOLID

Put simply, the book shows newcomers to OOA/D how to "think in objects" - 

Larman - "the critical design tool for software development is a mind well educated in design principles. It is not the UML or any other technology." <- word
Larman, Craig (2005) [2004]. Applying UML and Patterns – An Introduction to Object-Oriented Analysis and Design and Iterative Development (3rd ed.). New Jersey: Prentice Hall. ISBN 0-13-148906-2.

AGILE AS FUCK
- reserach the hell out of your techs
- test/spec/milestone driven development
- think hard before writing code (kinda like with physics, dont just dive in or you'll have no idea what you're doing an not a full scope of the problem)


(and make your dev easy)

This analysis was basically the core of the BSc project. It really doesn't *look* like a whole lot of work - yes, Josh, you pored through a lot of hard source code for a while and complained about how it sucked and the tools sucked and so on. In terms of SLOC written, sure, but dissecting the programs architecture, workflow and potential improvements was much easier to do when just ripping it out and trying to hack it together.

The alternative approach was to go through it with a fine toothcomb, 
GenX Strucuture:

- diffev.py module
	- this is where the diffev magic happens. this class contains all the logic for setting up a diffev fit, including the config
	- this is literally like 1200 lines long (eek) so open it up in a Real IDE - I spent a couple of weeks trying to figure out what the hell was going on using just Sublime Text - it was completely impossible to conceptualize, just because - get [VisualStudio Tools for Python](https://pytools.codeplex.com/wikipage?title=PTVS%20Installation)  (it's freely available, stick it in a [free windows VM](http://modern.ie)
- model.py module 

- LOTS AND LOTS AND LOTS of UI Code. Lots of really complicated UI code.\
	- This is one function, `start_fit`, from the event_handlers.py module:
	'''python
	def start_fit(frame, event):
    '''start_fit(frame, event) --> None
    
    Event handler to start fitting
    '''
    if frame.model.compiled:
        #try:
        #    frame.solver_control.StartFit()
        #except modellib.GenericError, e:
        #    raise e
        #    ShowModelErrorDialog(frame, str(e))
        #    frame.main_frame_statusbar.SetStatusText('Error in fitting', 1)
        #except Exception, e:
        #    raise e
        #    ShowErrorDialog(frame, str(e))
        #    frame.main_frame_statusbar.SetStatusText('Fatal Error', 1)
        #else:
        #    frame.main_frame_statusbar.SetStatusText('Fitting starting ...', 1)
        frame.solver_control.StartFit()
    else:
        ShowNotificationDialog(frame, 'The script is not compiled, do a'\
        ' simulation before you start fitting.')
	'''

	Yeah. This specific file is 1126 lines long, and contains like the entire UI backend code without any subclassing or separation of concerns. Some of the functions have docstrings, but the variables don't, and are are all named weird. Gross.

	There's also 

	CRITIQUE AGAINST SOLID

	DONT PLANG UIs - ITS SLOW AND SHITTY AND BAD 
	and slows you the fuck down
	basically this problem here (its slow as balls) is a) it's python b) the frameworks suck c) the code is a spaghetti mess, seeing 

	The hard bit is to try and figure out what's going on underneath: this starts a fit using a bunch of UI callbacks, but where's the programming object that we want to rip out - ideally we want an object that does the actual differential evolution.


