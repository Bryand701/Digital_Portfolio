/*
Autor: Bryand Brenes Z��iga 2018093347

Ejemplo de uso: parser('C:/Users/bryan/Downloads/Programaci�nLogica/arbol.txt').

El c�digo para leer el txt se sac� de: https://www.lawebdelprogramador.com/foros/Prolog/528147-COMO-ABRO-UN-ARCHIVO-EN-PROLOG.html
El codigo para splis: https://www.swi-prolog.org/pldoc/man?predicate=split_string/4
Atom chars: https://www.swi-prolog.org/pldoc/man?predicate=atom_chars/2
read_file('C:/Users/bryan/Downloads/Programaci�nLogica/arbol.txt', CharList).
*/

read_file(File, CharList):-see(File),
	                   read_list(X),
	                   seen,
                           atom_chars(Y,X),
                            split_string(Y, "\n", "\s\t\n", CharList).

% read_list(-List)
%  Reads characters from the the input
%  it reaches an eof.
read_list([Char | List]):-get0(Char),
	                  Char =\= -1,
			  !,
			  put(Char),
			  read_list(List).
read_list([]).

registro(R) :- R == "R0".
registro(R) :- R == "R1".
registro(R) :- R == "R2".
registro(R) :- R == "R3".
registro(R) :- R == "R4".
registro(R) :- R == "R5".
registro(R) :- R == "R6".
registro(R) :- R == "R7".
registro(R) :- R == "R8".
registro(R) :- R == "R9".
registro(R) :- R == "R10".
registro(R) :- R == "R11".
registro(R) :- R == "R12".
registro(R) :- R == "R13".
registro(R) :- R == "R14".
registro(R) :- R == "R15".

p(P):-P =="add".
p(P):-P =="sub".
p(P):-P =="and".
p(P):-P =="or".
p(P):-P =="xor".
p(P):-P =="sar".
p(P):-P =="slr".
p(P):-P =="shl".
p(P):-P =="ror".

pb(P):- P == "inc".
pb(P):- P == "ainv".
pb(P):- P == "mov".
pb(P):- P == "testle".
pb(P):- P == "teste".

t1(T):- T == "ld".
t1(T):- T == "st".
t1(T):- T == "swap".

t2(T):- T == "push".
t2(T):- T == "pop".

t3(T):- T == "ldi".

t4(T):- T == "lsr".

b(B):- B == "jmp".
b(B):- B == "jc".
b(B):- B == "jnc".
b(B):- B == "call".

v(V):- V == "testc".
v(V):- V == "testn".
v(V):- V == "tests".
v(V):- V == "testo".


linea(Linea) :- split_string(Linea, "\s", "\s",[P,Registros]),
    p(P) ,split_string(Registros, ",", "\s",LRegistros),
    verificarRegistroP(LRegistros).

linea(Linea) :- split_string(Linea, "\s", "\s",[P,Registros]),
    pb(P) ,split_string(Registros, ",", "\s",LRegistros),
    verificarRegistroPB(LRegistros).

linea(Linea) :- split_string(Linea, "\s", "\s",[T,Registros]),
    t1(T) , verificarRegistroT1(Registros).

linea(Linea) :- split_string(Linea, "\s", "\s",[T,Registros]),
    t2(T) ,split_string(Registros, ",", "\s",LRegistros),
    verificarRegistroT2(LRegistros).

linea(Linea) :- split_string(Linea, "\s", "\s",[T,Registros]),
    t3(T) ,verificarRegistroT3(Registros).

linea(Linea) :- split_string(Linea, "\s", "\s",[T]),
    t4(T).

linea(Linea) :- split_string(Linea, "\s", "\s",[B,_]),
    b(B).

linea(Linea) :- split_string(Linea, ":", "\s",[B,Linea2]),
    B==B, linea(Linea2).

linea(Linea) :- split_string(Linea, "\s", "\s",[V]),
    v(V).


verificarRegistroP([]).
verificarRegistroP(Registros):-count(Registros,N),
    N==3.

verificarRegistroPB([]).
verificarRegistroPB(Registros):-count(Registros,N),
    N==2.

verificarRegistroT1([]).
verificarRegistroT1(Registros):-split_string(Registros, "\s,()", "\s()",[R1,N,R2]),registro(R1),registro(R2),atom_number(N,_).

verificarRegistroT1(Registros):-split_string(Registros, "\s,()", "\s()",[R1,N,R2]),registro(R1),registro(R2), N==N.

verificarRegistroT2([]).
verificarRegistroT2(Registros):-count(Registros,N),
    N==1.

verificarRegistroT3([]).
verificarRegistroT3(Registros):-split_string(Registros, "\s,", "\s()",[R1,N]),registro(R1),atom_number(N,_).


count([],0).
count([H|Tail], N) :-
    count(Tail, N1),
    (  registro(H)
    -> N is N1 + 1
    ;  N = N1 + 10
    ).

parser(Direccion):-read_file(Direccion, ListaLineas),
    revision(ListaLineas).

revision([]).
revision([Head|Tail]):-linea(Head),
    revision(Tail).
