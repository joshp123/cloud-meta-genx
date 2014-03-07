cloud-meta-genx
===============

A system to run GenX reflectivity analysis software automated, in parallel, using a pre-configured cloud/HPC environment, and facilitate meta-optmization.
--------------------------------------------------------------------------------------

#### Scope

This is my Physics BSc project. I was tasked with evaluating the speed, quality and robustness of GenX, a Python tool written by Matts Björck, that fits X-ray and Neutron reflectivity data.

I quickly identified that, while the underlying algorithms and physical models were robust, significant optimizations, improvements and speedups could be made by modifying the software architechture and workflow slightly, to take advantage of recents improvements in cloud computing, parallel computing, and the Free Open Source Software that can be used to build such a foundation.

The aim of this project is to provide a system for automating and offloading processing of x-ray/neutron refelctivity data that is easy to use, easy to configure, easy to deploy, and most importantly: easy to adapt to potential future situation.

#### Architecture + technologies

Since this is 2014 and cloud computing is easy and cheap - we need to design this from the ground up to be easy to deploy and scale. This requires a bit of DevOps voodoo. GenX is cross-platform, but the parallel code struggles on Windows when not in the UI (idk, some horrible thing in python because *nix's fork() isn't on Windows and you have to tag a load of functions and it doens't work). 

Yep, we're using Linux.

However! The helpful thing about GenX is that despite its somewhat crazy structure, ripping out the core modelling code isn't too hard. This means that we just need to offload the __analysis__ to the Linux server - the researcher can still use GenX to set up the fit, parameters, and everything else they want to measure.

So, all we need to worry about is getting a standard Linux config set up that can run our stack - (python, a few scientific python modules, genx itself, and our parallelisation stuff). DevOps and Cloud Computing such as [EC2](http://aws.amazon.com/ec2/) or [DigitalOcean](https://www.digitalocean.com) makes this really easy - you can get a pre-configured Linux Virtual Machine running in the cloud, with a unique IP (and a hostname too). It's also really easy to set up the stack you need - as simple as writing a bash script (or even less with Chef/Ansible/etc).





proj/__init__.py
    /celery.py
    /tasks.py
    
  
  
  
