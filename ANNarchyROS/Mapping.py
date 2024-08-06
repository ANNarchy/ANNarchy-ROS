"""
:copyright: Copyright 2024 - now, see AUTHORS.
:license: GPLv3, see LICENSE for details.
"""

from dataclasses import dataclass

@dataclass
class ANNarchyROSMapping:
    # Unique identifier
    name : str

    # ROS topic
    topic_direction: str
    topic_name: str
    topic_msg_type: object

    # ANNarchy mapping
    population : "Population" = None
    mapping : dict = None

    # specific parameters
    callback_func: callable = None
    queue_size: int = 10
