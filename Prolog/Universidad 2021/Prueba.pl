oracion(Numero) --> fraseNominal(Numero), fraseVerbal(Numero).
fraseVerbal(Numero) --> verbo(Numero), fraseNominal(Numero1).
fraseNominal(Numero) --> determinante(Numero), sustantivo(Numero).
determinante(singular)--> [a].
determinante(plural)--> [some].
determinante(singular)--> [the].
determinante(plural)--> [the].
sustantivo(singular)-->[cat].
sustantivo(plural)-->[mice].
verbo(singular)-->[scares].
verbo(plural)-->[scare].
verbo(singular)-->[hates].
verbo(plural)-->[hate].

/*oracion(singular,[the,cat,hates,some,mice],[]).*/



