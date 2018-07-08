from enum import Enum, unique

@unique
class Month(Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12

for name, member in Month.__members__.items():
    print(name,'=>',member)
print(Month(12))