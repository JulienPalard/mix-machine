from helper import *

class ExecutionTestCase(unittest.TestCase):
  pass

suite = unittest.makeSuite(ExecutionTestCase, 'test')

if __name__ == "__main__":
  unittest.main()
