import os
import shutil

# Copy the bundled summary to the output path the task requires.
here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "summary.txt")
os.makedirs("/output", exist_ok=True)
shutil.copyfile(src, "/output/entry.txt")
