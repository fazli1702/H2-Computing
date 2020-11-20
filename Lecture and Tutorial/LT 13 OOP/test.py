def get_date_today():
    return (2013, 10, 30)

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


#Your code here
paramore = Band('Paramore', (2004, 1, 1), (Artist('Hayley Wiliams', (1988, 12, 27)), Artist('Zac Farro', (1990, 6, 4)), Artist('Taylor York', (1989, 12, 17))))


print(paramore.formation_age())
print(paramore.members[1].get_name())
print(paramore.members[0].get_name())
print(paramore.members[2].age())
print(round(paramore.age(),1))
