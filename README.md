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
export PATH=$(pwd)/fpga_toolchain/bin:f32c-tools/ujprog/build/:$PATH
```

# Build && run

```bash
python hello.py
ujprog build/top.bit
```
