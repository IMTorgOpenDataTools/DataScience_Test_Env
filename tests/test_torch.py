#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import numpy as np
import torch




torch.set_printoptions(edgeitems=2)
torch.manual_seed(123)

def test_cuda_available():
    assert torch.cuda.is_available() == True


def test_device_count():
    torch.cuda.device_count() > 0


def test_device_summary():
    if device.type == 'cuda':
        
        print(torch.cuda.get_device_name(0))
        print('Device location:', torch.cuda.device(0))

        print('Memory usage:')
        #maximum GPU memory managed by the caching allocator in bytes (for given device)
        print('Maximum:', round(torch.cuda.max_memory_cached(device=None)/1024**3,1), 'GB')
        #allocated amount
        print('Allocated:', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
        #current GPU memory usage by tensors in bytes for a given device
        print('Cached:   ', round(torch.cuda.memory_reserved(0)/1024**3,1), 'GB')
    assert True == True