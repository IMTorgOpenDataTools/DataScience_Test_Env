#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"




def test_spacy_without_gpu():
    """Basic spacy installation."""
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("This is a test sentence.")
    assert len(doc) > 0


def test_spacy_with_gpu():
    """Run spacy with gpu.

    This uses the following for installation with CUDA 11.3:
    >>>> sudo apt install nvidia-cuda-toolkit
    >>>> /usr/local/cuda/bin/nvcc --version                     #gives the CUDA compiler version (which matches the toolkit version)
    >>>> pip install -U 'spacy[cuda113]'
    """
    import spacy
    spacy.require_gpu() 
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("This is a test sentence.")
    assert len(doc) > 0