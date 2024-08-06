"""
:copyright: Copyright 2024 - now, see AUTHORS.
:license: GPLv3, see LICENSE for details.
"""

import sys
import os

from .Mapping import ANNarchyROSMapping
from .Interface import ANNarchyROSInterface

# Version tag
__version__ = '0.1'
__release__ = '0.1.0'

print( 'ANNarchyROS ' + __version__ + ' (' + __release__ + ') on ' + sys.platform + ' (' + os.name + ').' )
