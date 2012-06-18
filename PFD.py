#!/usr/bin/env python


class VertexPFD:
    def __init__(self, a, b, c)
	self.pred = a
	self.preds = [0] * b
	self.succs = [0]


# ------------
# pfd_read_first
# ------------

def pfd_read_first (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array on int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0 and a[0] < 101
    assert a[1] > 0 and a[1] < 101
    return True


# -------------
# pfd_solve
# -------------

def pfd_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    
    while pfd_read(r, a) :
        v = pfd_eval(a[0], a[1])
        pfd_print(w, a[0], a[1], v)
