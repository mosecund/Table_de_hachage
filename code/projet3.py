"""
Nom : Secundar
Prénom : Ismael
Matricule : 504107
Projet 3 d'algo
"""
from random import random
from math import log

class DictOpenAddressing:
    """
    Chainage à adressage ouvert
    Une amélioration a été faite pour marquer un élément
    lors d'une suppression ou d'une recherche

    """
    def __init__(self, m):
        self.T = [None] * m                     # on initialise une table avec des None
        self.m = m                              # on récupère la taille maximale de stockage
        self.n = 0                              # on initialise la taille des clés
        self.indicator = [False]*m              # indique si on est deja passé
    def __len__(self):
        return self.n
    @property
    def load_factor(self):
        """
        Permet de trouver le facteur de charge
        :return:
        """
        return self.n / self.m                  # on divise le nombre de clé présent par la capacité maximale
    def h1(self, k):
        """
        Hachage 1
        :param k:
        :return:
        """
        h = 0
        for i in k:
            h += ord(i)                         # on convertis en chiffre chaque charactère

        return h

    def h2(self, k):
        """
        Hachage é
        :param k:
        :return:
        """
        h = 0x1505

        for i in k:
            h += 33 * h + ord(i)

        return h

    def insert(self, k, v):
        """
        Permet d'ajouter un élément
        :param k:
        :param v:
        :return:
        """
        h1 = self.h1(k)                                     # on stock le hachage 1 dans une variable
        h2 = self.h2(k)                                     # on stock le hachage 2 dans une variable
        j = 0                                               # on initialise le nombre de boucle à 0
        while j < len(self.T):                              # tant que le compteur est inférieur à la taille du tableau
            idx = (h1 + j * h2) % self.m                    # on stock le calcul pour l'indice dans une variable
            if self.T[idx] is None or self.T[idx][0] == k:  # si la case est libre ou si la clé est déjà présente
                if self.T[idx] is None:                     # si c'est le cas on augmente la taille des clés
                    self.n += 1
                self.T[idx] = (k, v)                        # sinon on insère juste la clé et l'élément en question
                                                            # l'ancienne valeur sera écrasée par la nouvelle
                break                                       # on reprend avec le while
            j += 1                                          # on incrémente l'indice pour essayer un autre endroit

        else:
            raise OverflowError("La table est pleine")      # sinon on soulève une erreur pour dire qu'il n'y plus de
                                                            # place

    def search(self, k):
        """
        Permet de rechercher un clé
        :param k:
        :return:
        """
        h1 = self.h1(k)                                     # on stock le hachage 1 dans une variable
        h2 = self.h2(k)                                     # on stock le hachage 2 dans une variable
        j = 0                                               # on initialise le nombre de boucle à 0
        flag = True
        idx_old = (h1 + j*h2) % self.m
        while j < len(self.T):                              # tant que le compteur est inférieur à la taille du tableau
            if self.T[idx_old] == None and self.indicator[idx_old] == False:    # si il n'y a rien à cette case
                break

            if flag == True and self.indicator[idx_old] == True:    # si on a marqué la case
                flag = False
                idx_new = idx_old

            if self.T[idx_old] != None and self.T[idx_old][0] == k :# si on trouve la clé qu'on recherche
                temp = self.T[idx_old]
                if not flag :
                    self.T[idx_old] = None
                    self.T[idx_new] = temp

                return temp[1]                   # on renvoie la valeur

            j += 1                               # on incrémente l'indice et on recommence
            idx_old = (h1 + j * h2) % self.m
        raise KeyError(f"Clef inconnue {k}")     # si la clé n'est pas dans la table on renvoie une erreur

    def delete(self, k):
        """
        Pour supprimer un élémént dans la table
        :param k:
        :return:
        """
        h1 = self.h1(k)                                     # on stock le hachage 1 dans une variable
        h2 = self.h2(k)                                     # on stock le hachage 2 dans une variable
        j = 0                                               # on initialise le nombre de boucle à 0
        idx = (h1 + j * h2) % self.m
        while j < len(self.T) and self.T[idx] != None:      # tant que le compteur est inférieur à la taille du tableau
                                                            # on stock le calcul pour l'indice dans une variable
            if self.T[idx][0] == k:                         # si on a trouvé la case qu'on veut supprimer
                self.n -= 1                                 # on décrémente la taille des clés dans le tableau
                self.indicator[idx] = True                  # on marque la case
                self.T[idx] = None                          # on mets la case à None

                return
            j += 1
            idx = (h1 + j * h2) % self.m

        raise KeyError(f"Clef inconnue {k}")

    def __setitem__(self, k, v):
        self.insert(k, v)

    def __getitem__(self, k):
        return self.search(k)

    def __delitem__(self, k):
        self.delete(k)

