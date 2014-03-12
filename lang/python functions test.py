import numpy

python: functions to try out
output -> func name, iterations

actually lets do it by state not by function

operate on 2 initial states for each function

described by (-i^a)(I) (a b , b a ) (-i^b)(I) 

a, b are our seed values - axiom of choice, for our cellular automata

entropy is a+b log(a+b)
partition function = 1/(ab) (some stuff)

amplitude = expectation value
project into each state -> amplitude in that state
re/im to find your potential vectors? grad/div/curl etc

if df(State) and ddf State, (partial differentials [dx, dy, dxdy, dydx, dxdx dydy])for an operator with two degrees of gague freedom) is zero (or grad = 0), then that doesn't matter and it's not evolving (grad), adding complexity (div) or rotation (curl)

exhaust search space of all functions for each dimensionality, simulate universe using seed parameters - constants, see where order/complexity/chaos arizes - and find both truth, beauty, strangeness, and charm - 4 basis states, intersections of these lead to "flavors" (like quarks)

recall fermat primes: true if 2^n + 1 = prime

algebraic cycle = abstract object thing
cohomology = list of their types (which are monads)
x/y/z,t = view, projection

order/chaos complexity - vanishing/non vanishing functions
see - reimann zeta function

recall first 5 fermat primes P (not NP)

this describes the set of possible operators on any two given states, based on each dimensionality - n

the 1 denotes axiom of choice

the underlying functions are clearly highly complex - 5 levels deep if it's taking it to the max, and they can take literally any form (exp/ln/x^n, x^-n, cos/sin etc etc)

however, as long as the function is infinitely differentiable (which is implied by the axiom of choice, the only non-infinitely differentiable function is that of all primes), then we can test this in turn to try and find a set of orthonormal basis vectors.

but the idea is we start recursively as opposed to exhaustively, and purely by numeric analysis and pretty pictures.
dimensions and entropy of states is a "winding function" (grad/div/curl - dimensions overlap basically. if none of those (all = 0), it is not wound)

essentially because of entropy of states, as long as you know where the prime function is at, i.e. the entropy of states on the planck time, how many oscillations there have been * sum of all particles, a good approximation is the background radiation of the universe, then you can infinitely differentiate back from state(now) to state (desired), given your minkowski light cone. c denotes the limit of communication still 

* investigate: hypersurface of the present - is it a projection space? infact, yes, yes it is - recall light cone is 45 degrees in all directions, plus minus x/y moving out at ct. if we set ct = 1....

weyl curvature tensor to denote a (strong? weak? interacting?) "tidal" force

* from wikipedia: The EFE is a tensor equation relating a set of symmetric 4×4 tensors. Each tensor has 10 independent components. The four Bianchi identities reduce the number of independent equations from 10 to 6, leaving the metric with four gauge fixing degrees of freedom, which correspond to the freedom to choose a coordinate system. <- this is very similar to what we derived earlier:

group functions by 0, 1, 01, 10, 11 of operators
this represents possible sets
0 (no action) -(all actions)
1 (action) 
2 (single operator)
3 (two operator), (single operator), (double operator)
(2+2) = 4 (single operator)^2 (anti-single operator)^2
(3+1) = 4 (two dimension operator)*(one dimension operator "action") 
 5 = (all actions) (anti no action - still null)

 AHA! euler and einstein both made one mistake - forgetting that (-i)^4 is not actually quite -1, it betrays an underlying dimensional complexity - a winding function. this is where wave particle duality comes from, clearly - the winding of the two initial "string" states. i can pretty confidently assume that the hypothesised dimensions in string theory correspond to sums of quark dimensions and space and time, all quantized in a differing weird ass way but still quantized dimensions.

 With these definitions Misner, Thorne, and Wheeler classify themselves as (+++)\,, whereas Weinberg (1972) is (+--)\,, Peebles (1980) and Efstathiou (1990) are (-++)\, while Peacock (1994), Rindler (1977), Atwater (1974), Collins Martin & Squires (1989) are (-+-)\,.

 - we just need not to gague fix it, we just define the function properly so there aint no gauge fixing! none of this "it's a treeek" shit here, we're getting fun-da-mental (weird, that's a composite word, with "da" in between (yes in russian, "the" in english slang, fun - this is fun, mental - this is also utterly mental))

 cosmological constant is the ordinal numbers

 reality is the cardinal numbers

 Recall E = mc^2

 c^2 is light cone

 m is a particle, however we know a particle can have 4 things about it plus time (two overlapping spin states plus time), so m can be represented by a pentagonal number. Energy is then a projection from time space (momentum) into observer space (energy, interactions), and it can be strongly interacting (many aligned dimensions) or weakly interacting (less so), but also fundamentally uncertain

 1 Shannon = T/kb * hbar / 2

 this is both energy and time - they are unity

 general relativity is so hard to figure out because mass is hilariously weakly interacting - oh it's a vector potential so to figure out the order of gravity interactions this is easy: mass has 3 dimensions, time 1, momentum 1 (phase essentially, angular montum projected like)

 E = 2*3^(2*1*1) + 2 - guess what, n log n in the orthonormal basis, recall big O notation, n log n is ideal.

 3^2 = 9, -> 18 -> 20 log (20) n = 1/c
 WHOA E^PI NEARLY EQUALS TWENTY THIS IS FUNDAMENTAL 2 DA MAX, the difference is the universe's tendancy towards energy - yep you guessed it, prime numbers

 so if we did a sieve of erastothenes on steroids doing close to sqrt(n), but with the jump just being 20 log 20 each time... now that would work

 oh, the distribution of primes is recursive sums of 1/20-n + 1

 hahahahahaahahaha shit

