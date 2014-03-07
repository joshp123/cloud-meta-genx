cloud-meta-genx
===============

A parallel, highly scalable framework for cloud computation of X-ray/Neutron reflectivity fitting data.
--------------------------------------------------------------------------------------

X-ray and Neutron diffraction/refelctivity techniques are a very useful scientific tool for probing small structures. There is already good software out there to analyse it: [GenX](http://genx.sourceforge.com) is a [FOSS](http://en.wikipedia.org/wiki/Free_and_open-source_software), graphical based tool, written in Python, that is used by [lots of researchers!](http://genx.sourceforge.net/publ.html).

However, with a bit of clever thinking and modern distributed cloud computing, this can be hugely sped up - we reckon it's very feasible to get fully real time data analysis, without spending hilarious amounts on EC2 instances either.

We've taken the powerful core of GenX, and basically just ripped out the UI, automated the button pushing, and separated that out into a reusable task that we can easily run in parallel (and at huge scale). This is the same tech used by CERN and the LHC who handle a hilarious amount of data, and it works pretty well for them (we passed on the C++ and MySQL though, yuk!)

We've designed this from the ground up to fit in well with the way researchers are already working. So, our tool takes existing `.gx` files, straight from the GenX GUI. This means a reasearcher can set up some fitting parameters as normal in GenX, decide what to measure, then simply by saving the file and running `$ meta_genx start_sever example_fit.gx example_tests.py`. 

There's only a small amount of configuration to tell the server what to analyse, and this just a quick Python script - most scientists are fairly familiar with Python already, so we hope this is really easy to use.

Contents
----

* Scope
  * GenX
  * Potential speedups
* Architecture and techs
  * Stack
  * Program components and structure
* How can I use this?
  * Pre-reqs (a linux VM I guess)
  * Getting meta-genx
  * First run
  	* Cloud? HPC? Local?
  * Initialising the server 
  * Uploading a .gx file using WebSockets
 * Future Improvements:
   * Must
   * Should
   * Could
   * Won't


#### Scope

This is my Physics BSc project. I was tasked with evaluating the speed, quality and robustness of GenX, a Python tool written by Matts Björck, that fits X-ray and Neutron reflectivity data.

I quickly identified that, while the underlying algorithms and physical models were robust, significant optimizations, improvements and speedups* could be made by modifying the software architechture and workflow slightly, to take advantage of recents improvements in cloud computing, parallel computing, and the Free Open Source Software that can be used to build such a foundation.

*in the case of a small fit, up to 2 orders of magnitude on a desktop computer (so this is before any cloud speedups too)

The aim of this project is to provide a system for automating and offloading processing of x-ray/neutron refelctivity data that is easy to use, easy to configure, easy to deploy, and most importantly: easy to adapt to potential future situation.

#### Architecture + technologies

Since this is 2014 and cloud computing is easy and cheap - we need to design this from the ground up to be easy to deploy and scale. This requires a bit of DevOps voodoo. GenX is cross-platform, but the parallel code struggles on Windows when not in the UI (idk, some horrible thing in Python because *nix's `fork()` isn't on Windows and you have to tag a load of functions and it doens't work). 

Yep, we're using Linux.

However! The helpful thing about GenX is that despite its somewhat crazy structure, ripping out the core modelling code isn't too hard. This means that we just need to offload the __analysis__ to the Linux server - the researcher can still use GenX to set up the fit, parameters, and everything else they want to measure.

So, all we need to worry about is getting a standard Linux config set up that can run our stack - (python, a few scientific python modules, genx itself, and our parallelisation stuff). DevOps and Cloud Computing such as [EC2](http://aws.amazon.com/ec2/) or [DigitalOcean](https://www.digitalocean.com) makes this really easy - you can get a pre-configured Linux Virtual Machine running in the cloud, with a unique IP (and a hostname too). It's also really easy to set up the stack you need - as simple as writing a bash script (or even less with Chef/Ansible/etc).

This is handled in `whatever.sh` idk

##### Stack of techs
* debian linux
* chef ?
* digitalocean ? or aws? probably digitalocean its easier
* celery, paralell dispatching
* rabbitMQ - broker for celery
* 
* my classes for automating it

##### Project structure

* config/initialisation chef deploy thing basically pipe a config script to our cloud host
..* set up modules
..* start celery server and flower
..* some ssh stuff maybe
..* option to just start crunching data and spin down when done? (later)

```
metGenX/start/start_server.sh
             /stop_server.sh
             /server_stack_setup.sh  # this configures the environment - modify to tweak packages/modules etc
             
```

* my example classes wrapping GenX for use with celery in parallel

```
metaGenX/celery/__init__.py
               /celery.py
               /tasks.py
               /headless_genx.py # TODO: make proper python classes from these
               /headless_looper.py
```
* genx modules themselves (slightly swearily tweaked during the 3 months it took me to hack it all together lol)

```
metaGenX/lib/GenX/*

# diff here of my modifications
```



### Deployment, configuration and use.


- git clone it on a unix box i'll do windows later
- set up your ssh keys or a password or local machine
- fire it up with init
- a) send it some tasks thru a web browser?
- b) define it first in code then monitor in the web
- idk about this


## FUTURE IMPROVEMENTS:
(will finish in exchange for degree credit :P )
- swarmops - spin it out to give it a backend for optimization, meta optimization and metametaoptimization (atm research er has to define the meta-optimization and meta-meta-optimization search space- this is inefficent)
- documentation hahahaahahahahaha
- bugfixes (parallel)
- better parallel (idk if it properly scales for _n_ Core architectures)
  
  
  
