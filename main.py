#! /usr/bin/env python

import sys
import pandas as pd


def main():
    """Reads a csv file with information on some kerbals and outputs the information to a json file and to console."""
    try:
        kerbals_csv = pd.read_csv("kerbals.csv")
    except FileNotFoundError:
        print("Kerbals csv file not found in current directory!")
        sys.exit(1)
    kerbals_csv.to_json("kerbals.json", orient="records")
    kerbals_json = open("kerbals.json")
    print(kerbals_json.read())
    return 0


if __name__ == '__main__':
    main()
