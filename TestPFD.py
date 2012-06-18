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

from PFD import pfd_read_first, pfd_read_rest

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
        a = [0] * 102
        b = pfd_read_rest(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)
	self.assert_(a[2] == 20)
	self.assert_(a[3] == 30)
	self.assert_(a[4] == 40)

    def test_read_rest_2 (self) :
        r = StringIO.StringIO("")
        a = [0] * 102
        b = pfd_read_rest(r, a)
        self.assert_(b == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)

    def test_read_rest_3 (self) :
        r = StringIO.StringIO("1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 \n")
        a = [0] * 102
        b = pfd_read_rest(r, a)
        self.assert_(b == True)
	i = 0
	while i < 102 :
            self.assert_(a[i] == 1)
	    i += 1

# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
