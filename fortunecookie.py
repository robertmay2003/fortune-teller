## Fortune Cookie Generator
## Johnny and Robert May
## April 24, 2018

from random import*
import os
import sys
from time import sleep
sys.path.insert(0, '%s/modules'%(os.path.dirname(os.path.abspath(__file__))))

from minigames import *

class Cookie:
    def __init__(self, nouns, verbs, adjectives, adverbs, names, fortbank):
        self.nouns=nouns
        self.verbs=verbs
        self.adjectives=adjectives
        self.adverbs=adverbs
        self.names=names
        self.message=""
        self.score=0
        self.fortbank = fortbank
    def generatemessage(self):
        p=randint(1,5)
        if p==5 and len(self.fortbank) > 0:
        # if True:
            fort=self.fortbank[randint(0,len(self.fortbank)-1)]
            self.message = fort[0:-1]
        else:
            b=randint(1,10)
            if b==1:
                self.message="You will get %s by a %s %s" %(self.pasttense(choice(self.verbs).strip('\n')),
                                                            choice(self.adjectives).strip('\n'),
                                                            choice(self.nouns).strip('\n'))
            elif b==2:
                self.message="You will %s at the hands of a %s %s" %(choice(self.verbs).strip('\n'),
                                                                     choice(self.adjectives).strip('\n'),
                                                                     choice(self.nouns).strip('\n'))
            elif b==3:
                self.message="%s, you %s" %(choice(self.verbs).strip('\n'),
                                            choice(self.nouns).strip('\n'))
            elif b==4:
                self.message="%s will %s %s all over your %s" %(choice(self.names).strip('\n'),
                                                                choice(self.verbs).strip('\n'),
                                                                choice(self.adverbs).strip('\n'),
                                                                choice(self.nouns).strip('\n'))
            elif b==5:
                self.message="You %s the %s, didn't you" %(self.pasttense(choice(self.verbs).strip('\n')),
                                                           choice(self.nouns).strip('\n'))

            elif b==6:
                self.message="You will %s the %s of a %s %s" %(choice(self.verbs).strip('\n'),
                                                               choice(self.nouns).strip('\n'),
                                                                     choice(self.adjectives).strip('\n'),
                                                                     choice(self.nouns).strip('\n'))
            elif b==7:
                self.message="Your %s is about to %s you - be ready" %(choice(self.nouns).strip('\n'),
                                                                       choice(self.verbs).strip('\n'))
            elif b==8:
                self.message="You will get %s by the %s" %(self.pasttense(choice(self.verbs).strip('\n')),
                                                           choice(self.nouns).strip('\n'))
            elif b==9:
                self.message="You will be %s %s by a %s %s named %s" %(choice(self.adverbs).strip('\n'),
                                                                       self.pasttense(choice(self.verbs).strip('\n')),
                                                                       choice(self.adjectives).strip('\n'),
                                                                       choice(self.nouns).strip('\n'),
                                                                       choice(self.names).strip('\n'))

            elif b==10:
                self.message="%s is going to come out of your %s" %(choice(self.nouns).strip('\n'),
                                                                    choice(self.nouns).strip('\n'))

    def opencookie(self):
        self.generatemessage()
        self.score = self.scoreMessage(True)
        print self.message
        if self.score <= 0:
            print "You are to man as manure is to fresh soil;\nGarbage that will die away to fertilize it's superiors."
        else:
            print "You have IQ", self.score

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

    def scoreMessage(self, pr):
        scoredict={"a":1,"e":1,"i":1,"o":1,"u":1,"l":1,"n":1,"s":1,"t":1,"r":1,
                   "d":2,"g":2,
                   "b":3,"c":3,"m":3,"p":3,
                   "f":4,"h":4,"v":4,"w":4,"y":4,
                   "k":5,
                   "j":8,"x":8,
                   "q":10,"z":10}
        totalscore=0
        messages=self.message.split()
        letters=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z", "a","e","i","u","o","y"]
        #print self.message,self.fortbank
        if self.message+'\n' not in self.fortbank:
            for message in messages:
                score = 0
                for i in message.lower():
                    if i in letters:
                        score+=scoredict[i]
                score *= len(message)
                totalscore += score
            if "Nigel" in messages and "Hamilton" in messages:
                totalscore += 50
                if pr:
                    print choice(["You have inherited the IQ of Nigel Hamilton; plus 50 IQ points", "yo nigel got a 3 on the AP lmao take 50 extra IQ", "what is this speak of nigel hamilton? I will pay you 50 extra IQ to get this curd of a man away from my computer"])
            if "rqxtux" in messages:
                totalscore += 20000
                if pr:
                    print choice(["haha rqxtux yes indeed","mmmm rqxtux","aha, rqxtux arrives"])
            totalscore *= len(self.message)
            totalscore -= 5*ord(self.message[-2])
        else:
            #print("oof ow, naenae'd by nama jeff")
            for message in messages:
                score=0
                for i in message.lower():
                    if i in letters:
                        score+=scoredict[i]
                totalscore += score
            totalscore *= 15
            totalscore /= len(messages)
        if totalscore < 100 and pr:
            print("oof, naenae'd by nama jeff")

        return totalscore

