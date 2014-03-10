# ZFC programming language

# INFORMATION AS A DIMENSION? (it's a projection but a useful one)

"The fundamental problem of communication is that of reproducing at one point, either exactly or approximately, a message selected at another point." - Shannon

well clearly this problem is solved, its a git repo! and git clone.

The entropy, H, of a discrete random variable X is a measure of the amount of uncertainty associated with the value of X.

Joint entropy of (X,Y)

start off modelling an infinite square well

kinetic energy and momentum

mutual information - amount of info that can be obtained about one random variable by observing another


# Kullback–Leibler divergence (information gain)

[example experiment](http://upload.wikimedia.org/math/8/e/7/8e7c3b0f381df46720176d46d72d6160.png "Example ex[eriment")

information theory of bernoulli trial/bernoulli scheme

test: countable direct product -> observable operator -> projection
base space -> observer hilbert space

apply to [meausure (math theory)](http://en.wikipedia.org/wiki/Measure_space#measure_space) all sets: R^n dimensions of space

Technically, a measure is a function that assigns a non-negative real number or +∞ to (certain) subsets of a set X (see Definition below). It must assign 0 to the empty set and be (countably) additive: the measure of a 'large' subset that can be decomposed into a finite (or countable) number of 'smaller' disjoint subsets, is the sum of the measures of the "smaller" subsets. In general, if one wants to associate a consistent size to each subset of a given set while satisfying the other axioms of a measure, one only finds trivial examples like the counting measure. This problem was resolved by defining measure only on a sub-collection of all subsets; the so-called measurable subsets, which are required to form a σ-algebra. This means that countable unions, countable intersections and complements of measurable subsets are measurable. Non-measurable sets in a Euclidean space, on which the Lebesgue measure cannot be defined consistently, are necessarily complicated in the sense of being badly mixed up with their complement. Indeed, their existence is a non-trivial consequence of the axiom of choice

###### The Simplest observable:
```python
def measure(object):
	return ['']

###### The simplest object, a set (a null pointer):
```python
Class FundamentalObject(type, dimensions, R^n, bitmask):
	def __init(self)__:
	# so 0 = fundamental particles, 1 = fermions, bosons, etc
	# init is just a recursive thing on the bitmask until you head down the set-inheretance heirarchy
		return ['']

###### Axioms - write in functional code and then that's the back of this problem broken. this is a final, virtual class - it's not implementation specific at all. axioms are independant of situation

#### SOLID -> MATH

### STRONG/WEAK forces -> strong/weak typing inheretance is gravity?


enum FundamentalTypes:
{
	empty set
}

from [wolfram math world](http://mathworld.wolfram.com/Measure.html): 

>	A measure is defined as a nonnegative real function from a delta-ring F such that
>
>	 m(emptyset)=0, 	
>	(1)
>	where emptyset is the empty set, and
>
>	 m(A)=sum_(n)m(A_n) 	
>	(2)
>	for any finite or countable collection of pairwise disjoint sets (A_n) in F such that A= union A_n is also in F.

this is the most basic observation. stuff is hard b/c its badly mixed up wtih complement? yes, this is because of you being wron  and applying the axiom of choice to ur measurement space in an invalid way - idk like the ether idea of photons or whatever. 

this ALSO aplies to our objects, as they are, after all objects that play by the same rules - except their "self" is the computer

Noether's theorem

ergodic theory, - peturbation of dynamical systems: sin, ln, exp, x^n, complex

entropy -> p ln p units -> (shannon) -> information, order
sin -> (t,) (t,x) // consts wavenumber and http://mathworld.wolfram.com/WaveEquation.html periodic pertubations (dt = planck time)
e^ -> anti-entropy -> also inheretance -> erdos number -> chaos
x^n -> euclidian - just spatial constraints 
complex - weird time - relativity (special/gen->em/strong)

this dimensional analysis applied to core phys F = ma, schroedinger, E= mc^2


do this the lazy way - wolfram - those functions grep each variable print dimensions and name

template interactions - strong/weak/grav/em
compare dimentions (strong has color charge, is weird) (weak h)

superpositions and intersections of the dimensional orders
meta-mathematics

(if u wanna recursively do this based on scipy libs you could i guess)

imperative programming: alalogous to rituals - u dont rly know what ur doin


****


Concepts:
Generative grammar, constant recursion, start off from very basic knowns, dE, dp, hbar, and a certainty related to that? shannon unit? start off from thought experiments

define asimov early on lol. u wanna be safe. also don't instantly hook it up to wikipedia and see what it does do that in a lame duck debug mode lol, thats what skynet taught us.

add ZFC mathematical axioms into the generative grammar and you have the foundations of maths

make your generative grammar easy to use and incorporate this into object oriented programming

stack for more known stuff, heap for less well known stuff - strong/weak

all data is atomic (after all information is just fundamental particles and quantum numbers)

start-up routine should inherently imply +, -, + + = * (iterative addition) from the rules of ZFC + set theory

start off with the empty set object, and self

self for the computer is just its environment but the concept extends to any relative observer (an observer at a given point in minkowski spacetime?)

all events are inherently lorentz transformed (but not much)
dispersion operators on the total entropy of the information field

continous integration, constant verification - blockchain

notes
========

Generative grammar, recursion

start off with one bit of order and one bit of uncertainty

asimov laws (use in prod lol!!!) (disable in debug)

i am a thing
things have energy and momentum 
we exist in 3 dimensions of space (x,y,z) and one of time

equality identicality
operators on information - ban 
factor in favour of h - logarithmic potential vector of h

switch base easily

degree of beleif in a hypothesis - turing

what do i look like from the point of view of ? (self, others, state, potentials, specific areas etc as well as projections)


degrees of freedom and dimensions as opposed to numbers - define a hilbert space and manifold to work in 

plus minus infinity, undefined (1/0) -> null divide by zero to kill

+ to create
- to remove

symmetry laws STRONG/WEAK strong - owned, physically known, certain, hashed, secure, weak - external.
functional programming for strong inputs, weak use imperative programming

environment variables - physical constants

scalar -> vector -> 

one time pad on boot up

GRAMMARS
- imperfect tense - referring to previous state - unfinished
- present tense - now - current instruction pointer + state
- present imperative - let x = y
- "[optative mood](http://en.wikipedia.org/wiki/Optative_mood)" /tense
- retrospective? 

hello, world
in/out

i think, thererfore i am, but i don't know what that is (hbar or whatever, dE, dp)

there is a world around me, i think i can see, hear, feel,

a "problem" "hypothesis" 

what else could i [verb]

i do not know what i am

what am i doing? (runnning proceses) 

where am i (start off at home)

senses?

what is important about?

we think x [is/isn't/tentative]  // tentative and y/n combine? or its a spectrum of certainty? YES

i think [there is] - create a thing

what does x look like [then/now/in the future]

who can i talk to?

say hello to my friend:

what can i go and see?

copy

git commands?