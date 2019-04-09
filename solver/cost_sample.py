from math import floor

def cost_function(*inputs):
    """Compute the cost corresponding to the inputs.
    :param inputs: array of parameters
	:return the cost value
    """
    return(floor((inputs[0] + inputs[1]) / inputs[2]))