class Customer:
    def __init__(self, adjectives, verbs, names):
        self.desc = "A %s, %s fella %ss in."%(choice(adjectives),
                                              choice(adjectives),
                                              choice(verbs))
        self.name = choice(names).strip("\n")
        personalities = ["proper", "mean", "happy", "cool", "shady"]
        self.attitude = [choice(personalities), choice(personalities)]
        self.style = choice(["palm","crystal-ball","cards","constellations"])
    def introduce(self):
        dialogue = ""
        introDict = {"mean": ["Gimme a","I want a","My whore wife wants a"],
                     "proper": ["I require a'm'st","If it be not a burden, I would like a","Unto thee I request a"],
                     "cool": ["Can i get uhhhhh", "Yo, how about you gives me a", "I sure am cravin' a good ol"],
                     "happy": ["What a great day for a","What's crackin, doc-o? How about a","Haha yes. Haha. A"],
                     "shady": ["Listen, I got 20 seconds before I'm found. Can you get me a","I have $20. Do you have a","mmmmm. mmmmmm mmmm."]}
        middleDict = {"palm":"palm reading",
                      "crystal-ball":"crystal ball reading",
                      "cards":"tarot card reading",
                      "constellations":"zodiac sign reading"}
        endDict = {"mean": [", and make it snappy","you fat dickbag","for my whore wife"],
                   "proper": ["if the fates allow","if you may","please and thank you"],
                   "cool": ["capeesh?","mate","my guy"],
                   "happy": [". Yes haha.", "and no drugs", "and a dad who loves me", "doco"],
                   "shady": ["... You do understand the situation, right?", "for free", "... I'll give you a child for payment"]}
        dialogue = choice(introDict[choice(self.attitude)]) + " \033[1;32m" + middleDict[self.style] + "\033[0m\033[1;34m " + choice(endDict[choice(self.attitude)])
        print "%s: \033[1;34m"%(self.name) + dialogue + "\033[0m"
    def angryMessage(self):
        dialogue = ""
        startDict = {"mean":["Dammit,","Come on,","You ruined it,"],
                     "proper":["Goodness me,","By golly,","Good heavens"],
                     "cool":["What the fortnite,","Heckin Herobrine,","Despacheeto,"],
                     "happy":["I can't forgive that,","You ruined my day,","You sound like my dad,"],
                     "shady":["They'll find me now,","My cover's been blown,"]}
        endDict = {"mean":["trashwad!", "dirtbag!", "bastard!", "waldo!"],
                   "proper":["ruffian!", "good fellow!"],
                   "cool":["John Wick!","Jefferoony!","Baka!","n00b!"],
                   "happy":["dad!","government-man!","douche!"],
                   "shady":["agent!","copper pig!","bullyhunters!"]}
        dialogue = choice(startDict[choice(self.attitude)]) + " " + choice(endDict[choice(self.attitude)])
        print "%s: \033[0;31m%s\033[0m"%(self.name, dialogue)

