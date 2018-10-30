def move_disk(disk, start, end):
    print("moved disk %s from %s to %s" % (disk, start, end))
    return 1


def move_tower(disk, start, end, temp):
    if disk == 1:
        return move_disk(disk, start, end)
    return move_tower(disk - 1, start, temp, end) + move_disk(disk, start, end) + move_tower(disk - 1, temp, end, start)


print("moves = %s" % move_tower(3, "A", "B", "C"))
