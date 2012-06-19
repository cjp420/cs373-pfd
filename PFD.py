#!/usr/bin/env python


class VertexPFD:
    def __init__(self, b) :
	self.id = b[0]
	self.pred = b[1]
	self.preds = [0] * b[1]
	self.succ = []
	i = 2
	while i < len(b) :
	    self.preds[i - 2] = b[i] 


# ------------
# pfd_compare
# ------------
"""
compare function for sorting the list of VertexPFD so they will be be at the correct index
"""
def compare(a, b):
        return cmp(int(a.id), int(b.id))



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
# pfd_eval
# -------------

def pfd_eval (vs) :
    """
    solves the tasks for a permutation that is a valid order of the tasks
    vs is the list of VertexPFD with the index equal to the vertex number
    """ 
    z = []
    for i in vs :
	  


# -------------
# pfd_print
# -------------

def pfd_print (r) :
    """
    prints the resulting permutation that is passed in
    r is the list of ints that holds the result
    return
    """   
       

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
    b = [0] * 100
    pfd_read_first(r, a)
    c = [0] * a[0]
    vs = [None]
    while pfd_read_rest(r, b) :
        v = VertexPFD(b)
	vs.append(v)
    vs.sort(compare)
    for i in vs :
	if i.pred != 0 :
	    for j in i.preds :
		vs[j].succ.append (i.id)
    r = pfd_solve (vs)

	
