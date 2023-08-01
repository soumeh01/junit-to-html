# JUnit-to-HTML

This Github Action merge input test result JUnit files and generates a consolidated HTML output file.

## Configuration

The list of the notable options:

|Option|Default Value|Description|
|:-----|:-----:|:----------|
|`junit_files`|_no default_|Path to the directory containing [JUnit files](https://github.com/soumeh01/junit-to-html/tree/test#junit-file-namings-convention).|
|`output_file`|`"./test_report.html"`|Write out consolidated test results in the specified file in HTML format|

## Usage

### Output to specific output file

```yaml
- name: Generate HTML report
  uses: Open-CMSIS-Pack/junit-to-html@v1
  with:
    junit_files: testreports
    output_file: path/to/output/file/test_report.html
```

### Output to default output file (i.e. `./test_report.html`)

```yaml
- name: Generate HTML report
  uses: Open-CMSIS-Pack/junit-to-html@v1
  with:
    junit_files: testreports
```

## Limitations

### JUnit file namings convention

The JUnit files that needs to be merged should follow the naming conventions specified below.

```txt
[Name]report-[Configuration].xml
```

OR

```regex
.*report-.*[\.]xml
```

for e.g.

```txt
test_report-windows-amd64.xml
test_report-linux-arm64.xml
test_report-darwin-arm64.xml
```
