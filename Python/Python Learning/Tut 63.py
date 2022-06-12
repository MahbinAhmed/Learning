class Grand_father :
    cricket = 1

class Father(Grand_father) :
    football = 1
    cricket =  3
    badminton = 5
    
class Son (Father):
    badminton = 1

Harry = Son()
print(Harry.football)
print(Harry.cricket)
print(Harry.badminton)