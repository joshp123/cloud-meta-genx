Cloud Meta GenX TODO:
==============

MoSCoW priorities:

Must
-----
~~Get GenX working on the server~~ DONE

~~start playbook going~~ DONE

Set up the celery and flower worker thing and the backend STARTED
- debug why its not talking to the backend
- get arbitrary tasks reporting
- then scaffold in GenX

Write the code for the backend reporting ? basically just write to the files asnynchromously? or have a collecting thing idk

Clean up my GenX wrapper code a bit - init method? maybe call docstrings? create an HTML cheatsheet from diff_ev.

Explain GenX structure! hahahaa - this is important it's basically the core of our work

Finish report with scientific language - 3 hours

Keep literally everything in Git - make a fork of original GenX - 10

test an example ansible playbook doing helloworld before trying to run ours - 10

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