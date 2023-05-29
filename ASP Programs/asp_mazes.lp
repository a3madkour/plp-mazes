#const t_max = 35.
#const min_solution = 20.
#const max_solution = 35.
#const size = 5.

d(1..size*size).

adjacent(X,Y) :- d(X), d(Y), X-1 = Y, Y \ size > 0.
adjacent(X,Y) :- d(X), d(Y), X+size = Y.
adjacent(X,Y):- adjacent(Y,X).

%%(2 * size) -1 {edge(X,Y):adjacent(X,Y)} 2* (size * size) - (2 * size).
1 {edge(X,Y):adjacent(X,Y)} 2*size*size. 

edge(X,Y) :- edge(Y,X).
path(X,Y) :- edge(X,Y).
path(X,Y) :- edge(X,Z), Y!=Z, path(Z,Y).


:- not path(1,size*size).
:- not path(1,Y),d(Y).
#show edge/2.

#minimize{
edge(X,Y) : d(X), d(Y)
}.