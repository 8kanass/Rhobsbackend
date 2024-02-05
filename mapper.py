#!/usr/bin/python
import sys

wealth_indicators = {}

for line in sys.stdin:
    if "a,b,c,d,e,f,g" in line:
        continue
    data = line.strip().split(",")
    if len(data) == 7:
        person_name = data[2] + ' ' + data[3]
        wealth_indicator = int(data[6])
        
        # Update wealth indicator for the person
        wealth_indicators[person_name] = wealth_indicator

sorted_wealth = sorted(wealth_indicators.items(), key=lambda x: x[1], reverse=True)

for i in range(3):
    if i >= len(sorted_wealth):
        break
    person, wealth = sorted_wealth[i]
    print("{0}\t{1}".format(person, wealth))

