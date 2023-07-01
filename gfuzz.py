#!/bin/python3
import argparse
import os.path
import subprocess

FUZZ_KEYWORD = "FUZZ"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--wordlist", type=str, required=True, help="Path to a wordlist to fuzz with")
    parser.add_argument("-q", "--quiet", action="store_true", default=False)
    parser.add_argument("command", nargs="*")
    args = parser.parse_args()
    return args.wordlist, args.quiet, " ".join(args.command)


def validate_args(wordlist, command):
    assert FUZZ_KEYWORD in command, "No FUZZ keyword found to replace with wordlist tokens"
    assert os.path.exists(wordlist) and os.path.isfile(wordlist), "Wordlist must be an existing file"


def main():
    wordlist, quiet, command = parse_args()
    validate_args(wordlist, command)

    with open(wordlist) as words_file_object:
        for word in words_file_object.read().splitlines():
            cmd = command.replace(FUZZ_KEYWORD, word)
            if not quiet:
                print(cmd, end=" ")
            ret_val = os.system(cmd)
            print("[" + str(ret_val) + "]\n" if not quiet else "", end="")


if __name__ == '__main__':
    main()
