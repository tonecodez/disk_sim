import sys
import random

DISK_SIZE = 10000

# FCFS
#
# Services request based on time arrived (left to right)
#
def fcfs(start, disk, direct):
    
    head_changes = 0
    dist = 1
    curr_pos = start
  
    disk = list(map(int, disk))

    # Takes in the processes by index, since it is first come first serve, and
    # removes them and uses the difference to calculate distance
    for x in range(len(disk)):

        dest = curr_pos - disk[x]

        if dest > 0: 
            if direct == 1:
                head_changes += 1
                direct = 0
        
        if dest < 0:
            if direct == 0:
                head_changes += 1
                direct = 1

        dist += abs(dest)
        curr_pos = disk[x]

    print("FCFS   " + (" ".join(map(str, disk))))

    return " ".join(map(str, ["FCFS  ", head_changes, dist])) 

# Shortest Seek Time First
#
# Seeks out the shortest seek time in all requests
#
def sstf(start, disk, direct):
    
    head_changes = 0
    dist = 1
    curr_pos = start
    history = []

    disk = list(map(int, disk))

    # finds the minumum distance between the current point and a value held
    # within the list and sets that to the new value. Does this until all of the
    # values in the list are exhausted.
    for x in range(len(disk)): 
        
        min_dist = min(disk, key = lambda x: abs(x-curr_pos))
        dest = curr_pos - min_dist

        if dest > 0: 
            if direct == 1:
                head_changes += 1
                direct = 0
        
        if dest < 0:
            if direct == 0:
                head_changes += 1
                direct = 1

        dist += abs(dest) 
        curr_pos = min_dist
        history.append(min_dist)
        disk.remove(min_dist)

    print("SSTF   " + (" ".join(map(str, history))))  

    return " ".join(map(str, ["SSTF  ", head_changes, dist])) 

# Scan
#
# Scans in both directions and services as it goes along
# Scans to the min and the max
#
def scan(start, disk, direct):

    head_changes = 0
    dist = 1
    curr_pos = start
    history = []

    disk = list(map(int, disk))

    # This is the closest to a 'real' simulation, in that it actually steps over
    # and counts each of the indices that it goes over. SCAN, C-SCAN, LOOK, and
    # C-LOOK all follow the exact same patterns, with the caveat that the 'C'
    # variations do not collect from the disk when moving towards lower numbers.
    while disk:

        if direct:
            while curr_pos in disk:
                disk.remove(curr_pos)
                history.append(curr_pos)
            
            if disk:
                if curr_pos == DISK_SIZE - 1:
                    direct = 0
                    curr_pos -= 1
                    dist += 1
                    head_changes += 1
                else:
                   curr_pos += 1
                   dist += 1
        else:
            while curr_pos in disk:
                disk.remove(curr_pos)
                history.append(curr_pos)
           
            if disk:
                if curr_pos == 0:
                    direct = 1
                    head_changes += 1
                else: 
                   curr_pos -= 1
                   dist += 1

    print("SCAN   " + (" ".join(map(str, history))))

    return " ".join(map(str, ["SCAN  ", head_changes, dist])) 

# C-Scan
#
# Scans in both directions and services only going up
# Scans to the min and the max
#
def cscan(start, disk, direct):
    
    head_changes = 0
    dist = 1
    curr_pos = start
    done = False
    history = []

    disk = list(map(int, disk))

    while disk:

        if direct:
            while curr_pos in disk:
                disk.remove(curr_pos)
                history.append(curr_pos)
            
            if disk:
                if curr_pos == DISK_SIZE - 1:
                    direct = 0
                    curr_pos -= 1
                    dist += 1
                    head_changes += 1
                else:
                   curr_pos += 1
                   dist += 1
        else:
            if curr_pos == 0:
                direct = 1
                head_changes += 1
            else: 
               curr_pos -= 1
               dist += 1

    print("C-SCAN " + (" ".join(map(str, history))))

    return " ".join(map(str, ["C-SCAN", head_changes, dist])) 

