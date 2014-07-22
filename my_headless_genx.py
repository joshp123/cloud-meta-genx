import data, model, diffev, parameters
import random
import time
import threading
import os

class GenX:

    def log_results(self, solver):

        values = solver.best_vec.copy()

        # write our values to a CSV
        # later add stopping generation
        method = solver.get_create_trial()
        with open('output_' + method + '.csv', 'a') as file:
            # add a time stamp and header line)
            line = ''
            for value in values:
                line = line + repr(value) + ","
                # toodo trim trailing column

                # here you log the actual fit parameters

            line = line + repr(solver.fom) + ","
            # lol dont forget the separators !!!
            line = line + repr(solver.gen) + ","
            time2 = time.clock()
            timeTaken = (time2 - self.time1)
            #print 'Time taken: %r \t %r' % (timeTaken, (timeTaken * 5))

            line = line + '%0.3f' % (timeTaken * 5)

  
            print method

            # measure rate of convergence

            fomlog_path = 'fomlog_' + method + '.csv'
            if (not os.path.exists(fomlog_path)) or (os.stat(fomlog_path).st_size < 102400L):
            # do a fom log to a different file, method based on the string that we're using
            # give up if it's larger than 100kb cos i dont care after that

                with open(fomlog_path, 'a') as log:

                    for fom in solver.fom_log[:,1]:
                        log.write(repr(fom) + ',')
                
                    log.write("\n")

            file.write(line + '\n')
            print 'all done!!'
            return
        
        
        #check Values for data structure

        # append

        # finish timing in callback function because diffev author is retarded and loves fucking callbacks


    # should really start the timer here

    def __init__(self):
        self.time1 = time.clock()
        path = 'Ni\Ni x-ray fitted.gx'

        unix = False
        if not os.path.exists(path):
            # this is a hilariously lazy test for OS X/Linux/Unix* lixes
            path = 'Ni/Ni x-ray fitted.gx'
            unix = True

        # path to my .gx file
    
        self.diffev_solver = diffev.DiffEv()
        self.diffev_solver.model.load(path)
        self.diffev_solver.pickle_load(self.diffev_solver.model.load_addition('optimizer'))
    
        # do we need config? unsure. who cares.

        mutation_schemes = ['best_1_bin', 'rand_1_bin',\
            'best_either_or', 'rand_either_or', 'jade_best', 'simplex_best_1_bin']

        method = self.diffev_solver.set_create_trial(mutation_schemes[4])
    
        #(yes we do)
    
        # get params, modify, set params
        params = parameters.Parameters()
        params = self.diffev_solver.model.get_parameters()
            
        data = params.get_data()
    
        # randomize params \pm 10% to test your fit or whatever
    
        for param in data:
            variance = (0.9 + (random.random() * 0.2))
            param[1] = param[1] * variance

        # put the parameters back
    
        self.diffev_solver.model.parameters.set_data(data)
    
        self.diffev_solver.model.simulate()
        #self.diffev_solver.model.compile_script()   # ??? #dont do this i dont think
    
        # override config here beacuse this is retarded idk
    
        self.diffev_solver.use_max_generations = True
        self.diffev_solver.max_generations = 100
    
        # WINDOWS IS FUCKING GARBAGE SO THIS WILL BREAK LOL
        if unix:
            self.diffev_solver.set_use_parallel_processing(True)
            self.diffev_solver.set_processes(4)
    
    
        # start timer + fit
        self.model = self.diffev_solver.get_model()

    
        # tell the solver to actually spit out the results somewhere (our log_results func)
        self.diffev_solver.set_fitting_ended_func(self.log_results)
        print 'headless genx object set up ready to do your bidding'
        #return self

    def optimize(self):
        self.diffev_solver.init_fitting(self.model)
        self.diffev_solver.init_fom_eval()
        self.diffev_solver.optimize()
        return

    # finish timer

    # record values + time

    #if __name__ == "__main__":
    #    some_rlock = threading.RLock()
    #    with some_rlock:
    #        main()
    #        print 'done'
    #        #time.sleep(60)

    def __exit__(self, type, value, traceback):
        pass

    def __enter__(self):
        if not self.diffev_solver:
            self.init()
        else:
            pass