class DictChainingLinkedList:
    """
    Chainage Bidirectionelle, On a utilisé la classe Node et la classe Unordered list pour compléter cette classe
    """
    def __init__(self, m):
        self.T = [None] * m         # on initialise une table avec des None
        self.m = m                  # on récupère la taille maximale de stockage
        self.n = 0                  # on initialise la taille des clés
    def __len__(self):
        """
        Donne le nombre de clé
        :return:
        """
        return self.n
    def h(self, k):
        """
        Hachage unique
        :param k:
        :return:
        """
        h = 0x1505

        for i in k:
            h += 33 * h + ord(i)

        return h
    def insert(self, k, v):
        """
        Insère un élément
        :param k:
        :param v:
        :return:
        """
        h = self.h(k)                           # on effectue le hachage
        indice = h % self.m                     # on stock l'indice avec le hachage

        if self.T[indice] == None:              # si la case est vide
            self.T[indice] = UnorderedList()    # on vient créer une UnorderedList sur cette case

        elif self.T[indice][k] == None:         # si la clé est vide
            pass

        elif self.T[indice][k][0] == k:         # si la clé est déjà présente
            del self.T[indice][k]               # on enleve la clé
            self.n -= 1                         # on décrémente le nombre de clé

        self.T[indice].add((k, v))              # on vient ajouter sur cette UnorderedList une nouvelle valeur
        self.n += 1                             # on incrémente de nouveau le nombre de clé


    def search(self, k):
        """
        Permet de rechercher une clé
        :param k:
        :return:
        """
        h = self.h(k)
        indice = h % self.m                                 # on stock l'indice dans une variable
        if self.T[indice] is None:
            raise KeyError                                  # si la clé n'existe pas
        return self.T[indice][k][1]                         # renvoie la valeur recherché

    def delete(self, k):
        """
        Supprime un élément
        :param k:
        :return:
        """
        h = self.h(k)
        indice = h % self.m
        if self.T[indice] == None:                          # s'il n'y pas cette clé à la case demandée
            raise KeyError

        if self.T[indice][k] == None:
            raise KeyError
        del self.T[indice][k]                               # si on trouve l'element qu'on veut supprimer
        self.n -= 1

    def __setitem__(self, k, v):
        self.insert(k, v)

    def __getitem__(self, k):
        return self.search(k)

    def __delitem__(self, k):
        self.delete(k)


class UnorderedList :
    """
    Classe qui permet de mettre une valeur au début de la liste grâce à la classe Node
    """
    def __init__(self) :
        self.head = Node(None)              # tête de liste est un noeud avec None
        self.count= 0                       # permet de vérifier si la liste est vide ou pas
    def isEmpty(self) :
        """
        Bool qui dit si la liste est vide ou pas
        :return:
        """
        return self.count == 0
    def add(self,item):
        """
        Rajoute un noeud dans la liste
        :param item:
        :return:
        """
        temp = Node(item)                   # on transforme l'élément en un noeud
        temp.setNext(self.head.getNext())   # on mets la valeur suivante de ce noeud comme était la valeur suivante
                                            # de la tete de liste
        if self.isEmpty() == False:         # si la liste n'est pas vide
            temp.getNext().setPrevious(temp)

        self.head.setNext(temp)             # on mets l'élément qui vient d'etre ajoutée comme étant le suivant
                                            # de la tete de liste
        temp.setPrevious(self.head)         # et le précédent de l'élément qui vient d'être ajoutée sera la tête de
                                            # liste
        self.count += 1                     # on incrémente la taille parce qu'on vient de rajouter un élément

    def search(self, item):
        """
        Permet de rechercher un élément
        :param item:
        :return:
        """
        temp = self.head.getNext()          # on va prendre la valeur après la tete de liste
        if temp != None:                    # tant qu'on arrive pas à la fin
            while temp != None and temp.getData() != None and temp.getData()[0] != item:
                temp = temp.getNext()       # on continue à prendre la valeur suivante

            if temp == None or temp.getData() == None:
                return None                 # si on arrive à la fin

            return temp.getData()           # si on trouve l'élément on le renvoie
        return None

    def delete(self, item):
        """
        Permet de supprimer un élément
        :param item:
        :return:
        """
        flag = True                                         # booléen initialisé à Vrai
        temp = self.head.getNext()                          # on prend la valeur après la tete de liste

        if temp != None:                                    # si cet élément n'est pas None, si on arrive pas à la fin
            while temp.getData() is not None and temp.getData()[0] != item:
                temp = temp.getNext()                       # on continue à parcourir la liste
                flag = False                                # on a pas trouvé l'élément

            if temp.getData() is None:
                return None

            temp.getPrevious().setNext(temp.getNext())      # si on trouve l'élément on mets son précédent comme
                                                            # était le précédent de l'élément qui est devant lui

            if temp.getNext() is not None and flag:
                temp.getNext().setPrevious(temp.getPrevious())
            self.count -= 1

    def __len__(self):
        return self.count

    def __getitem__(self, item):
        return self.search(item)

    def __delitem__(self, key):
        self.delete(key)


