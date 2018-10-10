#store_open.py
# Checks whether store is open depending on schedule for the week

"""
  monday: 10am -> 4pm
  tuesday: 10am -> 4pm
  wednesday: 11am -> 8pm
  thursday: 11am -> 8pm
  friday: 11am -> 2am
  saturday: 5pm -> 4am
"""
# day of week: 1 -> Monday, 2 -> Tuesday, ..., 7 -> Sunday
# time store as minutes since midnight
example = [
  ([1, 2], [(10 * 60, 12 * 60), (15 * 60, 18*60)]),
  ([3, 4], [(11 * 60, 20 * 60)]),
  ([5], [(11 * 60, 2 * 60)]),
  ([6], [(17 * 60, 4 * 60)]),
]


for day in example:
  # print day[0], day[1]
  if 5 in day[0]:
    for i in range(len(day[1])):
      print day[i]


def is_store_open(example, dt):
    
    intDay = _day_of_week(dt)
    time_till_midnight = _minutes_since_midnight(dt)/60
    
    for ele in example:
        if intDay in ele[0]:
          timings = ele[1]
          for time in ele[1]:
              print time
              
              startTime = time[0]
              endTime = time[1]
              if time_till_midnight >= startTime and time_till_midnight <= endTime:
                  return True
            
        
    return False # or True

# Helper functions
import datetime
def _minutes_since_midnight(dt):
    midnight = datetime.datetime.combine(dt.date(), datetime.time())
    return (dt - midnight).seconds / 60

def _day_of_week(dt):
    return dt.isoweekday()

today =  datetime.datetime.utcnow()

result = is_store_open(example,today)
print result

# friday = example[2]
# print friday[1][0][1]/60