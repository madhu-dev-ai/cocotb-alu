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



@cocotb.test()
async def test_and(dut):
    dut.a.value = 12
    dut.b.value = 10
    dut.op.value = 2
    await Timer(1, unit="ns")
    assert dut.result.value == 8


@cocotb.test()
async def test_or(dut):
    dut.a.value = 12
    dut.b.value = 10
    dut.op.value = 3
    await Timer(1, unit="ns")
    assert dut.result.value == 14