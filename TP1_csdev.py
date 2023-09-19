#exo2 tp cs dev
#salager benoit
#19/09/2023
from math import *
def isbissex(annee):     
    #teste des conditions pour savoir si l'année est bissextile
    if annee%4 == 0 and annee%100 != 0 or annee%400 == 0:
        return True         #return true si oui
    else :
        return False        #sinon non


def jmois(num_mois,annee):
    liste30=[4,6,9,11]
    #num_mois=0
    #while num_mois not in range(1,12) : #on verifie que on a bien un nombre entre 1 et 12
        #int(input("numéro du mois :"))
    if num_mois in liste30 : #on cherche le mois dans la liste des mois a 30j
        return 30
    elif num_mois != 2: #est-ce que le mois est fevrier
        if isbissex(annee)==True:
            return 29
        else:
            return 28
    else :
        return 31

def isvalid(date):
    date =str(input("donner date sous format jj/mm/aaaa exemple 25/5/2005:")) #on demande une date a l'utilisateur
    jj , mm , aaaa =[int(s) for s in date.split("/")] #on recupere les jours, mois et années
    if mm in range(1,12): #le mois existe?
        if jj in range(jmois(mm,aaaa)): #le jour est bien dans le mois?
            return True
    else:
        return False
    

#exo3

def mesImpots():
    revenu=float(input("revenu :"))
    #taux:[0,11,30,41,45]
    #montant:[10225,26070,74 545,160336]
    #taxe={ 10225:0 , 26070:11 , 74545:30 , 160336:41 }
    if revenu<=10225:
        return 0
    elif revenu <= 26070:
        return ceil((revenu-10225)*0.11)
    elif revenu <= 74545:
        return 1744+ceil((revenu-26070)*0.30)
    elif revenu <= 160336:
        return 16287+ceil((revenu-75454)*0.41)
    elif revenu>=160336:
        return 51462+ceil((revenu-160336)*0.41)

#exo4
def oskour(m):
    D=[]
    D.append(m[3:])
    print(D)
    if len(m)==0:
        return D
    else :
        return oskour(m[3:])
def multiplication(A,B):
        C=[]
        M=[]
        for i in range(3):
            for v in range(3):
                for j in range(3):
                    for f in range(3):
                        C.append(A[i][v]*B[f][j])
        M=oskour(C)     


#exo5

def Hanoi(n):
    if n>1:
        print("deplace",n,"de plot 1 vers plot 2")
        print("deplace",n-1,"de plot 1 vers plot 3")
        print("deplace",n,"de plot 2 vers plot 3") 
        Hanoi(n-1)
               
