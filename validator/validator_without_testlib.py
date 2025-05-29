import sys
inp = sys.stdin.read()
assert inp[0] != ' ', 'input cannot starts with space'
assert inp[-2] != ' ', 'input cannot ends with space'
assert inp.count(' ') == 1, 'input must be seperated by one space'
for i in inp.strip(): assert i in ' 0123456789', 'input must be two integers'
N,n = map(int, inp.split())
assert N > 0, 'N must be positive integer'
assert N <= 10**2, 'N cannot be greater than 100'
assert n > 0, 'n must be positive integer'
assert n <= 10**18, 'N cannot be greater than 1e18'