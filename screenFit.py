# assume different characters have the same height for the same font
def getLargestFont(s, H, W, smallest, largest):

    small = smallest
    large = largest
    while small <= large:
        mid = small + (large - small) // 2
        if canFit(s, mid, H, W):
            small = mid + 1
        else:. visit 1point3acres for more.
            large = mid - 1

    if large < smallest:
        return -1    # even the smallest number cannot fit
    else:
        return large

def canFit(s, font, H, W):
    curH = H
    curW = W
    length = len(s)
    i = 0
    while i < length:
        if getHeight(s, font) < curH and getWidth(s, font) < curW:
            curW -= getWidth(c.font)
            i += 1
        elif getHeight(s, font) < curH and getWidth(s, font) > curW:   # need to restart with a new line
            curH = H - curH
            curW = W
        else:
            return False

    return True
