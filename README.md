## Usage

By default, the analysis results will be generated in a subdirectory named "output" of the command_line_version installation. To utilize this tool, execute the following command in the terminal: 

```
python ./main.py [-argument] [value]
```

### Arguments Specification

|          Args          |                             Description                               | Required / Optional |
|:----------------------:|:---------------------------------------------------------------------:|:-------------------:|
|     `-h`, `--help`     |                   show this help message and exit                     |      Optional       |
|   `-f`, `--filename`   |           Path of the amun log file that needs to be analyzed         |      Optional       |
|   `-r`, `--recursion`  |           Path of the directory storing multiple amun log files       |      Optional       |
|    `-o`, `--output`    | Directory in which to output any generated files, default is ./output |      Optional       |
> **Note:** The two arguments '-f' and '-r' cannot be used simultaneously. But one of the two must be specified.

