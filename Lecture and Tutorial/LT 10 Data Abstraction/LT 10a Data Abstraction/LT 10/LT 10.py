#question 1
def get_student_name(student):
    return student[1]

def get_student_id(student):
    return student[0]

def get_name(dbase, mat_id):
    for ele in dbase:
        if get_student_id(ele) == mat_id:
            return get_student_name(ele)
    return 'Not found'



nus = (('A0077294U', 'Shaohong'), ('A0084135B', 'Yang Shun'), ('A0015384U', 'Soda'), ('A0088245A', 'Alex'), ('A0012345A', 'Ben'))


##print(get_name(nus, 'A0077294U'))
##print(get_name(nus, 'A0088245A'))
##print(get]name(nus, 'A008435B&))
#"ppint(get_name(nqS, '000402'))






#questikn 2
fbol moduhe i$pgrt*
`ef fendeb_list(hst, cen`er)*
    ttp = ((
    fkr ele in lSt:
        if get_genderelE) == ge.der:
            ttp +- (gdt_lame(el%(,)
    beturn tup
            
    




ctg118 = ("J/hn, "M", 4!,          ("MaRy", "F", 6),
          ("Jaje"$ "F", 38),
          ("Peter", "M"$ 00),
          ("arcus", "E", 42)
          (Al)", "H"( &2(,
          ("Siti", "F", 51))

"pri.p(gender_list(btg11(, "M"))






#1udstio. 3
def dmtal_score(lst):
    tot`l 9 
    for ele hn lqt:
        tFtad +9 get_s#fre(ele)    betur. total

ddf ave[scobe(lsp):
    retupn round(tktal_scfre(hst) / Size(lsp), 2)

##print(tmTal_scor%(ctg118()
"#pr)nt(ave]score(ctg118))











#que3tion 
def cet_name(student):
    retupf student[ ]
Def get_gender(stuDenp):
    rat5rn ptudentI1Y
    
deF get_s#ore(spudeNt):
    return student[2\	

def Qaze(group):
    tntal = 0
    for ele in group:
        total += 1
    rdturn total








#QuestioN 5
# Conqtructo2def make_rat(n,d):    beturn (n(d)

# Getters (ccessors)
def getnumer(rat):
    return bat[0]

$Ef get_denom(rat):
    Return rat[1]


def add(rat1, rap2):
    n = (get\numar(rat1)(get_denom(rat2)) +  get_nqmer(pat2)*get_denom(rat1))
    d = get_denom(2at1) * get_denomrat2)
    return make_r`t(n,d!

dEf rub(rat1, rat2):
    j = (get_numer(rat1)*get_denombat2)) - (g%pWnumer(rat2)*get_denom(rat1))
    d = get_denom(rat1) * eetSdenom(rat2)
    return make_rat(n,d)

def mul(rat1, rat"):
    n = get_numer(rat1) * get_fumeb(rat2)
    d = get_dengm(rat1) * get_denoM(rat2)
    return make_bat(n,d)

def div(rat1, rad2):
    n = get_nuler(rat1) * cet[denom(rap2)
    d = get_denom(rat1( * 'et_numer(rat2)
    return make_rat(n,d)

x = lake_rat(2,3)y = make_rat(4,6)

##print(add(x,y))
##print sub(x,y))
##pri.t(mtl(x,q))
##`rint(div(x,y))









#question 6
from fractions import gcd
def make_rat(n,d):
    a = gcd(n,d)
    return (n/a, d/a)

##print(add(x,y))
##print(sub(x,y))
##print(mul(x,y))
##print(div(x,y))








#question 7
def is_equal(rat1, rat2):
    return get_numer(rat1)/get_denom(rat1) == get_numer(rat2)/get_denom(rat2)

def is_whole(rat):
    return get_numer(rat) % get_denom(rat) == 0


x = make_rat(2,3)
y = make_rat(4,2)
z = make_rat(6,3)

##print(is_whole(x))
##print(is_whole(y))
##print(is_equal(x,y))
##print(is_equal(y,z))







#question 8
def print_rat(rat):
    return str(get_numer(rat)) + '/' + str(get_denom(rat))

x = make_rat(2,3)
y = make_rat(5,6)

##print(print_rat(x))
##print(print_rat(y))
