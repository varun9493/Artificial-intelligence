sbird(eagle).
bird(penguin).
bird(ostrich).
bird(dodo).
bird(sparrow).
flies(eagle).
flies(sparrow).


can_fly(X) :- bird(X), flies(X).
cannot_fly(X) :- bird(X), \+ flies(X).