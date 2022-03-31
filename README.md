# MCU Build GitHub Action
## Usage

```yaml
uses: Arm-Debug/mcu-build-action@v1.1
with:
    # Add additional CMake Build args. E.g.: `--config Release`
    # Optional arg
    # Default: ''
    add_cmake_build_args:

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

## Examples
```yaml
- name: Build libdsq
  uses: Arm-Debug/mcu-build-action@v1.1
  id: mcu-build
  with:
    target: dsq
```

```yaml
- name: Build swig libs windows
  if: ${{ startsWith(matrix.runs_on, 'windows') }}
  uses: Arm-Debug/mcu-build-action@v1.1
  with:
    add_cmake_variables: -DSWIG_LIBS=ON
    add_cmake_build_args: --config Release
    arch: amd64
    build_folder: buildswig
    target: projmgr-python
```
