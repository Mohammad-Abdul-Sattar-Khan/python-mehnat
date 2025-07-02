def count(any_str, anylist):
    count = 0
    for x in anylist:
        if any_str == x:
            count += 1
    
    print(f"{any_str} is repeated {count} times.")

count("car", ["car", "car", "bike", "bike", "bike", "truck", "tractor", "tractor", "tractor", "tractor", "tractor"])
count("bike", ["car", "car", "bike", "bike", "bike", "truck", "tractor", "tractor", "tractor", "tractor", "tractor"])
count("truck", ["car", "car", "bike", "bike", "bike", "truck", "tractor", "tractor", "tractor", "tractor", "tractor"])
count("tractor", ["car", "car", "bike", "bike", "bike", "truck", "tractor", "tractor", "tractor", "tractor", "tractor"])