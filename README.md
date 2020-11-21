# Setup

```bash
# Programmer
git clone https://github.com/chmousset/f32c-tools
pushd f32c-tools/ujprog
mkdir build
cd build
cmake ..
make
popd

# Toolchain (see https://github.com/open-tool-forge/fpga-toolchain/releases)
wget https://github.com/open-tool-forge/fpga-toolchain/releases/download/nightly-20201112/fpga-toolchain-linux_x86_64-nightly-20201112.tar.xz
tar xf fpga-toolchain-linux_x86_64-nightly-20201112.tar.gz

# Python pkgs
python3 -mvenv ve3
source ve3/bin/activate
pip install -r requirements.txt
```


# Build environment

```bash
source ve3/bin/activate
export PATH=$(pwd)/fpga_toolchain/bin:$(pwd)/f32c-tools/ujprog/build/:$PATH
```


# Build && run

```bash
python hello.py
ujprog build/top.bit
```


# Handling the ULX3S FTDI tty with ujprog

Connect the board, and run `dmesg | tail`, observe the following lines:

```
[...] ftdi_sio 1-4.4.1:1.0: FTDI USB Serial Device converter detected
[...] usb 1-4.4.1: Detected FT-X
[...] usb 1-4.4.1: FTDI USB Serial Device converter now attached to ttyUSB0
```

Flash the FPGA with `ujprog`, run `dmesg | tail` again:

```
[...] ftdi_sio ttyUSB0: FTDI USB Serial Device converter now disconnected from ttyUSB0
[...] ftdi_sio 1-4.4.1:1.0: device disconnected
```

This is because ujprog uses another mode of the FTDI converter, which needs another driver. This driver claims the device, and the serial driver release it. ujprog does not seem to restore the correct drivers settings (or maybe it's just because it segfault after successfully flashing the fpga ?), so we do it by hand.

Find the USB device identifier: in the dmesg line `device disconnected`, we have here `1-4.4.1:1.0`, but **check this on your system everytime** !!!

Then, re-bind it to the serial driver:

```
sudo bash -c 'echo 1-4.4.1:1.0 > /sys/bus/usb/drivers/ftdi_sio/bind'
```
