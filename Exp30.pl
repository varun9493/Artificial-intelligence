man(socrates).
man(plato).
woman(xanthippe).
married(socrates, xanthippe).

% Define the rules
mortal(X) :- man(X).
needles(X, Y) :- married(X, Y).

% Define the backward chaining algorithm
rt(KBin, KBout) :- fwd_chain(KBin, KBout, _).

fwd_chain(KB, KB, "nothing to deduce anymore").
fwd_chain(KBin, KBout) :-
    findall(X, (member(Rule, KBin), Rule), Rules),
    apply_rules(Rules, KBin, KBout).

apply_rules([], KB, KB).
apply_rules([Rule|Rest], KBin, KBout) :-
    Rule,
    apply_rules(Rest, KBin, KBout).