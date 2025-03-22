""""""

import os
import sys

import bpy

WINGHOME = R"C:\Program Files\Wing Pro 10"
os.environ["WINGHOME"] = WINGHOME

if WINGHOME not in sys.path:
    sys.path.append(WINGHOME)

wingdbstub = __import__("wingdbstub")
wingdbstub.Ensure()

bpy.ops.celestine.begin('INVOKE_DEFAULT')
