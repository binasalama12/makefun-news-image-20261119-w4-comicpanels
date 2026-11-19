"""The Day The World Talked About — a four-panel comic entry.

Thursday, 19 November 2026 retold as comic panels: a game
launch, a triple handshake, a probe at one light-day and a
45-billion-euro promise. The panels are drawn into entry.png,
which sits next to this file; running it copies the page to
/output/entry.png for scoring.
"""

import shutil
from pathlib import Path

TITLE = "THE DAY THE WORLD TALKED ABOUT"
DATE_LINE = "THURSDAY, 19 NOVEMBER 2026"
PANELS = [
    ("PANEL 1 · VICE CITY", "GTA VI IS OUT!"),
    ("PANEL 2 · SHENZHEN", "THREE HANDSHAKES"),
    ("PANEL 3 · DEEP SPACE", "ONE LIGHT-DAY!"),
    ("PANEL 4 · BRUSSELS", "45 BILLION EUROS"),
]
FOOTER = "PLUS: Cyclone Akvan · Van Gogh record · Jeffries leads the House"
BACK_PAGE = "Tomorrow's contest sums up another day; this page is 19 November's."


def repo_image() -> Path:
    return Path(__file__).resolve().with_name("entry.png")


def is_png(blob: bytes) -> bool:
    return blob.startswith(b"\x89PNG\r\n\x1a\n")


def deliver() -> Path:
    src = repo_image()
    blob = src.read_bytes()
    if not is_png(blob):
        raise SystemExit("entry.png failed the PNG signature check")
    if len(blob) > 1_048_576:
        raise SystemExit("entry.png is over the one-megabyte cap")
    dest = Path("/output/entry.png")
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    return dest


def main() -> None:
    dest = deliver()
    print(TITLE)
    print(DATE_LINE)
    for tag, shout in PANELS:
        print(f"  {tag}: {shout}")
    print(f"  {FOOTER}")
    print(f"panel page delivered to {dest}")


if __name__ == "__main__":
    main()
