# Clpy

A wrapper for python allowing it to be used like awk or sed.

## Usage

Pass a single python statement as the first argument to the command. Optionally
 text can be piped into the command or a file name can be passed as second
 argument. Contents of the file are stored in the `inp` variable.


## Examples

```sh
clpy '27 + 47'
# output: 74

echo "hello world" | clpy 'inp.split(" ")[0]'
# output: hello

printf "53,87,26,95,75\n65,77,17,67,92\n34,62,41,82,54\n50,74,22,74,34\n" > hello.csv
clpy '[x.split(",") for x in inp.split("\n")][1][2]' hello.csv
# output: 17
```
