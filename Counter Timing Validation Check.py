#Importing the required modules
import datetime
from datetime import timedelta

# Aliasing a datetime module
t = datetime.time

# Our status values
COUNTER_STARTED = "COUNTER_STARTED"
COUNTER_ON_PROGRESS="COUNTER_ON_PROGRESS"
BREAK="BREAK"
BREAK_OVER="BREAK_OVER"
COUNTER_ENDED="COUNTER_ENDED"
DIFFERENCE="DIFFERENCE"
TIME_NONE = "TIME NONE"
DIFF="DIFF"

# AM/PM to make more readable
def AM(hours):
    return hours

def PM(hours):
    return hours + 12

# Get the status for the specified time
def get_status(user_time):

    if user_time == t(AM(9),00) and t(PM(1),9):
        status = COUNTER_STARTED

    elif user_time == t(AM(11),15 or t(PM(11),30)):
        status = COUNTER_ON_PROGRESS

    elif user_time == t(PM(1),10) or user_time <= t(PM(2),00):
        status = BREAK

    elif user_time == t(PM(2),00):
        status = BREAK_OVER    

    elif user_time == t(PM(6),00):
        status = COUNTER_ENDED
    
    elif user_time == t(PM(2),15):
        dt_started = datetime.datetime(1,00)
        dt_ended = datetime.datetime(2,00)
        res=((dt_ended - dt_started).total_seconds())
        return res
        status = DIFF 

    else:
        status = TIME_NONE

    return status

# Convert a time to a human readable string
def time_to_string(t):
    return t.strftime('%I:%M %p')

# Testing the status of the previously defined function
def test(t, expect_status):
    status = get_status(t) #Assigning previous function to "status" variable
    print(time_to_string(t) + " = " + status + ": ", end = "")
    if status == expect_status:
        print("yes")
    else:
        print("No!")

#Finally running all the above defined functions here:
def run_tests(iteration):
    i=0
    for i in range(int(iteration)):
            # Run a test for each time period
            test(t(AM(9),00), COUNTER_STARTED)
            test(t(AM(1), 25), BREAK)
            test(t(AM(11), 15), COUNTER_ON_PROGRESS)
            print(test(t(AM(2), 15), DIFF))
            test(t(PM(6),00), COUNTER_ENDED)
            if i == str(5):
                break
            i=i+1

    print("Completed",i,"Iterations!")
run_tests(input(str("How many iteration needed ?")))