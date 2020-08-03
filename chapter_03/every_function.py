#!/usr/bin/env python3

places_to_visit = ['Dublin', 'Tokyo', 'Boston', 'Berlin', 'Toronto']

print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)
print(sorted(places_to_visit, reverse=True))
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse=True)
print(places_to_visit)
del places_to_visit[0]
print(places_to_visit)
places_to_visit.pop()
print(places_to_visit)
places_to_visit.insert(0, 'Denver')
print(places_to_visit)
places_to_visit.remove('Boston')
print(places_to_visit)
