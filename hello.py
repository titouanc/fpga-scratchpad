from migen import Module, Signal

from plat import build_platform


# class Hello(Module):
#     def __init__(self, plat):
#         self.platform = plat
#         self.ios = set()

#         leds = [plat.request("user_led", i) for i in range(7)]
#         btns = [plat.request("user_button", i) for i in range(7)]

#         for i in range(7):
#             self.comb += leds[i].eq(btns[i] | btns[6 - i])
#             self.ios |= {leds[i], btns[i]}


class Hello(Module):
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
    plat.build(Hello(plat))
