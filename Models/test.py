def SontInvOuOpp(a, b) :
    if a+b==0 or a*b==1 :
        return True
    else :
        return False


def existeInvOuOppConsecutifs(T) :
    v = False
    while not v :
        for i in range(len(T) - 1) :
            a = T[i] + T[i+1]
            b = T[i] * T[i+1]
            if  a==0 or b==1 :
                v = True
        break
    return v


def existeInvOuOpp(T) :
    for i in range(len(T) - 1) :
        for j in range(i+1, len(T)) :
            if SontInvOuOpp(T[i], T[j]) :
                return True
    return False


def remplireAtome(N) :
    with open("Atomes.txt","w") as file:
        for i in range(N) :
            atome = input("saisir atome :")
            masse = input("saisir masse :")
            ligne = atome + "*" + masse + "\n"
            file.write(ligne)



def premier(n) :
    if n > 1 :
        for i in range(2, int(n/2) + 1) :
            if n%i == 0 :
                return False
            else :
                return True


def fact(n) :
    fact = 1
    for i in range(1, n+1) :            
        fact = fact * i
    return fact



def premier_fact(n) :
   pass





from json2excel import Json2Excel



if __name__ == '__main__':
    json2excel = Json2Excel(head_name_cols=["rank", "name"])
    # print(json2excel.run('./test.json'))

    jsons = [
        {
            "student_no": 1001,
            "name": "James",
            "score": 10,
            "class": "A-1",
            "rank": 1
        },
        {
            "student_no": 1002,
            "name": "Tome",
            "score": 91,
            "class": "A-1",
            "rank": 2
        },
    ]
    print(json2excel.run(jsons))