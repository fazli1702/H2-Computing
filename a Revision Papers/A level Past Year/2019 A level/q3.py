# Task 3.1
class ToDo:
    def __init__(self, c, d):
        self.category = c
        self.description = d
        
    def set_category(self, s):
        self.category = s
        
    def set_descritption(self, s):
        self.description = s
        
    def get_category(self):
        return self.category
    
    def get_description(self):
        return self.description
    
    def compare_with(self, td):
        if self.category < td.get_category():
            return -1
        
        elif self.category == td.get_category():
            if self.description < td.get_description():
                return -1
            elif self.description > td.get_description():
                return 1 
            else:
                return 0
        
        else:
            return 1
    
    def summary(self):
        print('category: {}, description: {}'.format(self.category, self.description))


def main():
    activities = [
    ToDo("reading", "Try some Shakespeare"),
    ToDo("shopping", "Consider items to recycle"),
    ToDo("reading", "Search on the web"),
    ToDo("reading", "Go to the library")
    ]

    output = []

    i = 0
    for activity in activities:
        print('activity:', activity.summary())
        print('i', i)
        if len(output) == 0:
            output.append(activity)
        else:
            insert = False
            for i, ele in enumerate(output):
                if activity.compare_with(ele) == -1:
                    output.insert(i, activity)
                    insert = True
                    
            # end of list
            if not insert:
                output.append(activity)
        i += 1
                    

##    for ele in output:
##        ele.summary()


main()
