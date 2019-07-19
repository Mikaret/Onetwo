import datetime, os, signal, subprocess, sys, time, unittest

def run(command, stdin = None, timeout = 30):
    """
    Runs the specified command using specified standard input (if any) and
    returns the output on success. If the command doesn't return within the
    specified time (in seconds), "__TIMEOUT__" is returned.
    """

    start = datetime.datetime.now()
    process = subprocess.Popen(command.split(),
                               stdin = subprocess.PIPE, 
                               stdout = subprocess.PIPE,
                               stderr = subprocess.STDOUT)
    if not stdin is None:
        process.stdin.write(stdin)
        process.stdin.close()
    while process.poll() is None:
        time.sleep(0.1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return "__TIMEOUT__"
    return process.stdout.read()
	
def check_style(filename):
    """
    Runs pep8 on the specified Python file and returns 
    (<pep8 output>, <# of style violations>).
    """

    output = ""
    try:
        output = subprocess.check_output(["pep8", filename], 
                                         stderr = subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output
    return output, len(output.splitlines())
	
class Problem1(unittest.TestCase):

    def test1(self):
        """ Problem 1. Correctness) """
        
        command = "python validDNA.py ACTGACG"
        sought = """True
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

    def test2(self):
        """ Problem 1. Correctness) """

        command = "python validDNA.py TGAGCCGTAGCXCTATACTTATAGC"
        sought = """False
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
        
    def test3(self):
        """ Problem 1. Style """

        output, violations = check_style("validDNA.py")
        self.assertEquals(violations, 0, output)

class Problem2(unittest.TestCase):

    def test1(self):
        """ Problem 2. Correctness """
        command = "python validISBN.py 0-13-407643-5"
        sought = """True
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
        
    def test2(self):
        """ Problem 2. Correctness """
        command = "python validISBN.py 02-0-131452-4"
        sought = """False
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
        
    def test3(self):
        """ Problem 2. Correctness """
        command = "python validISBN.py 02-013-145-2-5"
        sought = """True
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
    
    def test4(self):
        """ Problem 2. Style """
        output, violations = check_style("validISBN.py")
        self.assertEquals(violations, 0, output)

class Problem3(unittest.TestCase):

    def test1(self):
        """ Problem 3. Correctness """
        
        command = "python location.py 48.87 -2.33 37.8 -122.4"
        sought = """loc1 = (48.87, -2.33)
loc2 = (37.8, -122.4)
d(loc1, loc2) = 4703.45380716
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
  
    def test2(self):
        """ Problem 3. Correctness """

        command = "python location.py 46.36 -71.06 39.90 116.41"
        sought = """loc1 = (46.36, -71.06)
loc2 = (39.9, 116.41)
d(loc1, loc2) = 5608.92236459
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
        
    def test3(self):
        """ Problem 3. Style """

        output, violations = check_style("location.py")
        self.assertEquals(violations, 0, output)

class Problem4(unittest.TestCase):

    def test1(self):
        """ Problem 4. Correctness """

        command = "python point.py 0 1 1 0"
        sought = """p1 = (0.0, 1.0)
p2 = (1.0, 0.0)
d(p1, p2) = 1.41421356237
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

    def test2(self):
        """ Problem 4. Correctness """

        command = "python point.py 1 1 -1 -1"
        sought = """p1 = (1.0, 1.0)
p2 = (-1.0, -1.0)
d(p1, p2) = 2.82842712475
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

    def test3(self):
        """ Problem 4. Style """

        output, violations = check_style("point.py")
        self.assertEquals(violations, 0, output)

class Problem5(unittest.TestCase):

    def test1(self):
        """ Problem 5. Correctness """

        command = "python interval.py 3.14"
        sought = """[2.5, 3.5] contains 3.140000
[3.0, 4.0] contains 3.140000
[0.0, 1.0] intersects [0.5, 1.5]
[0.0, 1.0] intersects [1.0, 2.0]
[0.5, 1.5] intersects [1.0, 2.0]
[0.5, 1.5] intersects [1.5, 2.5]
[1.0, 2.0] intersects [1.5, 2.5]
[1.5, 2.5] intersects [2.5, 3.5]
[2.5, 3.5] intersects [3.0, 4.0]
"""
        got = run(command, "0 1 0.5 1.5 1 2 1.5 2.5 2.5 3.5 3 4")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

    def test2(self):
        """ Problem 5. Correctness """

        command = "python interval.py 1.41"
        sought = """[0.9, 1.5] contains 1.410000
[1.2, 1.8] contains 1.410000
[0.0, 0.6] intersects [0.3, 0.9]
[0.0, 0.6] intersects [0.6, 1.2]
[0.3, 0.9] intersects [0.6, 1.2]
[0.3, 0.9] intersects [0.9, 1.5]
[0.6, 1.2] intersects [0.9, 1.5]
[0.6, 1.2] intersects [1.2, 1.8]
[0.9, 1.5] intersects [1.2, 1.8]
[0.9, 1.5] intersects [1.5, 2.1]
[1.2, 1.8] intersects [1.5, 2.1]
"""
        got = run(command, "0 0.6 0.3 0.9 0.6 1.2 0.9 1.5 1.2 1.8 1.5 2.1")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

    def test3(self):
        """ Problem 5. Style """

        output, violations = check_style("interval.py")
        self.assertEquals(violations, 0, output)

class Problem6(unittest.TestCase):

    def test1(self):
        """ Problem 6. Correctness """

        command = "python rectangle.py 1.01 1.34"
        sought = """Area([0.0, 1.0] x [0.0, 1.0]) = 1.000000
Perimeter([0.0, 1.0] x [0.0, 1.0]) = 4.000000
Area([0.7, 1.2] x [0.9, 1.5]) = 0.300000
Perimeter([0.7, 1.2] x [0.9, 1.5]) = 2.200000
[0.7, 1.2] x [0.9, 1.5] contains (1.010000, 1.340000)
[0.0, 1.0] x [0.0, 1.0] intersects [0.7, 1.2] x [0.9, 1.5]
"""
        got = run(command, "0 1 0 1 0.7 1.2 .9 1.5")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

    def test2(self):
        """ Problem 6. Correctness """

        command = "python rectangle.py 1.41 3.14"
        sought = """Area([-1.0, 1.0] x [-1.0, 1.0]) = 4.000000
Perimeter([-1.0, 1.0] x [-1.0, 1.0]) = 8.000000
Area([0.0, 4.0] x [0.0, 4.0]) = 16.000000
Perimeter([0.0, 4.0] x [0.0, 4.0]) = 16.000000
[0.0, 4.0] x [0.0, 4.0] contains (1.410000, 3.140000)
[-1.0, 1.0] x [-1.0, 1.0] intersects [0.0, 4.0] x [0.0, 4.0]
"""
        got = run(command, "-1 1 -1 1 0 4 0 4")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
        
    def test3(self):
        """ Problem 6. Style """
        
        output, violations = check_style("rectangle.py")
        self.assertEquals(violations, 0, output)

class Problem7(unittest.TestCase):

    def test1(self):
        """ Problem 7. Correctness """
        command = "python rational.py 100"
        sought = """3.13159290356
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
        
    def test2(self):
        """ Problem 7. Correctness) """
        command = "python rational.py 50"
        sought = """3.12159465259
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
        
    def test3(self):
        """ Problem 7. Style """

        output, violations = check_style("rational.py")
        self.assertEquals(violations, 0, output)
        
class Problem8(unittest.TestCase):

    def test1(self):
        """ Problem 8. Correctness """
        command = "python threesum.py 13"
        sought = """ 30 -30   0
 30 -20 -10
-30 -10  40
-10   0  10

  0  10   5
"""
        got = run(command, "30 -30 -20 -10 40 0 10 5")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

    def test2(self):
        """ Problem 8. Correctness """
        command = "python threesum.py 2"
        sought = """ 30 -30   0
 30 -20 -10
-30 -10  40
-10   0  10

-10   0  10
"""
        got = run(command, "30 -30 -20 -10 40 0 10 5")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)

    def test3(self):
        """ Problem 8. Style """
        output, violations = check_style("threesum.py")
        self.assertEquals(violations, 0, output)
        
class Problem9(unittest.TestCase):

    def test1(self):
        """ Problem 9. Correctness """
        command = "python youngTableaux.py 5 5"
        sought = """False
"""
        got = run(command, "5 23 54 67 89 6 69 73 74 90 10 71 83 84 91 60 73 84 86 92 99 91 92 93 94")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
        
    def test2(self):
        """ Problem 9. Correctness """
        command = "python youngTableaux.py 5 5"
        sought = """True
"""
        got = run(command, "5 23 54 67 89 6 69 73 74 90 10 71 83 84 91 60 73 84 86 92 90 91 92 93 94")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
	
    def test3(self):
        """ Problem 9. Style """
        output, violations = check_style("youngTableaux.py")
        self.assertEquals(violations, 0, output)
 
class Problem10(unittest.TestCase):

    def test1(self):
        """ Problem 10. Correctness """
        command = "python binarySearch.py 3"
        sought = """2
"""
        got = run(command, "1 2 3 3 3 4 5 6")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
           
    def test2(self):
        """ Problem 10. Correctness """
        command = "python binarySearch.py 0"
        sought = """-1
"""
        got = run(command, "1 2 3 3 3 5 6 7")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
	
    def test4(self):
        """ Problem 10. Style """
        output, violations = check_style("binarySearch.py")
        self.assertEquals(violations, 0, output)
    
class Problem11(unittest.TestCase):

    def test1(self):
        """ Problem 11. Correctness """
        command = "python linkedList1.py 5"
        sought = """True
"""
        got = run(command, "1 3 2 4 5 7")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
        
    def test2(self):
        """ Problem 11. Correctness """
        command = "python linkedList1.py 8 "
        sought = """False
"""
        got = run(command, "1 3 2 4 5 7")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
        
    def test3(self):
        """ Problem 11. Style """
        output, violations = check_style("linkedList1.py")
        self.assertEquals(violations, 0, output)
        
class Problem12(unittest.TestCase):

    def test1(self):
        """ Problem 12. Correctness """
        command = "python linkedList2.py 3 "
        sought = """1 2 4 5 7 
"""
        got = run(command, "1 3 2 4 5 7")
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
        
    def test2(self):
        """ Problem 12. Style """
        output, violations = check_style("linkedList2.py")
        self.assertEquals(violations, 0, output)
        
class Problem13(unittest.TestCase):

    def test1(self):
        """ Problem 13. Correctness """
        command = "python deque.py 1 2 3 4 5 6"
        sought = """True
False
5 4 1 2 
"""
        got = run(command)
        self.assertNotEquals(got, "__TIMEOUT__")
        self.assertEquals(got, sought)
        
    def test2(self):
        """ Problem 13. Style """
        output, violations = check_style("deque.py")
        self.assertEquals(violations, 0, output)

if __name__ == "__main__":
    unittest.main()
