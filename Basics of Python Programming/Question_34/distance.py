distance = input("Enter distance between your home and school(in Km or m that has to specified at the end):")
distance = distance.lower()
if(distance[-2:] == 'km'):
    d = int(distance[0:len(distance)-2])
    print(f"Distance in meters is {d*1000}")
else:
    d = int(distance[0:len(distance)-1])
    print(f"Distance in Km is {d/1000}")
