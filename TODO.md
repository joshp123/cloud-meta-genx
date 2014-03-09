Cloud Meta GenX TODO/ROADMAP:
==============


## MILESTONES:

1) PRE-ALPHA CONCEPT: genX analysis from browser, spits out CSV
	* get a demo up, don't worry about self-deploying yet
	* make sure this is live @ genx.joshpalmer.co.uk before deadline
2) ALPHA: upload a .GX, and .py scripts, push butan get data
	* finish report here, add latex/pdf to git to include the report in the repo
	* update documentation
3) BETA1: sexy graphs
	* get bokeh working
4) BETA2: parallel dispacthing
	* play with celery more (low priority as long as 1 instance works, linearity is not that much of a drawback=)


MoSCoW priorities:

Must
-----
~~Get GenX working on the server~~ DONE 

~~start playbook going~~ DONE

make a meta-programming framework for using GenX with a 
yaml bindings from diffev public methods to a YAML file

Could make a parser thing to gen one from a model but lol

maybe a meta-programming class to inspect the methods and vars and export them to a yaml thing?
print([m for m in dir(simple) if not m.startswith('__')])

ok this is where the getters and setters might actually be useful lol

another meta-pgoramming thing to go YAML -> python but that's probably just on the server (although should have an interface)

Set up the celery and flower worker thing and the backend STARTED
- debug why its not talking to the backend
- get arbitrary tasks reporting
- then scaffold in GenX

http://skuld.bmsc.washington.edu/scatter/AS_form.html - steal gnuplot shit

conceptualise our data for bokeh graphing - what are we plotting, against what, and why (could add gavin's fitting code)

Write the code for the backend reporting ? basically just write to the files asnynchromously? or have a collecting thing idk

Clean up my GenX wrapper code a bit - init method? maybe call docstrings? create an HTML cheatsheet from diff_ev.

Explain GenX structure! hahahaa - this is important it's basically the core of our work

Finish report with scientific language - 3 hours

Keep literally everything in Git - make a fork of original GenX - 10

test an example ansible playbook doing helloworld before trying to run ours - 10

mention that 90% of our time was theoretical architecture work, reading, structuring things out, analysis, building a mental model (this is why i have no lab book just a git repo- its hard to document)

Should
------

Sort GenX into 2 proper classes - wrapper, looper [wrapper exposes GenX api so its extensible and documented, use VS] - 30 mins

Project structured better - 30 

References on the Report - 2 hours

More numbers and graphs - 1 hour

LaTeX the report - 1 hour

Sperg out on a tech spec discussion thing? mini white paper of the tech side?

Could
-----

File struct: 
/README.MD > make a quicy snyposis, link to our other files (github pages version links?)
/ABOUT.MD > more wikify ? dont replicate pages content - maybe quick overview 1 click install batteries included readme, about is more in depth
/FUTURE.MD > merge known issues
/SETUP.MD


Document things hahahaha

Tidy up wrapper classes to take arguments better and be more OO

Set up a non-root user so you're not 

Finish off the pages/wiki for submission


Won't
--------

strip out unused UI code (it just pads the git clone and looks ugly in lib folder)

get it to plot the spectra like GenX does on the server (this would own, it uses matplotlib too so you can do it on the webs woop)