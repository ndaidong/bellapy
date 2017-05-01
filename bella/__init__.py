import string
import random
import hashlib

class Bella:
  def createId(leng = 16):
    allchars = ''.join([string.ascii_letters, string.digits])
    candidates = list(allchars)
    random.shuffle(candidates)

    minimum = 0
    maximum = len(candidates) - 1
    output = []
    while len(output) < leng:
      ranint = random.randint(minimum, maximum)
      char = candidates[ranint]
      output.append(char)
    return ''.join(output)
  def md5(txt = ''):
    if txt != '':
      m = hashlib.md5()
      m.update(txt.encode('utf-8'))
      return m.hexdigest()
    return ''


