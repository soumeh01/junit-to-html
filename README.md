# MCU Build GitHub Action
## Usage

```yaml
uses: Arm-Debug/mcu-build-action@v1.1
with:
    # Build Type e.g. Release, Debug
    # Optional arg
    # Default: 'Release'
    build_target: ''

    # cross-compile target to linux aarch64
    # Optional arg
    # Default: 'false'
    cross_compile_linux_aarch64: ''

    # Build generator e.g. Ninja'
    # Optional arg
    # Default: 'Ninja'
    generator: ''

    # Product to be build e.g. buildmgr
    # Required arg
    # Default: ''
    target: ''

```

## Example
```yaml
- name: Build libdsq
  uses: Arm-Debug/mcu-build-action@v1.0
  id: mcu-build
  with:
    target: dsq
```
