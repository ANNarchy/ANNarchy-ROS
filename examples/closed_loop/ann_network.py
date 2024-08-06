"""
:copyright: Copyright 2024 - now, see AUTHORS.
:license: GPLv3, see LICENSE for details.
"""

from ANNarchy import *

turtle_control_neuron = Neuron(
    # read-out from ROS are the x- and y-coordinate
    parameters = """
    x = -1
    y = -1
    r = 0   # mandatory in ANNarchy
""",
    # simple control neuron: 
    #   if we hit a border, the turtle turns by some degree
    #   otherwise it always goes in a straight line.
    equations = """
    hit_border = (x < 0.75) or (x > 10.25) or (y < 0.75) or (y > 10.25)
    resp_1 = if (hit_border): 0.5 else: 1.0
    resp_2 = if (hit_border): 1.4 else: 0.0
"""
)

def create_network() -> Network:
    """
    We create an ANNarchy Population object. For easier handling, the whole network
    is encapsulated in a *Network* object.
    """
    pop = Population(1, neuron = turtle_control_neuron, name = "turtle_control")

    net = Network(everything=True)

    net.compile()

    return net