class GameSession:
    def __init__(self, nouns, verbs, adjectives, adverbs, names, fortbank):
        self.totalscore = 0
        self.difficulty = 1.0
        self.failedCustomers = 0
        self.totalCustomers = 0
        self.nouns=nouns
        self.verbs=verbs
        self.adjectives=adjectives
        self.adverbs=adverbs
        self.names=names
        self.fortbank = fortbank
    def ask(self, customer):
        game = randomGame.Game(self.difficulty, True)
        customer = Customer(self.adjectives, self.verbs, self.names)
        customer.introduce()
        raw_input("[ENTER] to continue")
        score = game.ask(customer.style)
        maxScore = game.getMaxScore()
        cookiescore = self.chooseCookie(score, maxScore)
        print "Your score: %s / %s"%(score, maxScore)
        if score <= maxScore / 2:
            self.failedCustomers += 1
            customer.angryMessage()
        self.totalscore += cookiescore
        self.totalCustomers += 1
        self.difficulty += 0.2
        if self.difficulty > 10.0:
            self.difficulty = 10.0
        print "Failed Customers: " + "x"*self.failedCustomers
        raw_input("[ENTER] to continue")

    def chooseCookie(self, ind, length):
        cookieArr = []
        for i in range(0, length + 1):
            cookieArr.append(Cookie(self.nouns, self.verbs, self.adjectives, self.adverbs, self.names, self.fortbank))
            cookieArr[i].generatemessage()
            cookieArr[i].score = cookieArr[i].scoreMessage(False)
        cookieArr = self.cookieSort(cookieArr)
        cookie = cookieArr[ind]
        print "YOU: \"\033[0;31m"+cookie.message+"\033[0m\""
        return cookie.score
    def cookieSort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i].score
            j = i-1
            while j >=0 and key < arr[j].score :
                    arr[j+1] = arr[j]
                    j -= 1
            arr[j+1].score = key
        return arr
    def conclude(self):
        print "\033[0;31mGAME OVER\033[0m"
        print "Your score: %s"%(self.totalscore)
        leaderboard, leadernames=readgamesboard()
        leaderboard.append(self.totalscore)
        leaderboard.sort()
        leaderboard.reverse()
        if leaderboard.index(self.totalscore)<10:
            print "You won the boogie down challenge!"
            name=raw_input("Whomsteth? ")
            if name == "Nigel Hamilton":
                print "f-word you"
                name = "horsef-worder"
            leadername=name + " -- " + str(self.totalCustomers) + " customers"
            leadernames.insert(leaderboard.index(self.totalscore), leadername)
        leaderboard = leaderboard[0:10]
        leadernames = leadernames[0:10]
        f=open("gamesleaderboard.txt","w")
        fullLB = ""
        for i in leaderboard:
            fullLB += (str(i) + "\n")
        f.write(fullLB)
        f.close()
        g=open("gamesleadernames.txt","w")
        fullLN = ""
        for i in leadernames:
            fullLN += (i + "\n")
        g.write(fullLN)
        g.close()
    def play(self):
        while self.failedCustomers < 5:
            self.ask(Customer(self.adjectives,self.verbs,self.names))
        self.conclude()


def opencookie(nouns, verbs, adjectives, adverbs, names, fortunes):
    cookie=Cookie(nouns, verbs, adjectives, adverbs, names, fortunes)
    cookie.opencookie()
    youhavemail = os.spawnlp(os.P_NOWAIT, "/usr/bin/afplay", "afplay", "levelup.mp3")
    leaderboard, leadernames=readleaderboard()
    leaderboard.append(cookie.score)
    leaderboard.sort()
    leaderboard.reverse()
    if leaderboard.index(cookie.score)<10:
        print "Victory Royale! You have IQ John Wick skin disease"
        name=raw_input("Whomsteth? ")
        if name == "Nigel Hamilton":
            print "f-word you"
            name = "horsef-worder"
        leadername=name + " -- " + cookie.message
        leadernames.insert(leaderboard.index(cookie.score), leadername)
    leaderboard = leaderboard[0:10]
    leadernames = leadernames[0:10]
    f=open("leaderboard.txt","w")
    fullLB = ""
    for i in leaderboard:
        fullLB += (str(i) + "\n")
    f.write(fullLB)
    f.close()
    g=open("leadernames.txt","w")
    fullLN = ""
    for i in leadernames:
        fullLN += (i + "\n")
    g.write(fullLN)
    g.close()

