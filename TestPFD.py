#!/usr/bin/env python

"""
To test the program:
    % python TestPFD.py > TestPFD.py.out
    % chmod ugo+x TestPFD.py
    % TestPFD.py > TestPFD.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from PFD import pfd_read_first, pfd_read_rest, pfd_print, pfd_eval, pfd_solve, VertexPFD

# -----------
# TestPFD
# -----------

class TestPFD (unittest.TestCase) :
    # ----
    # read_first
    # ----

    def test_read_first_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = pfd_read_first(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_first_2 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = pfd_read_first(r, a)
        self.assert_(b == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)

    def test_read_first_3 (self) :
        r = StringIO.StringIO("100 100 89\n")
        a = [0, 0]
        b = pfd_read_first(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 100)
    # --------
    # read_rest
    # --------

    def test_read_rest_1 (self) :
        r = StringIO.StringIO("1 10 20 30 40\n")
        a = []
        b = pfd_read_rest(r, a)
        self.assert_(b == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)
	self.assert_(a[2] == 20)
	self.assert_(a[3] == 30)
	self.assert_(a[4] == 40)

    def test_read_rest_2 (self) :
        r = StringIO.StringIO("")
        a = []
        b = pfd_read_rest(r, a)
        self.assert_(b == False)
        self.assert_(len(a) == 0)

    def test_read_rest_3 (self) :
        r = StringIO.StringIO("1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 \n")
        a = []
        b = pfd_read_rest(r, a)
        self.assert_(b == True)
	i = 0
	while i < 102 :
            self.assert_(a[i] == 1)
	    i += 1

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 5 3 2 4 \n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("3 2\n1 2 2 3\n2 1 3\n")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "3 2 1 \n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("4 2\n1 3 2 3 4\n2 2 3 4 \n")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "3 4 2 1 \n")


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        pfd_print(w, [1, 10, 20])
	s = w.getvalue()
	#print (s)
        self.assert_(s == "1 10 20 \n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        pfd_print(w, [1])
	s = w.getvalue()
	#print (s)
        self.assert_(s == "1 \n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        pfd_print(w, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
	s = w.getvalue()
	#print(s)
        self.assert_(s == "10 9 8 7 6 5 4 3 2 1 \n")

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
	b = [[3, 2, 1, 5], [2, 2, 5, 3], [4, 1, 3], [5, 1, 1]]
	vs = dict()
        i = 1       
	while i <= 4 :
            vs[b[i-1][0]] = VertexPFD(b[i-1])
	    i += 1
	vs[1] = VertexPFD([1, 0])
	vs[1].succ = [5, 3]
	vs[3].succ = [2, 4]
	vs[5].succ = [2, 3]
	r = pfd_eval(vs)
        self.assert_(r == [1, 5, 3, 2, 4])

    def test_eval_2 (self) :
	b = [[1, 2, 2, 3], [2, 1, 3]]
	vs = dict()
        i = 1       
	while i <= 2 :
            vs[b[i-1][0]] = VertexPFD(b[i-1])
	    i += 1
	vs[3] = VertexPFD([3, 0])
	vs[1].succ = [2]
	vs[2].succ = [1]
	vs[3].succ = [1, 2]
	r = pfd_eval(vs)
        self.assert_(r == [3, 2, 1])

    def test_eval_3 (self) :
	b = [[1, 3, 2, 3, 4], [2, 2, 3, 4]]
	vs = dict()
        i = 1       
	while i <= 2 :
            vs[b[i-1][0]] = VertexPFD(b[i-1])
	    i += 1
	vs[3] = VertexPFD([3, 0])
	vs[4] = VertexPFD([4, 0])
	vs[2].succ = [1]
	vs[3].succ = [1, 2]
	vs[4].succ = [1, 2]
	r = pfd_eval(vs)
        self.assert_(r == [3, 4, 2, 1])





# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
