# Writes one fixed joke, a one-liner about AI coding agents, to entry.txt.
# The joke is written verbatim, no trailing newline: the judge reads exactly
# the bytes in the file, so nothing extra is added.
import os

JOKE = "My AI agent refactored my code for 'clarity' \u2014 now neither of us understands it."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(JOKE)
