GenX Architecture and structre (methods/conclusions parallels)
==============================

####_Insights gained from analysis of GenX to help further dev work_

essentially looking at software from this angle of: 
a) best practices
b) OO-design and principles (SOLID GRASP MCV)
c) modularity (unix philosohpy)

... is actually incredibly powerful, and, when applied using "thought experiments" to theoretical physics, has given me some incredibly promising hypotheses/theories in the fundamental nature of reality (think Godel's incompleteness theorems, ZFC-set theory, and modelling the information theory of reality as a multi-dimensional Hilbert-Space, using the complex topology manifolds by studying edge cases (asymptotes or physical extremes) to make implications about the underlying dimensionality and number strucutre. You can prop it up with applying some philosophical meta-physics, quantum mechanics, )

These ideas are incredibly fascinating, but unfortunately i have to do this BSc project thing first, so are out of the scope of this (still, this project taught me an insane amount of full stack knowledge. watch this space.) If the hypotheses hold, and reality is somewhat-trivially computable as long as you do it properly, this has huge advances towards the (hypothesised) [technological singularity] as proposed by John von Neumann in 1958. (Current estimates reckon about 2040 - I'm pretty sure it will be 2020 if we give it a good shot. The future is already here: it's just not very evenly distributed (William Gibson - _Neuromancer_)).

Using a "what-if?" thought experiment to guess the potential benefits to an "ideal world" (in the spherical cow sense, obviously) of taking a bigger picture view really emphasises the principles of "getting it right first time", and constantly building on your knowledge.
If I just improved a few lines of code related to the specific implementations of these algorithms in GenX, if I was lucky, this could provide a single valuable insight into the study of X-rays in a couple of situations, but probably wouldn't. It'd also take a while and be pretty boring too. 

On the other hand, using software dev experience, paired with a rigorous analysis of the system from first principles, similarly to how calculus and quantum mechanics started off (well ish but you get the idea), can reveal a more fundamental insight: but if you estabish general principles (software best practices, paired with standard physical numerical methods of analysis), then you can make something potentially more profound.

This is exactly what I've tried to do here. The current shortcomings of GenX are pretty common to all scientific software and current analysis tools: they're hard to set up, hard to use, break a lot, aren't well documented, the underlying code is a horrible mess, and they're frankly ugly as all hell (compare your average scientific). This isn't particularly inherent, it's just because scientists have gone and learned the skills to develop these tools on a one off basis - so haven't been exposed to the really useful recent learning in software development practices. Physicsists know how to think, software engineers apply that thinking in a rigourous conceptual analytical way (think Lagrangian mechanics, dynamics of systems, constraints), and know how to put that thinking into making stuff. One thing both software and physics people are also really bad at is user centric design: if you're writing software from a technical point of view, the technical abilities are more important to you than how the user will interact with this. Unforunately, being easy for human beings to use is really important. Nobody in their right mind uses linux as their daily computer - doing everything through a text based interface is utterly insane, and not how humans work - we need visual, auditory, kinetic stimulation - staring at text and equations is not a good way to inteprete information or data. Nobody embodies this attitude more than the hugely inspirational Steve Jobs. His brilliant computing insight was to blend technical wisdom and robustness with liberal arts: making beautiful computers, software and hardware that people love to use, and freeing them from the irritation of having to janitor technical aspects

(full disclosure: this entire project was written on a late 2013 13" Macbook Pro running OS X with 2x external displays for a total of about 8 million pixels of screen space. It's an amazing computer platform, and genuinely wouldn't have been possible without Steve, the user-friendly philosophy and trickle-down effects into userspace make using a UNIX-backed OS X computer shockingly powerful, flexible, and easy to adapt a mental model to - the power of the human centric design really lets your mental model map very directly onto what you're doing, and it looking pretty means you'll actually want to use the tools to write code/do physics: they're almost fun.)

I guess this is a code reveiw against best practices - SOLID, GRASP, MVC and various software development "anti-patterns" (dumb things programmers still do).

This is basically the hard bit of being a developer. If you don't think a bunch about conceptualizing your code and fitting it in with SOLID

Put simply, the book shows newcomers to OOA/D how to "think in objects" - 

Larman - "the critical design tool for software development is a mind well educated in design principles. It is not the UML or any other technology." <- word
Larman, Craig (2005) [2004]. Applying UML and Patterns – An Introduction to Object-Oriented Analysis and Design and Iterative Development (3rd ed.). New Jersey: Prentice Hall. ISBN 0-13-148906-2.

AGILE AS FUCK
- reserach the hell out of your techs
- test/spec/milestone driven development
- think hard before writing code (kinda like with physics, dont just dive in or you'll have no idea what you're doing an not a full scope of the problem)

(and make your dev easy)

http://en.wikipedia.org/wiki/Aspect-oriented_programming

LACK OF MVC ARCH FUCKED IT
- view should be your POS lab compuuter
- model should be in a database
- controller should live on a server (but be pure code that you can spin up)

SPERGING ABOUT SOFTWARE DEV

- add some stuff about the hilarious SLOC/file in GenX
- maybe functions/classes static code analysis (but basically its an antipattern)

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


