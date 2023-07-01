# GFuzz - Generic Fuzz

Just a fuzzer that fuzzes shell commands. Intended to provide
a usage similar to strace that I couldn't find in existing tools.

### Example Usage
```shell
> ./gfuzz.py -w ./wordlist echo FUZZ

a
b
c
```
