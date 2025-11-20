class Date:
    def __init__(self, year=1973, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.month}/{self.day}/{self.year}"
    
    def to_tuple(self):
        return self.year, self.month, self.day
    
    def is_after(self, other):
        return self.to_tuple() > other.to_tuple()
        

date1 = Date(1933, 6, 22)
date2 = Date(1933, 9, 17)

print(date1)
print(date2)
print(date1.is_after(date2))