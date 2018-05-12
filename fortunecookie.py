## Fortune Cookie Generator
## Johnny and Robert May
## April 24, 2018

from random import*
import os

class Cookie:
    def __init__(self, nouns, verbs, adjectives, adverbs, names):
        self.nouns=nouns
        self.verbs=verbs
        self.adjectives=adjectives
        self.adverbs=adverbs
        self.names=names
        self.message=""
        self.score=0
    def generatemessage(self):
        b=randint(1,7)
        if b==1:
            self.message="You will get %s by a %s %s" %(self.pasttense(choice(self.verbs)[:-1]),
                                                        choice(self.adjectives)[:-1],
                                                        choice(self.nouns)[:-1])
        elif b==2:
            self.message="You will %s at the hands of a %s %s" %(choice(self.verbs)[:-1],
                                                                 choice(self.adjectives)[:-1],
                                                                 choice(self.nouns)[:-1])
        elif b==3:
            self.message="%s, you %s" %(choice(self.verbs)[:-1],
                                        choice(self.nouns)[:-1])
        elif b==4:
            self.message="%s will %s %s all over your %s" %(choice(self.names)[:-1],
                                                            choice(self.verbs)[:-1],
                                                            choice(self.adverbs)[:-1],
                                                            choice(self.nouns)[:-1])
        elif b==5:
            self.message="You %s the %s, didn't you" %(self.pasttense(choice(self.verbs)[:-1]),
                                                       choice(self.nouns)[:-1])

        elif b==6:
            self.message="You will %s the %s of a %s %s" %(choice(self.verbs)[:-1],
                                                           choice(self.nouns)[:-1],
                                                                 choice(self.adjectives)[:-1],
                                                                 choice(self.nouns)[:-1])
        elif b==7:
            self.message="YOU F0000L. YOU?=!DIDNOT.HIT(THE)QUAN////CORRECTLY.get fricking DUNKED on"

    def opencookie(self):
        self.generatemessage()
        print self.message

    def pasttense(self, verb):
        vowels=["a", "e", "i", "o", "u"]
        if verb[-2:]=="ng":
            verb=list(verb)
            verb[-3]="u"
            verb="".join(verb)
            return verb
        elif verb[-3] not in vowels:
            #print "verb -3 not in vowels"
            if verb[-1]=="e":
                return verb+"d"
            elif verb[-1]=="t":
                consonants=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
                if verb[-2] not in consonants:
                    return verb+"ted"
                else:
                    return verb+"ed"
            elif verb[-1]=="n":
                return verb+"ned"
            elif verb[-1]=="d":
                return verb+"ded"
            elif verb[-1]=="b":
                return verb+"bed"
            elif verb[-1]=="p":
                return verb+"ped"
            elif verb[-1]=="y":
                if verb[-2] not in vowels:
                    return verb[0:-1]+"ied"
            elif verb[-2] in vowels:
                if verb[-1]=="n":
                    return verb+"ned"
                elif verb[-1]=="m":
                    return verb+"med"
                elif verb[-1]=="s":
                    return verb+"sed"
            else:
                return verb+"ed"
        elif verb[-1]=="y":
            if verb[-2] not in vowels:
                return verb[0:-1]+"ied"
        elif verb[-1]=="e":
            return verb+"d"
        else:
            return verb+"ed"


def opencookie(nouns, verbs, adjectives, adverbs, names):
    cookie=Cookie(nouns, verbs, adjectives, adverbs, names)
    cookie.opencookie()


def main():
    #cookie=Cookie(0,0,0,0,0)
    #print cookie.pasttense("")
    print "Welcome to Fortune Cookie Generator"
    q = "n"
    while q == "n":
        menu()
        q = raw_input("Doth the omen prompt your departure? [y/n]: ").lower()[0]

def menu():
    nouns=open("./dictionary/nouns.txt","r")
    tempnounslist=nouns.readlines()
    nounslist=[]
    for i in tempnounslist:
        if i[-4:-1]!="ing":
            nounslist.append(i)
    nouns.close()
    adjectives=open("./dictionary/adjectives.txt","r")
    adjectiveslist=adjectives.readlines()
    adjectives.close()
    adverbs=open("./dictionary/adverbs.txt","r")
    adverbslist=adverbs.readlines()
    adverbs.close()
    verbs=open("./dictionary/verbs.txt","r")
    verbslist=verbs.readlines()
    verbs.close()
    names=open("./dictionary/names.txt","r")
    nameslist=names.readlines()
    names.close()
    fortbank=open("./fortbank.txt","r")
    fortunes=fortbank.readlines()
    fortbank.close()
    choice=0
    while choice!="3":
        print """
    1 - Open a fortune cookie
    2 - Peruse the fortune bank
    3 - Rid yourself of this purgatory
    """
        choice=raw_input("How dost thou wish to proceed? ")
        if choice=="1":
            opencookie(nounslist, verbslist, adjectiveslist, adverbslist, nameslist)
        elif choice=="2":
            choice2=0
            while choice2!="4":
                print """
        1 - Add an original fortune to the fortune bank
        2 - Send a fortune to the ward
        3 - Peer at the fortunes as they work
        4 - Retreat
        """
                choice2=raw_input("Which action takest thou next? ")
                if choice2=="1":
                    create()
                elif choice2=="2":
                    delete(fortunes)
                elif choice2=="3":
                    seeall(fortunes)

def create():
    print
    yn="y"
    while yn=="y":
        fortbank=open("./fortbank.txt","a")
        newfortune=raw_input("Birth a fortune of the womb of your mind ")
        fortbank.write(newfortune + "\n")
        fortbank.close()
        print
        yn=raw_input("Would you like to cultivate more legumes to the garden of fortunes? If no, you will be sent back to the menu. y/n ")
        yn=yn.lower()
        yn=yn[0]

def delete(fortunes):
    print
    yn="y"
    if len(fortunes) < 1:
        yn = "n"
        print "You monster, you've sent them all to the ward. A hex upon you."
    while yn=="y":
        seeall(fortunes)
        indexchoice=verifyindex(len(fortunes))
        fortunes.pop(indexchoice-1)
        print
        yn=raw_input("Would you like to eradicate the fortune bank of another disease? Otherwise, you will be delivered into the care of the menu. y/n ")
        yn=yn.lower()
        yn=yn[0]
        if len(fortunes) < 1:
            yn = "n"
            print "You monster, you've sent them all to the ward. A hex upon you."
    fortbank=""
    print
    f=open("./fortbank.txt", "w")
    if len(fortunes) < 1:
        f.write(fortbank)
    else:
        for fort in fortunes[0:-1]:
            fortbank += fort + "\n"
        fortbank += fortunes[-1]
        f.write(fortbank)
    f.close()

def seeall(fortunes):
    index=0
    for i in fortunes:
        index+=1
        print str(index)+" -",i


def verifyindex(index):
    f=False
    while f==False:
        indexchoice=raw_input("Which naughty boy would you like to punish?" )
        if indexchoice.isdigit() and int(indexchoice)<=index:
            f=True
        else:
            print "Scum"
    return int(indexchoice)


#        fortbank.close()

main()
