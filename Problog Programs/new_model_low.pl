d(1).
0.440842787682334::edge(1,2,0); 0.559157212317666::edge(1,2,1).
0.891410048622366::edge(1,6,0); 0.108589951377634::edge(1,6,1).
d(2).
0.3322528363047::edge(2,3,0); 0.6677471636953::edge(2,3,1).
0.774716369529984::edge(2,7,0); 0.225283630470016::edge(2,7,1).
d(3).
0.424635332252836::edge(3,4,0); 0.575364667747164::edge(3,4,1).
0.807131280388979::edge(3,8,0); 0.192868719611021::edge(3,8,1).
d(4).
0.392220421393841::edge(4,5,0); 0.607779578606159::edge(4,5,1).
0.815235008103728::edge(4,9,0); 0.184764991896272::edge(4,9,1).
d(5).
0.86385737439222::edge(5,10,0); 0.13614262560778::edge(5,10,1).
d(6).
0.327390599675851::edge(6,7,0); 0.672609400324149::edge(6,7,1).
0.810372771474878::edge(6,11,0); 0.189627228525122::edge(6,11,1).
d(7).
0.325769854132901::edge(7,8,0); 0.674230145867099::edge(7,8,1).
0.803889789303079::edge(7,12,0); 0.196110210696921::edge(7,12,1).
d(8).
0.341977309562399::edge(8,9,0); 0.658022690437601::edge(8,9,1).
0.758508914100486::edge(8,13,0); 0.241491085899514::edge(8,13,1).
d(9).
0.374392220421394::edge(9,10,0); 0.625607779578606::edge(9,10,1).
0.790923824959481::edge(9,14,0); 0.209076175040519::edge(9,14,1).
d(10).
0.849270664505673::edge(10,15,0); 0.150729335494327::edge(10,15,1).
d(11).
0.316045380875203::edge(11,12,0); 0.683954619124797::edge(11,12,1).
0.855753646677472::edge(11,16,0); 0.144246353322528::edge(11,16,1).
d(12).
0.46515397082658::edge(12,13,0); 0.53484602917342::edge(12,13,1).
0.753646677471637::edge(12,17,0); 0.246353322528363::edge(12,17,1).
d(13).
0.390599675850891::edge(13,14,0); 0.609400324149109::edge(13,14,1).
0.696920583468395::edge(13,18,0); 0.303079416531605::edge(13,18,1).
d(14).
0.403565640194489::edge(14,15,0); 0.596434359805511::edge(14,15,1).
0.690437601296596::edge(14,19,0); 0.309562398703404::edge(14,19,1).
d(15).
0.782820097244733::edge(15,20,0); 0.217179902755267::edge(15,20,1).
d(16).
0.356564019448947::edge(16,17,0); 0.643435980551053::edge(16,17,1).
0.824959481361426::edge(16,21,0); 0.175040518638574::edge(16,21,1).
d(17).
0.444084278768233::edge(17,18,0); 0.555915721231767::edge(17,18,1).
0.808752025931929::edge(17,22,0); 0.191247974068071::edge(17,22,1).
d(18).
0.538087520259319::edge(18,19,0); 0.461912479740681::edge(18,19,1).
0.706645056726094::edge(18,23,0); 0.293354943273906::edge(18,23,1).
d(19).
0.479740680713128::edge(19,20,0); 0.520259319286872::edge(19,20,1).
0.674230145867099::edge(19,24,0); 0.325769854132901::edge(19,24,1).
d(20).
0.841166936790924::edge(20,25,0); 0.158833063209076::edge(20,25,1).
d(21).
0.789303079416532::edge(21,22,0); 0.210696920583468::edge(21,22,1).
d(22).
0.761750405186386::edge(22,23,0); 0.238249594813614::edge(22,23,1).
d(23).
0.769854132901134::edge(23,24,0); 0.230145867098865::edge(23,24,1).
d(24).
0.837925445705024::edge(24,25,0); 0.162074554294976::edge(24,25,1).
d(25).
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
