def hanoi(disks, source, target, auxiliary):
    if disks > 0:
        hanoi(disks - 1, source, auxiliary, target)
        print("Move disk %s from %s to %s" % (disks, source, target))
        hanoi(disks - 1, auxiliary, target, source)
    else:
        return


if __name__ == "__main__":
    hanoi(2, "A", "B", "C")
