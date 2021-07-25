# After reviewing other submitted solutions, I liked this solution quite a bit, so I created a v2 of my solution
# The below solution is so efficient compared to mine. I'll get there one day.
# But for now, it's almost exactly what I did, I just did not use the built-in .count function. I need to keep that in
# mind for future scripts/implementations/katas
def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')