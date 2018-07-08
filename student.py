class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s'%(self.__name,self.__score))

    def get_name(self):
        return self.__name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')
        if value <0 or value >100:
            raise ValueError('score must between 0~100')
        self.__score = value

    def get_grade(self):
        if self.__score >=90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C'

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self,value):
        self.__birth = value
        
    @property
    def age(self):
        return 2017-self.__birth

bart = Student('Bart Simpson',59)
bart.print_score()
bart.get_grade()