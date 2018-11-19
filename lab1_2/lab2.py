import itertools


def implies(a, b):
    if a:
        return b
    return True

def print_row(a, b, c, d):
    print("%s\t|%s\t|%s\t|%s" % (a, b, c, d))


def truth_table1(table):
    """return the truth table of: p or q -> r"""
    print_row("p", "q", "r", "pORq->r")
    for i in table:
        print_row(i[0], i[1], i[2], implies(i[0] or i[1], i[2]))


def truth_table2(table):
    """return the truth table of: r -> p and not q"""
    print_row("r", "p", "q", "r->pANDNOTq")
    for i in table:
        print_row(i[0], i[1], i[2], implies(i[0], i[1] and not i[2]))


the_table = list(itertools.product([False, True], repeat=3))

truth_table1(the_table)
print()
truth_table2(the_table)
