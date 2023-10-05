%! Una solución al problema de las ocho reinas

solucion([]).
solucion([X/Y | Otras]) :-          % La primera reina esta en X/Y, las demás en Otras
   solucion(Otras),
   member(Y,[1,2,3,4,5,6,7,8]),
   noataca(X/Y, Otras).             % La primera reina no ataca a las otras
   
noataca(_, []).
noataca(X/Y, [X1/Y1 | Otras]) :-
   Y =\= Y1,
   Y1 - Y =\= X1 - X,
   Y1 - Y =\= X - X1,
   noataca(X/Y, Otras).
   
plantilla([1/Y1,2/Y2,3/Y3,4/Y4,5/Y5,6/Y6,7/Y7,8/Y8]).

reinas(S) :- plantilla(S), solucion(S).
