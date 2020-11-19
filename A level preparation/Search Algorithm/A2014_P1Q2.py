def BinarySearch(ThisArray, FindValue, Low, High, n=0):
    Middle = 0
    if len(ThisArray) == 1 and ThisArray[0] !=  FindValue:
        return -1, n
    else:
        Middle = (Low + High) // 2
        if ThisArray[Middle] > FindValue:
            return BinarySearch(ThisArray, FindValue, Low, Middle-1, n+1)
        elif ThisArray[Middle] < FindValue:
            return BinarySearch(ThisArray, FindValue, Middle+1, High, n+1)
        else:
            return Middle, n







MyAnimal = [None for i in range(33)]
MyAnimal[0]="aardvark"
MyAnimal[1]="ant"
MyAnimal[2]="antelope"
MyAnimal[3]="bat"
MyAnimal[4]="boa constrictor"
MyAnimal[5]="camel"
MyAnimal[6]="cat"
MyAnimal[7]="cheetah"
MyAnimal[8]="dog"
MyAnimal[9]="donkey"
MyAnimal[10]="duck"
MyAnimal[11]="elephant"
MyAnimal[12]="frog"
MyAnimal[13]="giraffe"
MyAnimal[14]="hare"
MyAnimal[15]="horse"
MyAnimal[16]="iguana"
MyAnimal[17]="jackass"
MyAnimal[18]="jaguar"
MyAnimal[19]="leopard"
MyAnimal[20]="lion"
MyAnimal[21]="llama"
MyAnimal[22]="mouse"
MyAnimal[23]="ostrich"
MyAnimal[24]="panther"
MyAnimal[25]="parrot"
MyAnimal[26]="rhinoceros"
MyAnimal[27]="seahorse"
MyAnimal[28]="seal"
MyAnimal[29]="spider"
MyAnimal[30]="turtle"
MyAnimal[31]="whale"
MyAnimal[32]="zebra"


print(BinarySearch(MyAnimal, 'seal', 0, len(MyAnimal)-1))
