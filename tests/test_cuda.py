#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import ctypes as c




def test_cuda():
    # Change here to play with alongside versions of runtime (and driver?)
    stdlibdir = '/usr/lib/x86_64-linux-gnu/'
    cudadrv = 'libcuda.so'
    cudart  = 'libcudart.so'

    cudrv = c.CDLL(cudadrv)
    curt  = c.CDLL(cudart)

    ver = c.c_int()
    if cudrv.cuDriverGetVersion(c.byref(ver)) == 0:
      print(f'Driver DriverGetVersion: {ver}')

    if curt.cudaDriverGetVersion(c.byref(ver)) == 0:
      print(f'RT DriverGetVersion: {ver}')

    if curt.cudaRuntimeGetVersion(c.byref(ver)) == 0:
      print(f'RT RuntimeGetVersion: {ver}')

    devcnt = c.c_int()
    if cudrv.cuDeviceGetCount(c.byref(devcnt)) == 0:
      print(f'Devices count: {devcnt}')

    if devcnt.value > 0:  
      for id in range(devcnt.value):
        handle = c.c_int()
        if cudrv.cuDeviceGet(c.POINTER(handle), id) == 0:
          devname = c.create_string_buffer(255)
          if cudrv.cuDeviceGetName(c.byref(devname), 255, handle) == 0:
            print(f' device #{id} is {devname.value}')

    assert devcnt > 0