class Node:
    """
    Classe Node vue au cours
    """
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrevious(self, newprevious):
        self.previous = newprevious

    def getPrevious(self):
        return self.previous

class Node_skip(object):
    """
    Classe Node qui va être utilisée pour SkipList
    """
    def __init__(self, value, next, width):
        self.value,self.next,self.width = value,next,width

    @property
    def get_value(self):
        return self.value

    def set_value(self,new_value):
        self.value = new_value



class End(object):
    def __le__(self, other):
        return False
    def __lt__(self, other):
        return False
    def __ge__(self, other):
        return True
    def __gt__(self, other):
        return True

NIL = Node_skip(End() , [], [])


class Skiplist :
    """
    Classe vue au cours mise à part l'ajout pour tester si c'est un élément de End ou pas tout est comme dans le cours
    """
    def __init__(self , expected_size=100):
        self.size = 0
        self.maxlevels = int(1 + log(expected_size , 2))
        self.head = Node_skip( 'HEAD' , [NIL]*self.maxlevels, [1]*self.maxlevels)

    def find(self, value):
        node = self.head
        for level in reversed(range(self.maxlevels)):
            if isinstance(node.next[level].value,End):      # on ne va pas toujours tomber sur un objet de la classe End
                                                            # à chaque modification on aura une clé et une valeur
                while node.next[level].value < value:
                    node = node.next[level]

            else:                                           # si l'objet n'est pas de End
                while node.next[level].value[0] < value:    # on compare la clé
                    node = node.next[level]
                    if isinstance(node.next[level].value,End): # si à un moment on arrive sur un node qui fait partie de End
                                                            # on est arrivé à None donc on peut s'arrêter
                        break
        node = node.next[0]                                 # on stock la valeur du node suivant qui n'est forcément
                                                            # pas de type End
        if isinstance(node.value,End):                      # on vérifie si cet élément fait partie de la classe End
            return None
        else:
            if node.value[0] == value:                      # si elle correspond à la valeur recherchée
                return node
        return None

    def insert(self, value):
        """
        Permet d'insérer un élément
        :param value:
        :return:
        """
        chain = [None]*self.maxlevels
        steps_at_level = [0]*self.maxlevels
        node = self.head

        for level in reversed(range(self.maxlevels)):

            while node.next[level].value <= value:
                steps_at_level[level] += node.width[level]
                node = node.next[level]
            chain[level] = node

        d = 1
        while d < self.maxlevels and random() < 0.5:
            d += 1
        newnode = Node_skip(value, [None]*d, [None]*d)
        steps = 0

        for level in range(d):
            prevnode = chain[level]
            newnode.next[level] = prevnode.next[level]
            prevnode.next[level] = newnode
            newnode.width[level] = prevnode.width[level] - steps
            prevnode.width[level] = steps + 1
            steps += steps_at_level[level]


        for level in range(d, self.maxlevels):
            chain[level].width[level] += 1

        self.size += 1

    def remove(self, value):
        chain = [None]*self.maxlevels

        node = self.head
        for level in reversed(range(self.maxlevels)):
            if isinstance(node.next[level].value,End):
                while node.next[level].value < value:

                    node = node.next[level]

            else:
                while node.next[level].value[0] < value:

                    node = node.next[level]
                    if isinstance(node.next[level].value,End): # si à un moment on arrive sur un node qui fait
                                                                # partie de End
                                                                # on est arrivé à None donc on peut s'arrêter
                        break

            chain[level] = node

        if isinstance(node.next[level].value,End):
            if value != chain[0].next[0].value:
                return False

        else:
            if value != chain[0].next[0].value[0]:
                return False

        d = len(chain[0].next[0].next)
        for level in range(d):
            prevnode = chain[level]
            prevnode.width[level] += prevnode.next[level].width[level] -1
            prevnode.next[level] = prevnode.next[level].next[level]

        for level in range(d,self.maxlevels):
            chain[level].width[level] -=1

        self.size-=1
        return True

    def __getitem__(self, i):
        node = self.head
        i += 1
        for level in reversed(range(self.maxlevels)):
            while node.width[level] <= i:
                i -= node.width[level]
                node = node.next[level]
        return node.value

