"""
Python Fire 是一个库，用于自动从任何 Python 对象生成命令行接口 (CLIs)。

Python Fire 是在Python中创建 CLI 的简单方法。[1]
Python Fire 是开发和调试 Python 代码的有用工具。[2]
Python Fire 有助于探索现有的代码或将他人的代码转换为CLI。[3]
Python Fire 使在 Bash 和 Python 之间的转换变得更容易。[4]
Python Fire 通过设置REPL并已经导入和创建了您需要的模块和变量，使使用 Python REPL 变得更容易
"""


import fire

class Calculator(object):
  """A simple calculator class."""

  def double(self, number):
    """2 number"""
    return 2 * number

if __name__ == '__main__':
  fire.Fire(Calculator)