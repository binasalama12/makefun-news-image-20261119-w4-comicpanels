#!/usr/bin/env python3
"""The Day The World Talked About - a four-panel comic page, 19 Nov 2026."""
import shutil
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
PNG_PREFIX = b"\x89PNG\r\n\x1a\n"
ONE_MIB = 1024 * 1024

PANELS = (
    {
        "panel": "PANEL 1 - THE LAUNCH",
        "caption": "Midnight. A game thirteen years in the making.",
        "bubble": "GTA VI is out. The whole planet is playing.",
    },
    {
        "panel": "PANEL 2 - THE SUMMIT",
        "caption": "Shenzhen. Three leaders, one long table.",
        "bubble": "Trump, Xi and Putin - talking, at last, in person.",
    },
    {
        "panel": "PANEL 3 - THE STORM",
        "caption": "The Bay of Bengal darkens as Akvan rolls in.",
        "bubble": "Andhra and Odisha brace for landfall tonight.",
    },
    {
        "panel": "PANEL 4 - THE SIGNAL",
        "caption": "Far beyond the planets, a whisper keeps travelling.",
        "bubble": "Voyager 1 is now one light-day from home.",
    },
)


def panel_count() -> int:
    return len(PANELS)


def find_page():
    page = BASE / "entry.png"
    return page if page.is_file() else None


def check_page(page):
    blob = page.read_bytes()
    if not blob.startswith(PNG_PREFIX):
        return None, "not a PNG file"
    if len(blob) > ONE_MIB:
        return None, f"page too heavy: {len(blob)} bytes"
    return len(blob), ""


def deliver(page):
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.png"
    shutil.copyfile(page, out_file)
    return out_file


def narrate(size, out_file):
    print("THE DAY THE WORLD TALKED ABOUT - 19 November 2026")
    for entry in PANELS:
        print(f"{entry['panel']}")
        print(f"  caption : {entry['caption']}")
        print(f"  bubble  : \"{entry['bubble']}\"")
    print(f"Comic page checked ({size} bytes) and delivered to {out_file}")


def main():
    page = find_page()
    if page is None:
        print("no comic page found (entry.png missing)", file=sys.stderr)
        return 1
    size, problem = check_page(page)
    if problem:
        print(f"comic page rejected: {problem}", file=sys.stderr)
        return 1
    narrate(size, deliver(page))
    return 0


if __name__ == "__main__":
    sys.exit(main())
