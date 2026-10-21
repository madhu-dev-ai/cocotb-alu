import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_add(dut):
    dut.a.value = 5
    dut.b.value = 3
    dut.op.value = 0
    await Timer(1, unit="ns")
    assert dut.result.value == 8


@cocotb.test()
async def test_subtract(dut):
    dut.a.value = 9
    dut.b.value = 4
    dut.op.value = 1
    await Timer(1, unit="ns")
    assert dut.result.value == 5