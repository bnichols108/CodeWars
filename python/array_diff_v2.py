# After reviewing several solutions from other users, this solution stuck out to me. Super basic and clean. Granted,
# could be tougher for newer devs to understand what's going on, as it took me a little bit of reading to understand it.
# But I'm wanting to get to this point where I can see this elegant solution when tackling a problem. Work in progress.
def array_diff(a, b):
    return [x for x in a if x not in b]

