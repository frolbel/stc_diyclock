''' custom script for platformio '''

from os.path import join
from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()

#print "post_extra_script running..."
#print env.Dump()

# compiler and linker flags dont work very well in build_flags of platformio.ini - need to set them here
env.Append(
    CFLAGS = [
    "--disable-warning", 126,
    "--disable-warning", 59,
    "-DWITH_ALT_LED9",
    "-DWITHOUT_LEDTABLE_RELOC",
    "-DSHOW_TEMP_DATE_WEEKDAY",
    "-DSHOW_DIGIT_WEEKDAY"
    ],
    LINKFLAGS = [
        "--data-loc", 0x30
    ],
    STCGALCMD="/stcgal.py"
)

