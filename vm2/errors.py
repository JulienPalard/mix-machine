# error codes of interface:
ERR_INVALID_ARGS = (1, "Invalid command line arguments, required one real filename")
ERR_INVALID_INPUT_FILE = (2, "Can't open input file")

class VMError(Exception):
  def __init__(self, info = None):
    self.info = info

  def __str__(self):
    if self.__doc__ is not None:
      try:
        return self.__doc__ % self.info
      except:
        return self.__doc__
    else:
      return str(self.info)

  def __cmp__(self, another):
    return cmp(self.__str__(), another.__str__())

class InvalidStartAddressError(VMError):
  """Invalid start address in input file (%s)"""