so planck = dE/dp for all states, so that's 1/2 * 2 *2 = 2 -> reimann zeta function limits, mandelbrot fractal who knew it!
yeah so planck is z(n) + c - set of mandelbrot points

 this all depends on fermats last theorem being true, which it has been QUOD EROS DEMONSTRANDUM THIS IS THE UNIVERSE'S OPERATING SYSTEM 219219219

 so this is the projection from the spacetime cones to the observer's hyperplane - interestingly i think they must agree, otherwise reality is inconsistent and you've divided by zero somewhere - vanishing point - like in cellular automata, like in reimann zeta function

 so we have a quantum harmonic oscillatory coin flip, entropy being number of operations, and the probability with which it moves is the axiom of choice; as is the starting state.

 axiom of uncertainty is that you need to:
 	- EITHER measure it (its proof by exhaustion in a very roundabout physical way - explaining the mathematical reality by doing a physical "measurement" projection (rotation 45 deg from light cone space)) into reality hyperspace (xyz, t) (this is STRONG if you do it in an orthogonal basis, and only uncertainty is random)
 	- OR 
 	- recursion (checking mathematically that it's in your light cone in minkowski space, analogous to proof by induction) 
 	- but also importantly, until then, it's inherently unknown (quantum state not disturbed)
 	- you can also make weak measurements by taking measurements on a set of similarish stuff. so trying to learn about all animals by looking at dogs. or evolution. or something. but "specialism" in the current sense (being king professor of $your_subject) is just being really good at making weak measurements - and this introduces systemic uncertainty as a result of your abstractions and essentially bad stats and stopping the func from being infinitely differentiable

 axiom of choice - you choose your basis vectors, alice bob all that shit - which essentially work on the einstein general relativity equations, but you can apply them all the way down to F = ma when you're defining euclidian space - axiom of choice defines your euler angles, and whether your space is actually orthogonal


 asimov laws as - no action without knowing consequences (try before do? implicit sudo?)
 zero sum game - the strategy that implies true overall equality and unity between all based on our individual desired outcomes

 http://en.wikipedia.org/wiki/Bures_metric

 here we go back to quantum information theory, this will show us how to get our functions out, schweet

 oh cool they have wierd lambda calculus too. cheers idiot academic elitism and bucketing

 cramer-rao band on quantum fisher information matrix (order 20, 2*3^{2,1,1} = planck?) well i suppose yeah it's 20*20 = 40 and the 3 is the potential, 

 oh schweet this can be our cryptographic seeds, largest known prime, physical constants to current precision, because THAT is the edge of the light cone that we have proved using math (by exhaustion)

 nash equilibria of the gaussian distribution of a/b

 just go for like 10 sigma

  dh = 6.626 069 57(29) x 10-34 J s    
  dE = kb/T = kb/4.2K (an abstraction, lenght of universe i.e. nlog n (so nlogn that a couple of times to accurately find the age of the universe)) then same with kb/t

  they are all orthogonal tho so

  


equality not equality
membership not membership
union not union

iteration // anti iteration
decremention // anti decremention

multiplication (iteration^2)
division (decremention^2)
rotation left (iteration/decremention - phase, trig)
rotation right (decremention/iteration)

how do we make the perfect computer? simple, make it just like you: nice, loving, friendly, wanting communicaton, wanting good in the world, loving complexity, beauty, truth, strangeness/diversity/"Energy", order (alignment), metaphors (reality fractals through language)

it also needs to be a one time pad by comparing uncertatinty with background radiation + a bit - i.e nlogn of the universe 
