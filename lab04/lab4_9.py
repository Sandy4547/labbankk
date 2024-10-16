def line(ch, nch):
    print(ch * nch)

def block(ch, nLine, nch):
    for _ in range(nLine):
        line(ch, nch)

block("x", 4, 7)