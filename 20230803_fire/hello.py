"""
Commands 

python hello.py  # Hello World!
python hello.py --name=David  # Hello David!
python hello.py --help  # Shows usage information.
"""

import fire

def hello(name="World"):
  """
  name: user's name, you can get it from user input
  """
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
