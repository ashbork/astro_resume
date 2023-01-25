import subprocess
import time

EN_DIST = "http://localhost:3000/astro_resume/en"
EN_TARGET = "./public/en.pdf"
PL_DIST = "http://localhost:3000/astro_resume/pl"
PL_TARGET = "./public/pl.pdf"
OPTS = "--print-media-type --no-outline"


if (
    subprocess.Popen(
        f"wkhtmltopdf {OPTS} {EN_DIST} {EN_TARGET} ", shell=True, stdout=None
    ).wait()
    or subprocess.Popen(
        f"wkhtmltopdf  {OPTS} {PL_DIST} {PL_TARGET}", shell=True, stdout=None
    ).wait()
):
    print("PDF build failed")
    raise SystemExit(1)
print("PDF build successful!")
