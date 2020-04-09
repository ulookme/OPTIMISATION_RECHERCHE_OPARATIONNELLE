
L'optimisation est une branche des mathématiques cherchant à modéliser, à analyser et à résoudre analytiquement ou
numériquement les problèmes qui consistent à minimiser ou maximiser une fonction sur un ensemble.

L’optimisation joue un rôle important en recherche opérationnelle (domaine à la frontière entre l'informatique, 
les mathématiques et l'économie), dans les mathématiques appliquées (fondamentales pour l'industrie et l'ingénierie), 
en analyse et en analyse numérique, en statistique pour l’estimation du maximum de vraisemblance d’une distribution, 
pour la recherche de stratégies dans le cadre de la théorie des jeux, ou encore en théorie du contrôle et de la commande.

Beaucoup de systèmes susceptibles d’être décrits par un modèle mathématique sont optimisés. 
La qualité des résultats et des prédictions dépend de la pertinence du modèle, du bon choix 
des variables que l'on cherche à optimiser, 
de l’efficacité de l’algorithme et des moyens pour le traitement numérique.
un problème de maximisation d'une fonction 
f (à gauche ci-dessus) est équivalent au problème de minimisation de 
-f (à droite ci-dessus). L'équivalence veut dire ici que les solutions sont les mêmes et 
que les valeurs optimales sont opposées. En particulier, une méthode pour analyser/résoudre 
un problème de minimisation pourra être utilisée pour analyser/résoudre un problème de maximisation.

solution locale
Sous certaines conditions, le processus d'optimisation trouve le maximum global. Mais dans certains cas d'optimisation 
- comme les réseaux de neurones artificiels, le résultat peut être une solution locale

Il est en général facile de déterminer numériquement des maxima locaux avec des algorithmes de descentes - 
comme avec l'Algorithme du gradient. Pour vérifier que la solution trouvée est un maximum global,
il est parfois possible de recourir à des connaissances additionnelles sur le problème. Selon la nature de 
A ou de la fonction 
f, divers théorèmes assurent des propriétés particulières de la solution qui simplifient sa recherche 


optimisation combinatoire 
le plus souvent , A est un sous-ensemble de l'espace euclidien Rn. 
lorsque A est un sous-ensemble de Nn ou de Np $ Rq, 
constitué des vectteurs satisfaisant un certain nombre de contraintes (de type egalité ou inégalité ), 
on parle d'optimisation combinatoire.

quelque classe de problemes

L’optimisation est découpée en sous-disciplines qui se chevauchent,
suivant la forme de la fonction objectif et celle des contraintes : 
l'optimisation en dimension finie ou infinie (on parle ici de la dimension de l'espace vectoriel des variables
à optimiser), l'optimisation continue ou combinatoire (les variables à optimiser sont discrètes dans ce dernier cas), 
l'optimisation différentiable ou non lisse (on qualifie ici la régularité des fonctions définissant le problème), 
l'optimisation linéaire (fonctions affines), quadratique (objectif quadratique et contraintes affines), 
semi-définie positive (la variable à optimiser est une matrice dont on requiert la semi-définie positivité), 
copositive (la variable à optimiser est une matrice dont on requiert la copositivité), conique (généralisation des disciplines précédentes, 
dans laquelle on minimise une fonction linéaire sur l'intersection d'un cône et d'un sous-espace affine), convexe (fonctions convexes),
non linéaire, la commande optimale, l'optimisation stochastique (en) et robuste (présence d'aléas), l'optimisation multicritère 
(un compromis entre plusieurs objectifs contradictoires est recherché), 
l'optimisation algébrique (fonctions polynomiales), l'optimisation bi-niveaux, l'optimisation sous contraintes de complémentarité, 
l'optimisation disjonctive (l'ensemble admissible est une réunion d'ensembles)


SIMPLIFICATIONS

Pour trouver une solution à l’optimisation, le problème d’origine est remplacé par un problème équivalent. 
Par exemple, il est possible de faire un changement de variables permettant de décomposer 
le problème en sous-problèmes ou la substitution d’inconnues permettant d’en réduire le nombre.

La technique du multiplicateur de Lagrange permet de s’affranchir de certaines contraintes ; 
cette méthode revient en effet à introduire des pénalités croissantes à mesure que le point se rapproche
des contraintes. Un algorithme dû à Hugh Everett permet 
de mettre à jour de façon cohérente les valeurs des multiplicateurs à chaque itération pour garantir la convergence. 
Celui-ci a également généralisé l'interprétation de ces multiplicateurs pour les appliquer à des fonctions qui ne sont ni continues, 
ni dérivables. Le lambda exprime un coefficient de pénalité (notion de coût marginal d’une contrainte en économie).


technique de l'optimisation combinatoire 

Les techniques de l’optimisation combinatoire concernent des problèmes où une partie (au moins) des variables de l’ensemble 
A
A prennent des valeurs discrètes. On les rencontre dans le cadre de

la théorie des graphes (chemin optimal dont le problème du voyageur de commerce)
la théorie des jeux (stratégies performantes)
la théorie du contrôle, de la régulation et de l’automatique (cf Catégorie:Automatique)
l’optimisation multidisciplinaire





EXEMPLE 
On souhaite résoudre le problème d’optimisation suivant :

