#towerofhanoi : 3 towers (source,auxiliary and destination)

def toh(n, source, destination, spare):
    if n == 1:
        print("Disk 1 Moved From Tower",source,"To Tower",destination)
        return
    toh(n-1,source,spare,destination)
    print("Disk",n,"Moved From Tower",source,"To Tower",destination)
    toh(n-1,spare, destination, source)

n = int(input("Enter the total Disks: "))
toh(n,'A','C','B')
