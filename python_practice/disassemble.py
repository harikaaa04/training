import dis

def mult(a, b):
    return a*b 

def sev():
    x = 7
    return x+3

def forloop():
    for _ in range(3):
        print("hi")


dis.dis(mult)
dis.dis(sev)
dis.dis(forloop)
# dis.dis(dis)