def readleaderboard():
    f=open("leaderboard.txt","r")
    leaderboard=f.readlines()
    f.close()
    g=open("leadernames.txt","r")
    leadernames=g.readlines()
    g.close()
    print
    newLeaderboard = []
    for i in leaderboard:
        newLeaderboard.append(int(i))
    newNameboard = []
    for i in leadernames:
        newNameboard.append(i.strip('\n'))
    return newLeaderboard, newNameboard

def readgamesboard():
    f=open("gamesleaderboard.txt","r")
    leaderboard=f.readlines()
    f.close()
    g=open("gamesleadernames.txt","r")
    leadernames=g.readlines()
    g.close()
    print
    newLeaderboard = []
    for i in leaderboard:
        newLeaderboard.append(int(i))
    newNameboard = []
    for i in leadernames:
        newNameboard.append(i.strip('\n'))
    return newLeaderboard, newNameboard


def main():
    #cookie=Cookie(0,0,0,0,0)
    #print cookie.pasttense("")
    menuTheme = os.spawnlp(os.P_NOWAIT, "./audioPlayer.sh", "fortuneCookieTheme", choice(["p.mp3", "fardnite.mp3"]))
    print "Welcome to Fortune Cookie Generator"
    q = "n"
    while q == "n":
        menu()
        q = raw_input("Doth the omen prompt your departure? [y/n]: ").lower()[0]
        # We should write everything within the program to the list versions, and then, HERE, replace each file with the contents of the new list.
        # f=open("fortbank.txt", "w")
        # for i in fortunes:
        #   i=i+/n
        #   f.write(i)
    print "Good riddance, scum"
    os.system("kill %s;kill \"$(cat /tmp/cu-song.pid)\""%(menuTheme))

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
    choice="0"
    while choice!="5":
        fortbank=open("./fortbank.txt","r")
        fortunes=fortbank.readlines()
        fortbank.close()
        print """
    1 - Open a fortune cookie
    2 - Peruse the fortune bank
    3 - Marvel at the intellectual superiority
    4 - View the grand contest
    5 - Rid yourself of this purgatory
    """
        choice=raw_input("How dost thou wish to proceed? ")
        if choice=="1":
            opencookie(nounslist, verbslist, adjectiveslist, adverbslist, nameslist, fortunes)
        elif choice=="2":
            choice2="0"
            while choice2 !="4":
                fortbank=open("./fortbank.txt","r")
                fortunes=fortbank.readlines()
                fortbank.close()
                print """
        1 - Add an original fortune to the fortune bank
        2 - Send a fortune to the ward
        3 - Peer at the fortunes as they work
        4 - Retreat
        """
                choice2=raw_input("Which action takest thou next? ")
                if choice2=="1":
                    create(fortunes)
                elif choice2=="2":
                    delete(fortunes)
                elif choice2=="3":
                    seeall(fortunes)
        elif choice=="3":
            leaderboard()
        elif choice == "4":
            choice2="0"
            while choice2 != "3":
                print """
        1 - Dabble in the games of God
        2 - View the victors
        3 - Exeunt
                """
                choice2=raw_input("Whomst option shalt thou pickerooni? ")
                if choice2 == "1":
                    game = GameSession(nounslist, verbslist, adjectiveslist, adverbslist, nameslist, fortunes)
                    game.play()
                elif choice2 == "2":
                    gamesboard()

def create(fortunes):
    print
    yn="y"
    while yn=="y":
        #newfortune=raw_input("Birth a fortune of the womb of your mind")
        #fortunes.append(newfortune)
        #return fortunes
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
    f=open("./fortbank.txt", "w")
    f.close()
    f=open("./fortbank.txt", "a")
    yn="y"
    if len(fortunes) < 1:
        yn = "n"
        print
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
    for fort in fortunes:
        f.write(fort)
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

def leaderboard():
    leadernums, leadernames = readleaderboard()
    index = 0
    for i in leadernums:
        print index+1, "-", leadernames[index].strip('\n') + ": " + str(i)
        index += 1

def gamesboard():
    leadernums, leadernames = readgamesboard()
    index = 0
    for i in leadernums:
        print index+1, "-", leadernames[index].strip('\n') + ": " + str(i)
        index += 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'KeyboardInterrupted'
        os.system("killall fortuneCookieTheme")
        os.system("killall afplay")
