/**
 * Programación Logica Grupo 1
 * Tecnologico de Costa Rica, Sede Central
 * Integrantes:
 *   Abraham Meza Vega - 2018168174
 *   Bryand Brenes Zúñiga - 2018093347
 */

 /* Ejercicio 1a */

 % Expresión regular: ^[+-]?[0-9]+\.[0-9]+([eE][+-]?[0-9]+)?$

 /* Ejercicio 1b */

 final(s3).
 final(s5).

 trans(s1, +, s2) :- !.
 trans(s1, -, s2) :- !.
 trans(s1, 0, s2) :- !.
 trans(s1, 1, s2) :- !.
 trans(s1, 2, s2) :- !.
 trans(s1, 3, s2) :- !.
 trans(s1, 4, s2) :- !.
 trans(s1, 5, s2) :- !.
 trans(s1, 6, s2) :- !.
 trans(s1, 7, s2) :- !.
 trans(s1, 8, s2) :- !.
 trans(s1, 9, s2) :- !.

 trans(s2, 0, s2) :- !.
 trans(s2, 1, s2) :- !.
 trans(s2, 2, s2) :- !.
 trans(s2, 3, s2) :- !.
 trans(s2, 4, s2) :- !.
 trans(s2, 5, s2) :- !.
 trans(s2, 6, s2) :- !.
 trans(s2, 7, s2) :- !.
 trans(s2, 8, s2) :- !.
 trans(s2, 9, s2) :- !.
 trans(s2, '.', s3) :- !.

 trans(s3, 0, s3) :- !.
 trans(s3, 1, s3) :- !.
 trans(s3, 2, s3) :- !.
 trans(s3, 3, s3) :- !.
 trans(s3, 4, s3) :- !.
 trans(s3, 5, s3) :- !.
 trans(s3, 6, s3) :- !.
 trans(s3, 7, s3) :- !.
 trans(s3, 8, s3) :- !.
 trans(s3, 9, s3) :- !.
 trans(s3, e, s4) :- !.
 trans(s3, 'E', s4) :- !.

 trans(s4, +, s5) :- !.
 trans(s4, -, s5) :- !.
 trans(s4, 0, s5) :- !.
 trans(s4, 1, s5) :- !.
 trans(s4, 2, s5) :- !.
 trans(s4, 3, s5) :- !.
 trans(s4, 4, s5) :- !.
 trans(s4, 5, s5) :- !.
 trans(s4, 6, s5) :- !.
 trans(s4, 7, s5) :- !.
 trans(s4, 8, s5) :- !.
 trans(s4, 9, s5) :- !.

 trans(s5, 0, s5) :- !.
 trans(s5, 1, s5) :- !.
 trans(s5, 2, s5) :- !.
 trans(s5, 3, s5) :- !.
 trans(s5, 4, s5) :- !.
 trans(s5, 5, s5) :- !.
 trans(s5, 6, s5) :- !.
 trans(s5, 7, s5) :- !.
 trans(s5, 8, s5) :- !.
 trans(s5, 9, s5) :- !.

 /* Ejercicio 1c */

 acepta(Estado, []) :- !, final(Estado).

 acepta(Estado, [S|Resto]) :- !, trans(Estado,S,Estado1),
                              acepta(Estado1, Resto).

 acepta(Estado, Hilera) :- acepta(Estado1, Hilera).

 correcto1() :- Estado = s1, Hilera = [-,3,1,8,'.',2,4], acepta(Estado,Hilera).
 correcto2() :- Estado = s1, Hilera = [+,5,'.',0,1,0,1], acepta(Estado,Hilera).
 correcto3() :- Estado = s1, Hilera = [0,'.',2,4,'E',+,1], acepta(Estado,Hilera).
 correcto4() :- Estado = s1, Hilera = [3,'.',1,4,1,5,9,e,-,3], acepta(Estado,Hilera).
 correcto5() :- Estado = s1, Hilera = [4,3,4,3,4,'.',2,1,'E',4,3], acepta(Estado,Hilera).
 correcto6() :- Estado = s1, Hilera = [1,8], acepta(Estado,Hilera).
 correcto7() :- Estado = s1, Hilera = ['.',4,4,5], \+ acepta(Estado,Hilera).
 correcto8() :- Estado = s1, Hilera = [0,'.'], \+ acepta(Estado,Hilera).
 correcto9() :- Estado = s1, Hilera = [1,'.',4,'E'], \+ acepta(Estado,Hilera).

 /* Ejercicio 4a */

