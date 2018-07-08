# This file defines  environmental variables used throughout the project.
# To modify environmental variables, run pt.env(). Maintain a local file with pt.env() calls to set the
# environment correctly. (or modify this file, if you want...)

env = dict()

## ROM Paths
env['ROMPath'] = ''

## search utils
env['compareBinPath'] = ''

## disassembly utils
env['dismProjPath'] = ''
# disassembled asm files go here
env['asmPath'] = ''
# the path for where *.inc files are found to contain external symbols for disassembled asm files
env['externsPath'] = ''
# dictionary of filename and tuple of addresses: (Ex: {"start":(0x8000000, 0x80002CC)}
env['asmFiles'] = None