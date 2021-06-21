countries = [ "Ireland", "Mongolia", "Norway", "New Zealand", "Brazil", 
                "Colombia", "Canada", "Ukraine", "Thailand", "Libya" ]

city_names = [ 'Oakland', 'Atlanta', 'New York', 'Seattle', 'Memphis', 'Miami', 'Boston', 'Los Angeles', 'Denver', 'New Orleans']

city_names[0] ='San Francisco'
city_names[2] = 'Brooklyn'
city_names[-3] = 'Hollywood'
city_names[5] = 'Tampa'

print(city_names)

city_names.append('New Jersey')     #adds data to END of list
city_names.extend(['Santa Cruz', 'Dallas', 'Dublin'])   #add one list to another list
city_names.insert(7, 'Washington, D.C')     #adds data at a specific index

print(city_names)

del city_names[7]   #deletes city @ index
city_names.pop(0)   #removed element according to index
city_names.remove('Boston')  #removes specific element that matches ''

print(city_names)