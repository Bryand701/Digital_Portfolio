/*Ejercicio 3C
Ejemplo del llamado turing([1,1,1,*,1,1,1],N).*/

 inst_mul(q0,*,q0,*,der).
 inst_mul(q0,1,q1,*,der).

 inst_mul(q1,1,q1,1,der).
 inst_mul(q1,*,q2,*,der).

 inst_mul(q2,1,q3,*,der).
 inst_mul(q2,*,q7,*,der).

 inst_mul(q3,1,q3,1,der).
 inst_mul(q3,*,q4,*,der).
 inst_mul(q3,v,q4,*,der).

 inst_mul(q4,1,q4,1,der).
 inst_mul(q4,*,q5,1,izq).
 inst_mul(q4,v,q5,1,izq).

 inst_mul(q5,*,q6,*,izq).
 inst_mul(q5,1,q5,1,izq).

 inst_mul(q6,1,q10,1,izq).
 inst_mul(q6,*,q7,*,izq).

 inst_mul(q7,*,q7,*,izq).
 inst_mul(q7,v,qf,*,detener).
 inst_mul(q7,1,q8,1,der).

 inst_mul(q8,*,q9,*,der).

 inst_mul(q9,*,q9,1,der).
 inst_mul(q9,1,q11,1,izq).

 inst_mul(q10,1,q10,1,izq).
 inst_mul(q10,*,q2,*,der).

 inst_mul(q11,*,qf,*,detener).
 inst_mul(q11,1,q14,*,izq).

 inst_mul(q14,1,q14,1,izq).
 inst_mul(q14,*,q12,*,izq).

 inst_mul(q12,*,qf,*,detener).
 inst_mul(q12,1,q13,1,izq).

 inst_mul(q13,*,q0,*,der).
 inst_mul(q13,1,q13,1,izq).

% Simulador

turingMul(CintaActual, CintaFinal) :-
    ejecuteMul(q0, [], CintaActual, Ls, Rs),
    reverse(Ls, Ls1),
    append(Ls1, Rs, Temp),
    limpiar(Temp,CintaFinal).

ejecuteMul(qf, Ls, Rs, Ls, Rs) :- !.
ejecuteMul(Q0, Ls0, Rs0, Ls, Rs) :-
    simbolo(Rs0, SimboloLeido, RsRest),
    once(inst_mul(Q0, SimboloLeido, Q1, NuevoSimb, Action)),
    accion(Action, Ls0, [NuevoSimb|RsRest], Ls1, Rs1),
    ejecuteMul(Q1, Ls1, Rs1, Ls, Rs).

simbolo([], v, []).
simbolo([Simb|Rs], Simb, Rs).

accion(izq, Ls0, Rs0, Ls, Rs) :- izq(Ls0, Rs0, Ls, Rs).
accion(detener, Ls, Rs, Ls, Rs).
accion(der, Ls0, [Sym|Rs], [Sym|Ls0], Rs).

izq([], Rs0, [], [v|Rs0]).
izq([L|Ls], Rs, Ls, [L|Rs]).

limpiar([C|Lista],NLista):-C =='*',
    append(Lista, [], ListaTemp),
    limpiar(ListaTemp,NLista).
limpiar(Lista,Lista).
