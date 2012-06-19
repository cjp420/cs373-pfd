#!/usr/bin/env python


class VertexPFD:
    def __init__(self, b) :
	self.done = False
	self.id = b[0]
	self.pred = b[1]
	self.preds = []
	self.succ = []
	i = 2
	while i < len(b) :
	    self.preds.append (b[i]) 
	    i += 1


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
	b.append (int(l[i]))
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
    vs is the dict of VertexPFD with the key equal to the vertex number
    """ 
    assert len (vs) > 0
    r = []
    low = 0
    while  True:
        z = []
        for i in vs.keys() :
	    if vs[i].pred == 0 and not vs[i].done :
	        z.append (vs[i].id)
        if len (z) == 0 :
            break
        low = 105
        j = 0
        while j < len (z) :
	    if z[j] < low :
	        low = z[j]
	    j += 1
        r.append (low)
        vs[low].done = True
        for k in vs[low].succ :
	    vs[k].pred -= 1
    assert len (r) > 0
    return r
	  


# -------------
# pfd_print
# -------------

def pfd_print (w, re) :
    """
    prints the resulting permutation that is passed in
    r is the list of ints that holds the result
    """   
    s = ""
    for i in re :
	s += (str (i) + " ")
    s += "\n"
    w.write (s)

# -------------
# pfd_solve
# -------------

def pfd_solve (r, w) :
    """
    read, eval, print 
    r is a reader
    w is a writer
    """
    a = [0, 0]
    pfd_read_first(r, a)
    b = []
    vs = dict()
    i = 1
    while i <= a[0] :
        vs[i] = VertexPFD([i, 0])
	i += 1
    while pfd_read_rest(r, b) :
        vs[b[0]].pred = b[1]
	print b[0]
	print (vs[b[0]].pred)
        k = 2
	while k < len(b) :
	    vs[b[0]].preds.append (b[k])
	    print (str (vs[b[0]].preds)) 
	    k += 1
        del b[:]
    for i in vs.keys() :
	if vs[i].pred != 0 :
	    for j in vs[i].preds :
		vs[j].succ.append (vs[i].id)
		print (str (vs[j].succ) )
    re = pfd_eval (vs)
    pfd_print (w, re)

	
