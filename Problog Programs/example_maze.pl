0.5::edge(1,2,0);0.5::edge(1,2,1).
0.5::edge(1,6,0);0.5::edge(1,6,1).
0.5::edge(2,3,0); 0.5::edge(2,3,1).
0.5::edge(2,7,0); 0.5::edge(2,7,1).
0.5::edge(3,4,0); 0.5::edge(3,4,1).
0.5::edge(3,8,0); 0.5::edge(3,8,1).
0.5::edge(4,5,0); 0.5::edge(4,5,1).
0.5::edge(4,9,0); 0.5::edge(4,9,1).
0.5::edge(5,10,0); 0.5::edge(5,10,1).
0.5::edge(6,7,0); 0.5::edge(6,7,1).
0.5::edge(6,11,0); 0.5::edge(6,11,1).
0.5::edge(7,8,0); 0.5::edge(7,8,1).
0.5::edge(7,12,0); 0.5::edge(7,12,1).
0.5::edge(8,9,0); 0.5::edge(8,9,1).
0.5::edge(8,13,0); 0.5::edge(8,13,1).
0.5::edge(9,10,0); 0.5::edge(9,10,1).
0.5::edge(9,14,0); 0.5::edge(9,14,1).
0.5::edge(10,15,0); 0.5::edge(10,15,1).
0.5::edge(11,12,0); 0.5::edge(11,12,1).
0.5::edge(11,16,0); 0.5::edge(11,16,1).
0.5::edge(12,13,0); 0.5::edge(12,13,1).
0.5::edge(12,17,0); 0.5::edge(12,17,1).
0.5::edge(13,14,0); 0.5::edge(13,14,1).
0.5::edge(13,18,0); 0.5::edge(13,18,1).
0.5::edge(14,15,0); 0.5::edge(14,15,1).
0.5::edge(14,19,0); 0.5::edge(14,19,1).
0.5::edge(15,20,0); 0.5::edge(15,20,1).
0.5::edge(16,17,0); 0.5::edge(16,17,1).
0.5::edge(16,21,0); 0.5::edge(16,21,1).
0.5::edge(17,18,0); 0.5::edge(17,18,1).
0.5::edge(17,22,0); 0.5::edge(17,22,1).
0.5::edge(18,19,0); 0.5::edge(18,19,1).
0.5::edge(18,23,0); 0.5::edge(18,23,1).
0.5::edge(19,20,0); 0.5::edge(19,20,1).
0.5::edge(19,24,0); 0.5::edge(19,24,1).
0.5::edge(20,25,0); 0.5::edge(20,25,1).
0.5::edge(21,22,0); 0.5::edge(21,22,1).
0.5::edge(22,23,0); 0.5::edge(22,23,1).
0.5::edge(23,24,0); 0.5::edge(23,24,1).
0.5::edge(24,25,0); 0.5::edge(24,25,1).
edge(X,Y,V) :- edge(Y,X,V).
path(X,Y) :- edge(X,Y,0).
path(X,Y) :- edge(X,Z,0), Y\=Z, path(Z,Y).
evidence(path(1,2)).
evidence(path(1,3)).
evidence(path(1,4)).
evidence(path(1,5)).
evidence(path(1,6)).
evidence(path(1,7)).
evidence(path(1,8)).
evidence(path(1,9)).
evidence(path(1,10)).
evidence(path(1,11)).
evidence(path(1,12)).
evidence(path(1,13)).
evidence(path(1,14)).
evidence(path(1,15)).
evidence(path(1,16)).
evidence(path(1,17)).
evidence(path(1,18)).
evidence(path(1,19)).
evidence(path(1,20)).
evidence(path(1,21)).
evidence(path(1,22)).
evidence(path(1,23)).
evidence(path(1,24)).
evidence(path(1,25)).

query(edge(_,_,0)).
