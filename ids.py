import idaapi
import idc
import os
import sys

out = os.getenv('IDSOUT')
if out:
    sys.stdout = sys.stderr = open(out, 'w')
    sys.argv = idc.ARGV
    sys.exit = idc.Exit

    if os.getenv('IDSWAIT'):
        idaapi.autoWait()
