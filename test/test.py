# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.ui_in.value = 36
    dut.uio_in.value = 0 # addition
    await ClockCycles(dut.clk, 3)
    assert dut.uo_out.value == 36  # Example output, update based on your ALU logic

    dut.ui_in.value = 36
    dut.uio_in.value = 1 # subtraction
    await ClockCycles(dut.clk, 3)
    assert dut.uo_out.value == 0  # Example output, update based on your ALU logic

    dut.ui_in.value = 36
    dut.uio_in.value = 2 # and
    await ClockCycles(dut.clk, 3)
    assert dut.uo_out.value == 36  # Example output, update based on your ALU logic

    dut.ui_in.value = 36
    dut.uio_in.value = 3 # or
    await ClockCycles(dut.clk, 3)
    assert dut.uo_out.value == 36  # Example output, update based on your ALU logic

    dut.ui_in.value = 36
    dut.uio_in.value = 4 # xor
    await ClockCycles(dut.clk, 3)
    assert dut.uo_out.value == 0  # Example output, update based on your ALU logic

    dut.ui_in.value = 36
    dut.uio_in.value = 5 # not
    await ClockCycles(dut.clk, 3)
    assert dut.uo_out.value == ~36 & 0xFF  # Example output, update based on your ALU logic

    dut.ui_in.value = 36
    dut.uio_in.value = 6 # multiply
    await ClockCycles(dut.clk, 3)
    assert dut.uo_out.value == 36 * 2  # Example output, update based on your ALU logic

    dut.ui_in.value = 36
    dut.uio_in.value = 7 # divide
    await ClockCycles(dut.clk, 3)
    assert dut.uo_out.value == 36 // 2  # Example output, update based on your ALU logic
