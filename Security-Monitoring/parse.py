#!/usr/bin/env python

def parse():
    with open("alerts.log") as alerts:
        for line in alerts:
            print(line)

if __name__ == "__main__":
    parse()
