from City import City

filename = 'climates.csv'

with open(filename, 'w') as file:
      file.write('City, Low min, Low max, High min, High max, Sunshine\n')
      
cities = ['Bratislava', 'Prague', 'Budapest', 'Vienna', 'Leipzig', 'Berlin', 'Hamburg', 'Zurich', 'Amsterdam', 'Paris', 'London', 'Edinburgh', 'St_Andrews', 'Milan', 'Barcelona', 'Madrid', 'Lisbon', 'Tenerife']
cities += ['Boston', 'Raleigh', 'Phoenix,_Arizona', 'Los_Angeles', 'San_Francisco', 'Seattle', 'Vancouver', 'Toronto']
cities += ['Singapore', 'Brisbane', 'Melbourne', 'Sydney', 'Perth', 'Auckland', 'Dunedin', 'Wellington']

for city in cities:
  C = City(city)
  C.parse_page()
  C.save(filename)
