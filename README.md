# MCU Build GitHub Action
## Usage

```yaml
uses: Arm-Debug/mcu-build-action@v1.1
with:
    # Add adicional CMake variables to the build. E.g. `-DLIBS_ONLY=ON`
    # Optional arg
    # Default: ''
    add_cmake_variables: ''

    # arch is either amd64 (default) or `aarch64`. If `aarch64` is cross-compiled from x86.
    # Optional arg
    # Default: 'amd64'
    arch: ''

    # Choose a build folder
    # Optional arg
    # Default: 'build'
    build_folder: ''

    # Build Type e.g. Release, Debug
    # Optional arg
    # Default: 'Release'
    build_type: ''

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
