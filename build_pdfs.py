import subprocess
from signal import CTRL_C_EVENT
import signal
import time

EN_DIST = "http://localhost:3000/astro_resume/en"
EN_TARGET = "./public/en.pdf"
PL_DIST = "http://localhost:3000/astro_resume/pl"
PL_TARGET = "./public/pl.pdf"
OPTS = "--print-media-type --no-outline"
dev = subprocess.Popen("npm run astro dev", shell=True, stdout=None)
print(dev.pid)
time.sleep(5)

if subprocess.Popen(f"wkhtmltopdf {OPTS} {EN_DIST} {EN_TARGET} ", shell=True, stdout=None).wait() or subprocess.Popen(f"wkhtmltopdf  {OPTS} {PL_DIST} {PL_TARGET}", shell=True, stdout=None).wait():
    print("PDF build failed")
    raise SystemExit(1)
print("PDF build successful!")
# kill node process
try:
    dev.send_signal(CTRL_C_EVENT)
    time.sleep(0.5)
    dev.communicate(b"y\n")
except KeyboardInterrupt:
    pass # ignoring ctrl+c
# this is hacky as all hell, but it lets me kill the dev server