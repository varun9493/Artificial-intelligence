planet(mercury).
planet(venus).
planet(earth).
planet(mars).
planet(jupiter).
planet(saturn).
hottest(venus).
largest(jupiter).
smallest(mercury).
rings(saturn).

hotter(X, Y) :- hottest(X), \+ hottest(Y).
larger(X, Y) :- largest(X), \+ largest(Y).
smaller(X, Y) :- smallest(X), \+ smallest(Y).
has_rings(X) :- rings(X).