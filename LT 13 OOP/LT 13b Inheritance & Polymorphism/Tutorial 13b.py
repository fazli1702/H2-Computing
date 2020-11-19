#question 1
class Mammal(object):
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def say(self):
        return 'What does the ' + str(self.name) + ' says'

    


#question 2
class Dog(Mammal):
    def __init__(self):
        super().__init__('Dog')

class Cat(Mammal):
    def __init__(self):
        super().__init__('Cat')
        
class Fox(Mammal):
    def __init__(self):
        super().__init__('Fox')



#question 3
class Dog(Mammal):
    def __init__(self):
        super().__init__('Dog')

    def say(self):
        return 'Woof'

class Cat(Mammal):
    def __init__(self):
        super().__init__('Cat')

    def say(self):
        return 'Meow'
        
class Fox(Mammal):
    def __init__(self):
        super().__init__('Fox')

    def say(self):
        return "Ring-ding-ding-ding-dingeringeding"




#question 4
class Artist(object):
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
        
    def get_name(self):
        return self.name
        
        
    def get_dob(self):
        return self.dob
        
        
# Used for public test cases.
# You DO NOT have to include this in your submission.
jt = Artist("Justin Timberlake", (1981, 1, 31))


##print(jt.get_name())
##print(jt.get_dob())
##print(Artist("JC Chasez", (1976, 8, 8)).get_name())
##print(Artist("JC Chasez", (1976, 8, 8)).get_dob())





#question 5
class Artist:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
    def get_name(self):
        return self.name
    
    def get_dob(self):
        return self.dob
        
    def age(self):
        year = self.dob[0]
        month = self.dob[1]
        day = self.dob[2]
        today = get_date_today()
        c_age = today[0] - year
        
        if (today[1], today[2]) < (month, day):
            return c_age - 1
        else:
            return c_age
            
        
        
def get_date_today():
    return (2013, 10, 30)

# Used for public test cases.
# You DO NOT have to include this in your submission
jt = Artist("Justin Timberlake", (1981, 1, 31))


##print(jt.age())
##print(Artist('Hayley Williams', (1988, 12, 27)).age())





#question 6
class Duration:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds
        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        self.total_seconds = self.seconds + self.minutes * 60

    def get_minutes(self):
        return self.minutes

    def get_seconds(self):
        return self.seconds

    def total_seconds(self):
        return (int(self.minutes) * 60) + int(self.seconds)


##print((Duration(3, 30)).total_seconds)












#question 7
class Duration:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds
        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        self.total_seconds = self.seconds + self.minutes * 60

    def __str__(self):
        if self.minutes < 10:
            n_min = '0' + str(self.minutes)
        else:
            n_min = str(self.minutes)
            
        if self.seconds < 10:
            n_sec = '0' + str(self.seconds)
        else:
            n_sec = str(self.seconds)

        return n_min + ':' + n_sec


##print(str(Duration(3, 20)))
##print(str(Duration(0, 0)))
##print(str(Duration(103, 20)))
##print(str(Duration(5, 70)))








#question 8
class Duration:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds
        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        self.total_seconds = self.seconds + self.minutes * 60

    def __str__(self):
        if self.minutes < 10:
            n_min = '0' + str(self.minutes)
        else:
            n_min = str(self.minutes)
            
        if self.seconds < 10:
            n_sec = '0' + str(self.seconds)
        else:
            n_sec = str(self.seconds)

        return n_min + ':' + n_sec

    def __add__(self, object):
        return Duration(self.minutes + object.minutes, self.seconds + object.seconds)


##print(str(Duration(0,20) + Duration(0,30)))
##print(str(Duration(4,40) + Duration(4,30)))
##print(str(Duration(0,0) + Duration(0,0)))








#quesrion 9
class Artist:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
    def get_name(self):
        return self.name
    
    def get_dob(self):
        return self.dob
        
    def age(self):
        year = self.dob[0]
        month = self.dob[1]
        day = self.dob[2]
        today = get_date_today()
        c_age = today[0] - year
        
        if (today[1], today[2]) < (month, day):
            return c_age - 1
        else:
            return c_age


class Duration:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds
        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        self.total_seconds = self.seconds + self.minutes * 60

    def get_minutes(self):
        return self.minutes

    def get_seconds(self):
        return self.seconds

    def __str__(self):
        if self.minutes < 10:
            n_min = '0' + str(self.minutes)
        else:
            n_min = str(self.minutes)
            
        if self.seconds < 10:
            n_sec = '0' + str(self.seconds)
        else:
            n_sec = str(self.seconds)

        return n_min + ':' + n_sec

    def __add__(self, object):
        return Duration(self.minutes + object.minutes, self.seconds + object.seconds)


class Song:
    def __init__(self, artist, title, duration):
        self.artist = artist
        self.title = title
        self.duration = duration

    def get_artist(self):
        return self.artist

    def get_title(self):
        return self.title

    def get_duration(self):
        return self.duration



test = Song(Artist('name', (1988, 12, 27)), 'title', Duration(4, 20))
##print(test.get_artist().get_name())
##print(test.get_duration().get_minutes())












#question 10
class Album:
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def total_runtime(self):
        total_time = Duration(0, 0)
        for song in self.songs:
            total_time += song.get_duration()
        return total_time

    










#question 11
class Band(Artist):
    def __init__(self, name, dob, members):
        super().__init__(name, dob)
        self.members = members
        
    def formation_age(self):
        return super().age()

    def age(self):
        total_age = 0
        for member in self.members:
            total_age += member.age()

        return total_age / len(self.members)


    
paramore = Band('Paramore', (2004, 1, 1), (Artist('Hayley Wiliams', (1988, 12, 27)), Artist('Zac Farro', (1990, 6, 4)), Artist('Taylor York', (1989, 12, 17))))

print(paramore.formation_age())
print(paramore.members[1].get_name())
print(paramore.members[0].get_name())
print(paramore.members[2].age())
print(round(paramore.age(),1))

