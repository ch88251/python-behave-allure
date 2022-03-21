
def counting_valleys(n, s):
    curr_offset = 0
    below_sealevel = False
    valley_count = 0
    for i in s:
        if i not in 'UD':
            return
        if i == 'D':
            curr_offset -= 1
            if curr_offset < 0:
                below_sealevel = True
            continue
        elif i == 'U':
            curr_offset += 1
        if curr_offset < 0:
            below_sealevel = True
        if below_sealevel and curr_offset == 0:
            valley_count += 1

    return valley_count

