# MCU Build GitHub Action
## Usage

```yaml
uses: Arm-Debug/mcu-build-action@v1.1
with:
    # Beside build linux x86, cross-compile aarch64 target
    # Optional arg
    # Default: 'false'
    also_linux_aarch64: ''

    # Build Type e.g. Release, Debug
    # Optional arg
    # Default: 'Release'
    build_target: ''

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
  uses: Arm-Debug/mcu-build-action@v1.1
  id: mcu-build
  with:
    target: dsq
```