# Look
#
# Scans in both directions and services any request it sees
# Only scans until max and min of the request pool
#
def look(start, disk, direct):

    head_changes = 0
    dist = 1
    curr_pos = start
    history = []

    disk = list(map(int, disk))

    max_val = max(disk)
    min_val = min(disk)  

    # Switches the direction of the head if it is out of range of the max and
    # the min value.
    if curr_pos < min_val and direct == 0:
        direct = 1
        head_changes += 1
        dist += (min_val - curr_pos)
        curr_pos = min_val

    elif curr_pos > max_val and direct == 1:
        direct = 0
        head_changes += 1
        dist += (curr_pos - max_val)
        curr_pos = max_val

    while disk:

        if direct:
            while curr_pos in disk:
                disk.remove(curr_pos)
                history.append(curr_pos)
            
            if disk:
                if curr_pos == max_val:
                    direct = 0
                    curr_pos -= 1
                    dist += 1
                    head_changes += 1
                else:
                   curr_pos += 1
                   dist += 1
        else:
            while curr_pos in disk:
                disk.remove(curr_pos)
                history.append(curr_pos)
           
            if disk:
                if curr_pos == min_val:
                    direct = 1
                    head_changes += 1
                else: 
                   curr_pos -= 1
                   dist += 1


    print("LOOK   " + (" ".join(map(str, history))))

    return " ".join(map(str, ["LOOK  ", head_changes, dist])) 

# C-Look
#
# Scans in both directions and services only going up
# Only scans until max and min of the request pool
#
def clook(start, disk, direct):
    
    head_changes = 0
    dist = 1
    curr_pos = start
    history = []

    disk = list(map(int, disk))

    max_val = max(disk)
    min_val = min(disk)

    if curr_pos < min_val and direct == 0:
        direct = 1
        head_changes += 1
        dist += (min_val - curr_pos)
        curr_pos = min_val

    elif curr_pos > max_val and direct == 1:
        direct = 0
        head_changes += 1
        dist += (curr_pos - max_val)
        curr_pos = max_val

    while disk:

        if direct:
            while curr_pos in disk:
                disk.remove(curr_pos)
                history.append(curr_pos)
            
            if disk:
                if curr_pos == max_val:
                    direct = 0
                    curr_pos -= 1
                    dist += 1
                    head_changes += 1
                else:
                   curr_pos += 1
                   dist += 1
        else:
            if curr_pos == min_val:
                direct = 1
                head_changes += 1
            else:
               curr_pos -= 1
               dist += 1
                

    print("C-LOOK " + (" ".join(map(str, history))))
    
    return " ".join(map(str, ["C-LOOK", head_changes, dist])) 

def gen_rand(gen):
    
    disk_arr = random.sample(range(0, DISK_SIZE), gen) 

    return disk_arr

def check_rand(r):
    
    gen = 0

    if (r[0] == 'R'):
         
        if (len(r) > 1):
            num = int (r[1:])
            print("{} randomly generated requests".format(num))
            gen = num
        
        else:
            print("1000 randomly generated requests")
            gen = 1000

    return gen

def main():
    
    args = sys.argv[1:]

    if len(args) == 0:
        print("error")
        exit(1)
    
    elif len(args) == 1:
        gen = check_rand(args[0])
        
        if gen > 0:
            requests  = gen_rand(gen) 
            start     = random.randint(0, DISK_SIZE)
            direction = random.randint(0,1)

    else:
        start = int (args[0])

        if len(args) < 3:
            print("error")
            exit(1)

        elif args[1] == 'H':
            direction = 1

        elif args[1] == 'L':
            direction = 0

        else:
            print("error")
            exit(1)

        requests = args[2:]
        
        gen = check_rand(requests[0])

        if gen > 0:
            requests = gen_rand(gen)
    
    
    check = list(map(int, requests))
    
    if any( i > 9999 for i in check):
        print("request for disk not valid")
        exit(1)

    print("Start at disk {}".format(start))
    print("Moving towards {} disks".format("higher" if direction else "lower")) 

    print("\n== Service history ==")

    info = []

    info.append(fcfs(start, requests, direction))
    info.append(sstf(start, requests, direction))
    info.append(scan(start, requests, direction))
    info.append(cscan(start, requests, direction))
    info.append(look(start, requests, direction))
    info.append(clook(start, requests, direction))

    print("== Service stats ==")

    print(" \n".join(map(str, info)))

main()