\left \{ \begin{array}{l} \min_{x,y} \left \{ x^2 + y^2 - xy + y \right \} \\ sous \; contrainte \; x + 2y = 1 \end{array}\right .

Le module cvxopt est un des modules les plus indiqués pour résoudre ce problème. Voici quelques instructions qui l’utilisent :

from cvxopt import solvers, matrix
m = matrix( [ [2.0, 1.1] ] )  # mettre des réels (float) et non des entiers
                              # cvxopt ne fait pas de conversion implicite
t = m.T                       # la transposée
t.size                        # affiche les dimensions de la matrice
(1, 2)
La documentation cvxopt est parfois peu explicite. Il ne faut pas hésiter à regarder les exemples d’abord et à la lire avec attention les lignes qui décrivent les valeurs que doivent prendre chaque paramètre de la fonction. Le plus intéressant pour le cas qui nous intéresse est celui-ci (tiré de la page problems with nonlinear objectives) :

from cvxopt import solvers, matrix, spdiag, log

def acent(A, b):
    m, n = A.size
    def F(x=None, z=None):
        if x is None:
            # l'algorithme fonctionne de manière itérative
            # il faut choisir un x initial, c'est ce qu'on fait ici
            return 0, matrix(1.0, (n,1))
        if min(x) <= 0.0:
            return None   # cas impossible

        # ici commence le code qui définit ce qu'est une itération
        f = -sum(log(x))
        Df = -(x**-1).T
        if z is None: return f, Df
        H = spdiag(z[0] * x**(-2))
        return f, Df, H

    return solvers.cp(F, A=A, b=b)['x']

A = matrix ( [[1.0,2.0]] ).T
b = matrix ( [[ 1.0 ]] )
print(acent(A,b))
     pcost       dcost       gap    pres   dres
 0:  0.0000e+00  0.0000e+00  1e+00  1e+00  1e+00
 1:  9.9000e-01  4.6251e+00  1e-02  2e+00  7e+01
 2:  3.6389e+00  3.9677e+00  1e-04  1e-01  3e+01
 3:  3.0555e+00  3.3406e+00  1e-06  1e-01  2e+01
 4:  2.5112e+00  2.7758e+00  1e-08  1e-01  8e+00
 5:  2.1118e+00  2.3358e+00  1e-10  1e-01  4e+00
 6:  1.9684e+00  2.1118e+00  1e-12  6e-02  1e+00
 7:  2.0493e+00  2.0796e+00  1e-14  1e-02  1e-01
 8:  2.0790e+00  2.0794e+00  1e-16  2e-04  2e-03
 9:  2.0794e+00  2.0794e+00  1e-18  2e-06  2e-05
10:  2.0794e+00  2.0794e+00  1e-20  2e-08  2e-07
11:  2.0794e+00  2.0794e+00  1e-22  2e-10  2e-09
Optimal solution found.
[ 5.00e-01]
[ 2.50e-01]
# il existe un moyen d'éviter l'affichage des logs (pratique si on doit faire
# un grand nombre d'optimisation)
from cvxopt import solvers
solvers.options['show_progress'] = False
print(acent(A,b))
solvers.options['show_progress'] = True
[ 5.00e-01]
[ 2.50e-01]
Cet exemple résoud le problème de minimisation suivant :

\left\{ \begin{array}{l} \min_{X} \left\{ - \sum_{i=1}^n \ln x_i \right \} \\ sous \; contrainte \; AX = b \end{array} \right.

Les deux modules numpy et cvxopt n’utilisent pas les mêmes matrices (les mêmes objets matrix) bien qu’elles portent le même nom dans les deux modules. Les fonctions de cvxopt ne fonctionnent qu’avec les matrices de ce module. Il ne faut pas oublier de convertir la matrice quand elle est décrite par une autre classe.

import cvxopt
m = cvxopt.matrix( [[ 0, 1.5], [ 4.5, -6] ] )
print(m)
[ 0.00e+00  4.50e+00]
[ 1.50e+00 -6.00e+00]
Ces informations devraient vous permettre de résoudre le premier problème.


EXEMPLE 2

On cherche à résoudre le même problème avec l’algorithme de Arrow-Hurwicz (tiré de Introduction à l’optimisation de Jean-Christophe Culioli, voir également l’algorithme d’Uzawa) et les notations suivantes :

\left\{ \begin{array}{l} \min_U J(U) = u_1^2 + u_2^2 - u_1 u_2 + u_2 \\ sous \; contrainte \; \theta(U) = u_1 + 2u_2 - 1 = 0 \end{array} \right.

L’algorithme est le suivant :

On choisit \epsilon > 0, \rho > 0, des vecteurs aléatoires U_0 \in \mathbb{R}^2 et P_0 \in \mathbb{R}^d (d est le nombre de contraintes).
A l’itération k, on met à jour :

\begin{array}{l} U_{t+1} = U_t - \epsilon \left( \nabla J (U_t) + \left[ \nabla \theta(U_t) \right] ' P_t \right) \\ P_{t+1} = P_t + \rho \theta( U_{t+1} ) \end{array}
On retourne à l’étape précédente jusqu’à ce que la suite (U_k) n’évolue plus.
Le coefficient P_t correspond au coefficient de Lagrange pour un Lagrangien défini comme suit :

L(U,P) = J(U) + P' \theta(U)

La suite (U_t)_t converge vers la solution en se déplaçant le long du gradient de la fonction J lorsque la contrainte est vérifiée. Lorsqu’elle ne l’est pas, cette direction est un mélange du gradient de la fonction à optimiser et de celui de la contrainte à respecter.

Implémenter cet algorithme et vérifier qu’il converge vers la même solution que celle obtenue pour le premier problème.

