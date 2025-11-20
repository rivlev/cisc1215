class Time:
    """Represents the time of day."""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        s = f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
        print(s)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
    def int_to_time(seconds):
        minute, second = divmod(seconds, 60)
        hour, minute = divmod(minute, 60)
        return Time(hour, minute, second)

    def add_time(self, hours, minutes, seconds):
        duration = Time(hours, minutes, seconds)
        seconds = self.time_to_int() + duration.time_to_int()
        return Time.int_to_time(seconds)
    
    def is_after(self, other_time):
        assert self.is_valid(), 'self is not a valid Time'
        assert other_time.is_valid(), 'other_time is not a valid Time'
        return self.time_to_int() > other_time.time_to_int()
    
    def __str__(self):
        s = f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
        return s
    
    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return Time.int_to_time(seconds)
    
    def is_valid(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        if not isinstance(self.hour, int):
            return False
        if not isinstance(self.minute, int):
            return False
        return True
    
 
start = Time(9, 10, 11)

print(start)

end = Time(1, 35, 0)

print(start + end)

duration = Time(minute=132)
print(duration)

start.is_after(duration)