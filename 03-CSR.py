from migen import Module
from litex.soc.cores.uart import UARTWishboneBridge
from litex.soc.integration.export import get_csr_csv
from litex.soc.integration.soc_core import SoCCore
from litex.soc.interconnect.csr import AutoCSR, CSRStatus, CSRStorage

from fpga_platform import build_platform

SYS_CLK = int(25e6)


class Adder(Module, AutoCSR):
    def __init__(self):
        self.A = CSRStorage(32, name="A", reset=0)
        self.B = CSRStorage(32, name="B", reset=0)
        self.C = CSRStatus(32, name="C", reset=0)
        self.comb += self.C.status.eq(self.A.storage + self.B.storage)


class CSRDemo(SoCCore, AutoCSR):
    """
    CSR demonstrator: a cpu-less SoC with 2 input registers A and B, and one
    output register C = A+B
    """
    def __init__(self, platform):
        # Initialize SoC things
        SoCCore.__init__(self, platform, SYS_CLK,
            cpu_type=None,
            csr_data_width=32,
            with_uart=False,
            ident="csrdemo", ident_version=True,
            with_timer=False
        )

        # Create a Wishbone bus, bridged to the UART
        bridge = UARTWishboneBridge(platform.request("serial"), SYS_CLK, baudrate=115200)
        self.submodules.bridge = bridge
        self.add_wb_master(bridge.wishbone)

        # Then wire up the addition
        self.submodules.adder = Adder()
        self.add_csr("adder")


if __name__ == "__main__":
    plat = build_platform()

    top = CSRDemo(plat)
    top.finalize()

    plat.build(top)
    
    csv = get_csr_csv(top.csr.regions, top.constants)
    print(csv)
    with open("build/csr.csv", 'w') as out:
        out.write(csv)
