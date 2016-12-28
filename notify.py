#!/usr/bin/env python

import subprocess
import re


fname = "/home/ansq/.wine/drive_c/Program Files (x86)/Grinding Gear Games/Path of Exile/logs/Client.txt"


def notify(title, body="", timeout=8000, icon=""):
    subprocess.call(["notify-send", "-t", str(timeout), "-i", icon, sanitize(title), sanitize(body)])
    subprocess.Popen(["play", "-q", "-v", "0.2", "alert.wav"])

def sanitize(x):
    return x.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    f = subprocess.Popen(["tail", "-F", fname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    regex = re.compile(".+?\[INFO Client .+?\] ((@|(?!.+?[^>] .+?:)).*?:.+)")

    while True:
        line = f.stdout.readline()
        match = regex.match(line)

        if match:
            chat = match.group(1)
            print chat

            if chat.startswith("@From"):
                notify("PoE Whisper", chat, 10000, "7F60_ClientIcon.0")


if __name__ == "__main__":
    main()
