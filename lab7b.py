#!/usr/bin/env python3
# Student ID: vmpatel41

class Time:
    """Simple object type for time of the day."""

    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


def format_time(t):
    """Return a Time object as a formatted string."""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'


def sum_times(t1, t2):
    """Add two Time objects and return a new Time object."""
    result = Time(0, 0, 0)

    result.hour = t1.hour + t2.hour
    result.minute = t1.minute + t2.minute
    result.second = t1.second + t2.second

    while result.second >= 60:
        result.second -= 60
        result.minute += 1

    while result.minute >= 60:
        result.minute -= 60
        result.hour += 1

    return result


def change_time(time, seconds):
    """Modify a Time object by adding or subtracting seconds."""
    time.second += seconds

    while time.second >= 60:
        time.second -= 60
        time.minute += 1

    while time.second < 0:
        time.second += 60
        time.minute -= 1

    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    while time.minute < 0:
        time.minute += 60
        time.hour -= 1

    return None


def valid_time(t):
    """Return True if the Time object contains valid values."""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False

    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False

    return True
