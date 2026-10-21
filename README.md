# cocotb ALU

A 4-bit ALU (add and subtract) verified with cocotb and Icarus Verilog.

## Files
- alu.v: the Verilog design (op = 0 adds, op = 1 subtracts)
- test_alu.py: cocotb tests (5 + 3 = 8, 9 - 4 = 5)
- Makefile: runs the simulation

## How to run
make

## Result
TESTS=2 PASS=2 FAIL=0

I also changed the adder to a subtractor on purpose and the test failed, which shows the test really checks the result.