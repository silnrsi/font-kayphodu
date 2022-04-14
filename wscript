#!/usr/bin/python3
# this is a smith configuration file

# override the default folders
# DOCDIR = ["documentation", "web"]

# set the font name and description
APPNAME = 'KayPhoDu'
FAMILY = APPNAME
DESC_SHORT = "Font for the Kayah Li script"

TESTDIR = ["tests", "../font-kayphodu-private/tests"]

# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/masters/' + FAMILY  + '-Regular.ufo')
# BUILDLABEL = 'beta1'

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

designspace('source/' + FAMILY + '.designspace',
    target = "${DS:FILENAME_BASE}.ttf",
    params = "--decomposeComponents --removeOverlap",
    woff = woff('web/${DS:FILENAME_BASE}.woff',
        metadata=f'../source/{FAMILY}-WOFF-metadata.xml',
        cmd='psfwoffit -m ${SRC[1]} --woff ${TGT} --woff2 ${TGT}2 ${SRC[0]}'
        ),
    pdf = fret(params='-oi')
)
