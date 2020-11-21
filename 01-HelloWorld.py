from migen import Module

from fpga_platform import build_platform


class Hello(Module):
    """
    Hello world module: light up LED[i] and LED[6-i] when BUTTON[i] is pressed
    """
    def __init__(self, plat):
        self.platform = plat
        self.ios = set()
        N = 7

        leds = [plat.request("user_led", i) for i in range(N)]
        btns = [plat.request("user_button", i) for i in range(N)]

        for i in range(N):
            self.comb += leds[i].eq(btns[i] | btns[N-1-i])
            self.ios |= {leds[i], btns[i]}


if __name__ == "__main__":
    plat = build_platform()
    plat.build(Hello(plat))