class DictChainingSkipList:
    def __init__(self, m):
        self.T = [None] * m
        self.m = m
        self.n = 0
    def __len__(self):
        return self.n
    def h(self, k):
        h = 0x1505

        for i in k:
            h += 33 * h + ord(i)

        return h
    def insert(self, k, v):
        h = self.h(k)
        indice = h % self.m

        if self.T[indice] == None:      # si la case ne contient rien
            self.T[indice] = Skiplist() # on va créer une skiplist sur cette case
            self.T[indice].insert((k,v))
            self.n += 1

        else:
            elem = self.T[indice].find(k)
            if elem:
                elem.value = (k,v)

            else:
                self.T[indice].insert((k,v))
                self.n += 1

    def search(self, k):
        h = self.h(k)
        indice = h % self.m

        if self.T[indice]:                      # si l'élément est trouvé
            elem = self.T[indice].find(k)
            if elem:
                return elem.get_value[1]

        raise KeyError
    def delete(self, k):
        h = self.h(k)
        indice = h % self.m
        if self.T[indice]:
            self.T[indice].remove(k)
            self.n -= 1

        else:
            raise KeyError
    def __setitem__(self, k, v):
        self.insert(k,v)
    def __getitem__(self, k):
        return self.search(k)

    def __delitem__(self, k):
        self.delete(k)

class ResizableDictOpenAddressing:
    """
    Classe qui permet de redefinir la taille à chaque fois
    """
    def __init__(self, m):
        self.m = m
        self.n = 0
        self.key = [None]*self.m            # on stock les clés dans une liste
        self.value = [None]*self.m          # on stock les valeurs dans une liste
        self.indices_used = []              # on stock les indices utilisées dans une liste

    def resize(self):
        """
        Fonction gère la taille
        :return:
        """
        replace = []
        for indices in self.indices_used:
            replace.append((self.key[indices], self.value[indices]))    # on ajoute dans une liste la clé et la valeur
            self.key[indices], self.value[indices] = None, None         # on les mets à None
        self.key += [None for i in range(self.m)]
        self.value += [None for i in range(self.m)]
        self.m *= 2                                                     # on augmente la taille de 2 fois
        for k, v in replace:
            self.insert(k, v)                                           # on rajoute les éléments

    @property
    def load_factor(self):
        """
        Calcul pour trouver la surchage de la table
        :return:
        """
        return self.n / self.m

    def h1(self, k):
        """
        Hachage 1
        :param k:
        :return:
        """
        h = 0
        for i in k:
            h += ord(i)

        return h

    def h2(self, k):
        """
        Hachage 2
        :param k:
        :return:
        """
        h = 0x1505

        for i in k:
            h += 33 * h + ord(i)

        return h

    def h(self, k, j):
        """
        Fonction qui donne le double hashage
        :param k:
        :param j:
        :return:
        """
        h1 = self.h1(k)
        h2 = self.h2(k)
        h = (h1 + j * h2) % self.m
        return h

    def insert(self, k, v):
        """
        Insère
        :param k:
        :param v:
        :return:
        """
        indice, flag = self.search_indice(k)
        if flag is True:
            self.value[indice] = v
        elif flag is None:
            self.n += 1
            self.key[indice] = k
            self.value[indice] = v
            self.indices_used.append(indice)
        else:
            self.resize()
            self.insert(k, v)

    def search(self, k):
        """
        Fonction qui recherche une clé
        :param k:
        :return:
        """
        indice, flag = self.search_indice(k)
        if flag == True:
            return self.value[indice]
        else:
            raise KeyError

    def search_indice(self, k):
        """
        Fonction qui recherche un indice et complètement le search afin d'aller plus vite en récupérant uniquement
        ce dont l'on a besoin
        :param k:
        :return:
        """
        i = 0
        hash = self.h(k, i)
        hash_ = hash
        while True:
            if self.key[hash]:
                keep = hash
            if self.key[hash] == k:
                self.key[keep], self.key[hash] = self.key[hash], self.key[keep]
                self.value[keep], self.value[hash] = self.value[hash], self.value[keep]
                return hash, True

            else:
                i += 1
                hash = self.h(k, i)

            if self.key[hash] == None:
                return hash, None

            if hash_ == hash:
                return hash, False

    def delete(self, k):
        """
        Fonction qui supprime une clé
        :param k:
        :return:
        """
        indice, flag = self.search_indice(k)
        if flag:
            self.n -= 1
            self.key[indice] = True
            self.value[indice] = True
            self.indices_used.remove(indice)
        else:
            raise KeyError

    def __len__(self):
        return self.n

    def __setitem__(self, k, v):
        self.insert(k, v)

    def __getitem__(self, k):
        return self.search(k)

    def __delitem__(self, k):
        self.delete(k)
