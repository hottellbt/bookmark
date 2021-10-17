#!/usr/bin/python3

import argparse
import sys
import os

SCRIPT_NAME = "bookmark"

VERSION = "1.1.0"


def eprint(*args, **kwargs):
    print(f"{SCRIPT_NAME}:", *args, file=sys.stderr, **kwargs)


def normalize_path(path):
    return os.path.realpath(os.path.expanduser(path))


def open_r_file(file_path):
    if file_path is None:
        return sys.stdin
    else:
        file_path = normalize_path(file_path)
        if not os.path.isfile(file_path):
            eprint(f"not a file: {file_path}")
            return 1
        return open(file_path, 'r')


def main():
    argp = argparse.ArgumentParser(
        prog=SCRIPT_NAME)

    argp.add_argument(
        "--version",
        help="display version, then exit",
        action="store_true")

    argp.add_argument(
        "-b", "--bookmark",
        help="bookmark name to resolve, incompatible with -B",
        default=None)

    argp.add_argument(
        "-B", "--bookmark-stdin",
        help="read bookmark to resolve from stdin, incompatible with -b, -F",
        action="store_true")

    argp.add_argument(
        "-f", "--bookmark-file",
        help="file that holds your bookmarks, incompatible with -F",
        default=None)

    argp.add_argument(
        "-F", "--bookmark-file-stdin",
        help="read bookmark data from stdin, incompatible with -f, -B",
        action="store_true")

    argp.add_argument(
        "-l", "--list",
        help="list available bookmarks before reading from stdin",
        action="store_true")

    argp.add_argument(
        "--expand-paths",
        help="treat bookmark destinations as paths and fully resolve them",
        action="store_true")

    args = argp.parse_args()

    if args.version:
        print(VERSION)
        return 0

    if args.bookmark and args.bookmark_stdin:
        eprint("incompatible args: -b, -B")
        return 1

    if args.bookmark_file and args.bookmark_file_stdin:
        eprint("incompatible args: -f, -F")
        return 1

    if args.bookmark_stdin and args.bookmark_file_stdin:
        eprint("incompatible args: -B, -F")
        return 1

    if not args.bookmark_file_stdin and args.bookmark_file is None:
        eprint("Please use either -f or -F")
        return 1

    bookmarks = []

    # Read bookmarks file

    with open_r_file(args.bookmark_file) as f:
        line_num = 0

        for ln in f:
            line_num += 1

            ln = ln.strip()
            if len(ln) == 0 or ln[0] == '#':
                continue

            parsed_bookmark = ln.rsplit(maxsplit=1)

            if len(parsed_bookmark) != 2:
                eprint(f"syntax error on line {line_num}")
                continue

            # user option: expand paths

            if args.expand_paths:
                parsed_bookmark[1] = normalize_path(parsed_bookmark[1])

            bookmarks.append(parsed_bookmark)

    if args.list:
        for bookmark in bookmarks:
            print(bookmark[0])

    if args.bookmark_stdin:
        my_bookmark = input().strip()
    else:
        my_bookmark = args.bookmark

    if my_bookmark is not None:
        for bookmark in bookmarks:
            if bookmark[0] == my_bookmark:
                print(bookmark[1])
                return 0
        # not found
        return 1



if __name__ == "__main__":
    sys.exit(main())
