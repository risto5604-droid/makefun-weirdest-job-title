#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922.

The line is one job title, 60 characters or fewer and nothing else.
Judge: a deadpan comedy scout picking the weirdest, funniest title in
blind 2v2 rounds. Lesson from pelajaran.md: one concrete scene plus a
specific twist beats a generic oddity — so this is a real-sounding job
(professional mourner) with one hilariously specific client (retired
office printers), not a vague "weird job".
"""
import os

LINE = "Professional Mourner for Retired Office Printers"

# Gate: the entry must be a single job title of at most 60 characters,
# plain ASCII text, nothing else — the bounty takes the title exactly as
# written. Any non-ASCII byte means the text was corrupted in editing and
# the sandbox run must fail loudly.
assert 1 <= len(LINE) <= 60 and LINE.strip() and LINE.isascii(), "entry line violates the <=60 character gate"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: confirm the file on disk is byte-for-byte
    # the entry line (no newline, no trailing whitespace, no corruption).
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, (
        f"read-back mismatch: /output/entry.txt contains {written!r}, "
        f"expected {LINE!r}"
    )

if __name__ == "__main__":
    main()
