# MCU Build GitHub Action
## Usage

```yaml
uses: Arm-Debug/mcu-build-action@v1.0
with:
    # Product to be build e.g. buildmgr
    # Required arg
    # Default: ''
    target: ''

    # Build Type e.g. Release, Debug
    # Optional arg
    # Default: 'Release'
    build_target: ''

    # Build generator e.g. Ninja'
    # Optional arg
    # Default: 'Ninja'
    generator: ''
```

## Example
```yaml
- name: Build libdsq
  uses: Arm-Debug/mcu-build-action@main
  id: mcu-build
  with:
    target: dsq
```
