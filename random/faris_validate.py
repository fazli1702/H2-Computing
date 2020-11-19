def validate(noOfSubjects):
    if noOfSubjects.isdigit():
        if int(noOfSubjects) >= 5 and int(noOfSubjects) <= 10:
            return True
        return False
    return False
    
