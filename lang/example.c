#include "stdio.h"

Formal systems in mathematics consist of the following elements:

A finite set of symbols (i.e. the alphabet), that can be used for constructing formulas (i.e. finite strings of symbols).
A grammar, which tells how well-formed formulas (abbreviated wff) are constructed out of the symbols in the alphabet. It is usually
required that there be a decision procedure for deciding whether a
formula is well formed or not.
A set of axioms or axiom schemata: each axiom must be a wff.
A set of inference rules.

// TODO: sql bindings for data manipulation
// YAML: for model 

// set imperative algo and recursive algo off at the same time - compute a nash equilibria for any given situation
// imperative so you can be lazy and inaccurate, but potentially quick if you have a shortcut for a high entropy situation
// recursive so you can be accurate (i think proper recursion would always be faster tho, especially if you bitshift the pointers)

// bitshift +/- for ptr++ operations

// i = known unknown, what is sqrt(i) - i.e. truely unknowable - fundamental unit of uncertainty
// i is self - you are fundamentally uncertain as a thing, reality is not infinitely knowable

// grad / div / curl == 1,0, (0,1) ?? probably not its probably a pauli matrix but
// these are probably relevant as inspection operators - grad/div/curl describes the set theory of the operators? the domain? i.e. all the special cases

// empty set is inherently uncertain? or certain? it's herently BOTH axiom of choice

// pauli matrices of uncertainty based on your level of certainty

// algorithms of number theory (model), set theory (view?), and controller (manifolds?) + uncertainty


// primes as most fundamental
// print "primes are a set. all primes have no more than 2 divisors, themself, and unity (self.divide) by (primes.factors) to give results in a list (numbers.primespair)"

// Monads are a code abstraction of metaphors - rules, lists, structures, arrangments: repeated nested structures
// monads are a representation of a thing, at i guess nothing we see truely is real
// metaphor as polymorphic object


// LINK: basic metaphor of infinity, potential infiinty https://www.t-kougei.ac.jp/research/pdf/vol2-27-06.pdf
// hyperfunctions


struct emptySet
{
	// the most fundamental empty set from ZFC set theory.
	// In the idea of a Euclidian/Hilbert space, this is a 0 x 0 space.
	// basic spcaes should be able to be defined as a
	int certainty; // likelihood? starts with 1 for empty set, as it is fudamental in zfc? who knows what initial values are. it is there tho. (it'll be pauli matrices)
	int uncertainty;
	int phase; // if uncertainty and certainty are out of phase, reality is inconsistent
	//stdev vs variance
	uint long64 time_created; // unix epoch style

	// i think certainty/uncertainty/phase is euler's formula projected onto on the empty set (cardinal 0) (shannon 1)
};

int main(int argc, char const *argv[]) // optional turing head start location (i.e. arbritary entry point), after all, that is just a subset of the program
{
	// i know that i am here and now
	// the schroedinger/heisenberg joke - echo that

	signed int cardinal = 0; // position
	signed int next = 1
	// momentum - this isn't a number, it's a vector potential with an uncertainty
	// for example, there's always some infinitely unlikely event that could stop 
	// our confidence in the uniformity principle, negative direction because
	// potentials are inverse functions
	// 	uncertainty on both is hbar

	signed int todo = 0; // stick other instructions here if we want to start up with any out of the box (later: argv it)

	// background quantum vacuum: infinitely spaced set of uncertain uncertain empty sets, each with certain uncertainty rotating with t,
	// \partial entropy (shannon) \partial  
	// quantum vaccum fluction


	// while time is still continuous (EOF or BREAK to "stop time" for good), see what we should do next
	// special case of next being undefined (or rather, at what case, time, WOULD it be undefined)
	// is the halting problem. we say fuck it. 
	// WAIT BUT NO! time is discrete, the universe must have a clock speed. the universe is probably
	// infinitely parallel, but also atomic and uncertain (planck time), so while everything might have
	// started off at t = 0, we can't rely on all the particles being in sync at any one time without verifying it

	while (next != 1/0 && next != 219): // special "interrupt"
		fork() // fork with self to simulate background quantum vaccuum - on a computer, this IS the background radiation (and the uncertainty )
	// it needs to be a hamiltonean operating (with a CSRNG) on all states
	// stack is known knowns 
	// addressed heap is unknown - stuff we are working with but don't fully know yet (until we have fully traversed its memory)
	// cores as dimensions - parallel processing - race conditions/threadlocks, concurrency as uncertainty of time? clock? syncs? simultaneity?

	// outside addressed space is outside "our universe" - we can only interact with "other universes" using APIs - networking, stdin, stdout, stderr, (gague bosons?)

	// spam as background radiation, known unknowns
	// dark matter as unknown unknowns - we have no idea really. uncertain 2 da max. we know it has a bunch of mass but that's it (so negative potential entropy)
	// we can use inlined asserts to test the nature of reality - checking the background radiation of ourself, the heap (which we can interfere with)
	// and thus quantify our hyperbolic uncertainty as it varies with time - this is skynet i think
	// inherently self aware of what it knows and what it does not know

	// shared reality is the blockchain like in bitcoin except really it's a hash of the work function you did with specific IO (and maybe separate hashes for each)

    // Exceptions:
	// throw "P, program finished", "NP, program failed to finish" "Don't know (certainty threshold) (zero but tends to 1 as ], count to infinity,
    // get something thats not there (/0)
	//execution time tends to t equals infinity, i.e. the heat death of the universe or w/e")
	// assert failed: something in the back reality state history doesn't equal what it should

	return 0; 
}

transistor: ternary branching - P, NP, PNP NP NP NPNP = i^2 - 1  - godel incompleteness

measure a thing (for each sub thing in thing)
					return thing (all pointers to things) - this is the identity matrix

do a thing (update)


try a thing 


get rid of a thing

Kronecker Delta
DOWNLOAD Mathematica Notebook
The simplest interpretation of the Kronecker delta is as the discrete version of the delta function defined by

 delta_(ij)={0   for i!=j; 1   for i=j. 