from migen import Module, Signal

from fpga_platform import build_platform


class BinaryClock(Module):
    """
    Show a binary clock at SYS_CLK/(2^22) on the 8 user leds
    """
    def __init__(self, plat):
        counter = Signal(30)
        self.sync += counter.eq(counter + 1)
        self.ios = set()
        for i in range(8):
            led = plat.request("user_led", i)
            self.comb += led.eq(counter[-1-i])
            self.ios.add(led)


if __name__ == "__main__":
    plat = build_platform()
    plat.build(BinaryClock(plat))
