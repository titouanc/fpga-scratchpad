from litex.build.generic_platform import IOStandard, Pins
from litex.boards.platforms.ulx3s import Platform


def build_platform():
    # by default, LiteX uses Lattice's closed-source toolchain.
    # ULX3S has 4 FPGA size variants, set 'device' accordingly
    plat = Platform(toolchain="trellis", device="LFE5U-12F")

    # these IOs should probably be defined by default in litex, but since it's not we have to do it
    plat.add_extension([
        ("user_button", 0, Pins("D6"),  IOStandard("LVCMOS33")), # BTN_PWRn (inverted logic)
        ("user_button", 1, Pins("R1"),  IOStandard("LVCMOS33")), # FIRE1
        ("user_button", 2, Pins("T1"),  IOStandard("LVCMOS33")), # FIRE2
        ("user_button", 3, Pins("R18"), IOStandard("LVCMOS33")), # UP
        ("user_button", 4, Pins("V1"),  IOStandard("LVCMOS33")), # DOWN
        ("user_button", 5, Pins("U1"),  IOStandard("LVCMOS33")), # LEFT
        ("user_button", 6, Pins("H16"), IOStandard("LVCMOS33")), # RIGHT
    ])
    return plat
