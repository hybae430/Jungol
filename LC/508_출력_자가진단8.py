table = ["item", "count", "price", "pen", "20", "100", "note", "5", "95", "eraser", "110", "97"]

for idx, t in enumerate(table):
    if idx != 0 and not idx % 3:
        print()
    print("%10s" % t, end="")