iniciaSucesion(guillermo_I,masculino,reino,no_ingles,normandia,diciembre_25_1066).
info(guillermo_II,guillermo_I,masculino,reino,ingles,normandia,setiembre_9_1087).
info(enrique_I,guillermo_I,masculino,reino,ingles,normandia,agosto_5_1100).
info(adela,guillermo_I,femenino,no_reino,no_ingles,normandia,no_aplica).
info(esteban,adela,masculino,reino,no_ingles,blois,diciembre_22_1135).
info(matilda,guillermo_I,femenino,no_reino,ingles,normandia,no_aplica).
info(enrique_II,matilda,masculino,reino,no_ingles,plantagenet,diciembre_19_1154).
info(ricardo_I,enrique_II,masculino,reino,ingles,plantagenet,julio_6_1189).
info(juan,enrique_II,masculino,reino,ingles,plantagenet,abril_6_1199).
info(enrique_III,juan,masculino,reino,ingles,plantagenet,octubre_28_1216).
info(eduardo_I,enrique_III,masculino,reino,ingles,plantagenet,noviembre_20_1272).
info(eduardo_II,eduardo_I,masculino,reino,ingles,plantagenet,julio_8_1307).
info(eduardo_III,eduardo_II,masculino,reino,ingles,plantagenet,febrero_1_1372).
info(eduardo_BP,eduardo_III,masculino,no_reino,ingles,plantagenet,no_aplica).
info(juan_de_gante,eduardo_III,masculino,no_reino,no_ingles,plantagenet,no_aplica).
info(leonel_de_antwerp,eduardo_III,masculino,no_reino,no_ingles,plantagenet,no_aplica).
info(ricardo_II,eduardo_BP,masculino,reino,no_ingles,plantagenet,junio_21_1377).
info(enrique_IV,juan_de_gante,masculino,reino,ingles,lancaster,setiembre_30_1399).
info(joan_beaufort,juan_de_gante,femenino,no_reino,no_ingles,lancaster,no_aplica).
info(john_beaufort_C,juan_de_gante,masculino,no_reino,no_ingles,lancaster,no_aplica).
info(john_beaufort_D,john_beaufort_C,masculino,no_reino,ingles,lancaster,no_aplica).
info(margaret_beaufort,john_beaufort_D,femenino,no_reino,ingles,tudor,no_aplica).
info(cecily_neville,joan_beaufort,femenino,no_reino,ingles,york,no_aplica).
info(enrique_V,enrique_IV,masculino,reino,ingles,lancaster,marzo_21_1431).
info(enrique_VI,enrique_V,masculino,reino,ingles,lancaster,agosto_31_1422).
info(eduardo_IV,cecily_neville,masculino,reino,no_ingles,york,marzo_4_1461).
info(eduardo_V,eduardo_IV,masculino,reino,ingles,york,abril_9_1483).
info(ricardo_III,cecily_neville,masculino,reino,ingles,york,junio_25_1483).
info(enrique_VII,margaret_beaufort,masculino,reino,ingles,tudor,agosto_22_1485).
info(enrique_VIII,enrique_VII,masculino,reino,ingles,tudor,abril_21_1509).
info(margarita,enrique_VII,femenino,reino,ingles,tudor,enero_14_1502).
info(jaime_V_de_Escocia,margarita,masculino,reino,no_ingles,estuardo,setiembre_9_1513).
info(maria_estuardo,jaime_V_de_Escocia,femenino,reino,no_ingles,estuardo,agosto_19_1561).
info(eduardo_VI,enrique_VIII,masculino,reino,ingles,tudor,enero_28_1547).
info(maria_I,enrique_VIII,femenino,reino,ingles,tudor,julio_6_1553).
info(isabel_I,enrique_VIII,femenino,reino,ingles,tudor,noviembre_17_1558).
info(jaime_I,maria_estuardo,masculino,reino,ingles,estuardo,junio_19_1567).
info(carlos_I,jaime_I,masculino,reino,no_ingles,estuardo,marzo_27_1625).
info(isabel_estuardo,jaime_I,femenino,reino,no_ingles,estuardo,noviembre_4_1619).
info(sofia_de_hanover,isabel_estuardo,femenino,no_reino,no_ingles,palatinado_simmern,no_aplica).
info(carlos_II,carlos_I,masculino,reino,ingles,estuardo,mayo_29_1660).
info(jaime_II,carlos_I,masculino,reino,ingles,estuardo,febrero_6_1685).
info(maria_II,jaime_II,femenino,reino,ingles,estuardo,febrero_13_1689).
info(ana,jaime_II,femenino,reino,ingles,estuardo,mayo_1_1707).
info(jorge_I,isabel_estuardo,masculino,reino,no_ingles,hannover,agosto_1_1714).
info(jorge_II,jorge_I,masculino,reino,no_ingles,hannover,junio_11_1727).
info(federico,jorge_II,masculino,no_reino,no_ingles,hannover,no_aplica).
info(jorge_III,federico,masculino,reino,ingles,hannover,octubre_25_1760).
info(jorge_IV,jorge_III,masculino,reino,ingles,hannover,enero_29_1820).
info(eduardo_de_kent,jorge_III,masculino,no_reino,ingles,hannover,no_aplica).
info(guillermo_IV,jorge_III,masculino,reino,ingles,hannover,junio_26_1830).
info(victoria,eduardo_de_kent,femenino,reino,ingles,hannover,junio_20_1837).
info(eduardo_VII,victoria,masculino,reino,ingles,sajonia_coburgo_y_gotha,enero_22_1901).
info(jorge_V,eduardo_VII,masculino,reino,ingles,sajonia_coburgo_y_gotha,mayo_6_1910).
info(eduardo_VIII,jorge_V,masculino,reino,ingles,windsor,enero_20_1936).
info(jorge_VI,jorge_V,masculino,reino,ingles,windsor,diciembre_11_1936).
info(isabel_II,jorge_VI,femenino,reino,ingles,windsor,febrero_6_1952).

 /* Ejercicio 4b */

