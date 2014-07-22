import time
from my_headless_genx import *
import sys
#from multiprocessing import Process, freeze_support

# Mutation schemes implemented
#self.mutation_schemes = [self.best_1_bin, self.rand_1_bin,\
#    self.best_either_or, self.rand_either_or, self.jade_best, self.simplex_best_1_bin]

def loop(lim = 10):
    for x in xrange(0,lim):
        genx = GenX()
        genx.optimize()
        with open('looperlog.txt', 'a') as log:
            log.write('run' + genx.diffev_solver.get_create_trial() +  repr(time.clock()))
            # also log method and frequency and paramters idk
    return

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print 'Running with %s repeats' % sys.argv[1]
        loop(int(sys.argv[1]))

    
    #freeze_support()
    #Process(target = loop).start()
        




