0.5::edge(1,2,0);0.5::edge(1,2,1).
0.5::edge(1,3,0);0.5::edge(1,3,1).
0.5::edge(2,4,0);0.5::edge(2,4,1).
0.5::edge(3,4,0);0.5::edge(3,4,1).


edge(X,Y,V) :- edge(Y,X,V).
path(X,Y) :- edge(X,Y,1).
path(X,Y) :- edge(X,Z,1), Y\=Z, path(Z,Y).


inactive(X,Y) :- edge(X,Y,0).
inactive(X,Y) :- edge(X,Y,1), \+path(X,Z), Z \=Y.

active(X,Y) :- edge(X,Y,1), \+ inactive(X,Y).

evidence(path(1,4)).
query(active(_,_)).
