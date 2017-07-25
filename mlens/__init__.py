"""ML-ENSEMBLE

:author: Sebastian Flennerhag
:copyright: 2017
:licence: MIT

ML-Ensemble, a Python library for memory efficient parallelized ensemble
learning.
"""
# Initialize configurations
import mlens.config
from mlens.config import check_cache

__version__ = "0.1.5.dev0"


__all__ = ['base',
           'ensemble',
           'externals',
           'metrics',
           'model_selection',
           'parallel',
           'preprocessing',
           'utils',
           'visualization']
