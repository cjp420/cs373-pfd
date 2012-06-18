#!/usr/bin/env python

"""
class VertexPFD:
    def __init__(self, a, b, c)
	self.pred = a
	self.preds = [0] * b
	self.succs = [0]
"""


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

# --------------
# pfd_read_rest
# --------------

def pfd_read_rest (r, b) :
    """
    reads a line of ints
    r is a reader
    b is a list of ints
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    i = 0
    while i < len(l) :
	b[i] = int(l[i])
	i += 1
    for j in b :
	assert j > -1 and j <101
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
    a = [0, 0]
    b = [0] * 102
    pfd_read_first(r, a)
    while pfd_read_rest(r, b, vs) :
        v = pfd_eval(a[0], a[1])
        pfd_print(w, a[0], a[1], v)
