# use argparse and operator to create a calculator with prefix notation

import argparse
import operator

op = {
    '+': operator.add,
    '-': operator.sub,
    'x': operator.mul,
    '/': operator.truediv,
    '_': operator.floordiv,
    '%': operator.mod,
    '^': operator.pow,
}

parser = argparse.ArgumentParser(description='arithmetic in prefix notation')
parser.add_argument('op', help='operator')
parser.add_argument('a', help='operand', type=float)
parser.add_argument('b', help='operand', type=float)

args = parser.parse_args()
print(op[args.op](args.a, args.b))