ancestro(X,Z,G,R,I,C,F) :- info(X,Z,G2,R2,I2,C2,F2), iniciaSucesion(Z,G,R,I,C,F).
ancestro(X,Z,G,R,I,C,F) :- info(X,Y,G2,R2,I2,C2,F2), ancestro(Y,Z,G,R,I,C,F).


/*Ejercicio 2a
[3,/,4,-,/,3,/,8]
*/

/* Ejercicio 2 b*/


 final(s9).

 natural(0).
 natural(N) :-N>0, M is N - 1, natural(M).


 trans_abaco(s1, N, s2) :- natural(N).

 trans_abaco(s2, /, s3) .

 trans_abaco(s3, N, s4) :- natural(N).

 trans_abaco(s4, +, s5) .
 trans_abaco(s4, -, s5) .

 trans_abaco(s5, /, s6) .

 trans_abaco(s6, N, s7) :- natural(N).

 trans_abaco(s7, /, s8) .

 trans_abaco(s8, N, s9) :- natural(N).

/* Ejercicio 2 c*/

acepta(Estado, []) :- final(Estado).

acepta(Estado, [S|Resto]) :-  trans_abaco(Estado,S,Estado1),
                              acepta(Estado1, Resto).
/*-------------------------------------------------------------*/

/*Ejercicio 3a*/


/*inst Ejercicio 3a
Ejemplo del llamado turing([1,1,1,+,1,1,=],N)*/


inst(q0,1,q0,1,der).
inst(q0,+,q1,1,simSum).
inst(q1,1,q1,1,sum).
inst(q1,=,qf,=,detener).

/*inst del Ejercicio 3b
Ejemplo del llamado turing([1,1,1,-,1,=],N)*/
inst(q0,-,q2,1,simRest).
inst(q2,1,q2,1,rest).
inst(q2,=,qf,=,detener).


/*inst del Ejercicio 3c
Ejemplo del llamado turingMul([1,1,1,*,1,1],N)*/

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

turing(CintaActual, CintaFinal) :-
    ejecute(q0, [], CintaActual, Ls, Rs),
    append(Rs,Ls , CintaFinal).

ejecute(qf, Ls, Rs, Ls, Rs) :- !.
ejecute(Q0, Ls0, Rs0, Ls, Rs) :-
    simbolo(Rs0, SimboloLeido, RsRest),
    once(inst(Q0, SimboloLeido, Q1, NuevoSimb, Action)),
    accion(Action, Ls0, [NuevoSimb|RsRest], Ls1, Rs1),
    ejecute(Q1, Ls1, Rs1, Ls, Rs).


/*Ejercicio 3c turing*/

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


/*accion Ejercicio 3a*/
accion(sum, Ls0, [Sym|Rs], [Sym|Ls0], Rs).
accion(simSum,Ls0, [_|Rs], Ls0, Rs).

/*accion Ejercicio 3b*/
accion(rest, [_|Ls0], [_|Rs], Ls0, Rs).
accion(simRest,Ls0, [_|Rs], Ls0, Rs).

/*accion Ejercicio 3b*/

izq([], Rs0, [], [v|Rs0]).
izq([L|Ls], Rs, Ls, [L|Rs]).


limpiar([C|Lista],NLista):-C =='*',
    append(Lista, [], ListaTemp),
    limpiar(ListaTemp,NLista).
limpiar(Lista,Lista).
