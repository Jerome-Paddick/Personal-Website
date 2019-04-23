import numpy as np

input_data = {"training inputs":[0.05, 0.10], "target output": [0.01, 0.99]}
input_data = [[[0.05, 0.10], [0.01, 0.99]]]  # , [[0.1, 0.05],[0.02, 0.98]]]


def create_initial_weights(length_of_input):
    array = np.array(np.array_split([x/((length_of_input**2)) for x in range(length_of_input**2)], length_of_input))
    return array/2, (array/2)+0.5


def sigmoid(np_input):
    """Returns list of sigmoid functions for input list"""
    return np.array([[1 / (1 + np.exp(-z)) for z in np_input]])



def run_network(input_data, cycles, b1= 0.35, b2 = 0.60, eta=0.5):
    input_arrays = [[[0.05, 0.10], [0.01, 0.99]]]
    input_arrays = []
    for x in input_data:
        x[0] = np.array(x[0])
        x[1] = np.array(x[1])
    cycles = cycles
    b1 = b1
    b2 = b2
    Eta = eta  # Learning rate

    I_weights, H_weights = create_initial_weights(len(input_data[0]))

    # I_weights = np.array([[0.15, 0.25], [0.20, 0.30]])
    # H_weights = np.array([[0.40, 0.50], [0.45, 0.55]])

    for x in range(cycles):
        for input_array in input_data:

            target = input_array[1]
            fwd_I = np.array([input_array[0]]).T

            # --> FORWARD PASS
            out_fwd_H = sigmoid((fwd_I * I_weights).sum(axis=0) + b1)
            out_fwd_O = sigmoid((out_fwd_H * H_weights).sum(axis=0) + b2)
            # <-- FORWARD PASS

            Delta_O = (-(target-out_fwd_O))*(out_fwd_O*(1-out_fwd_O))
            Delta_H = (-(target-out_fwd_H))*(out_fwd_H*(1-out_fwd_H))

            I_weights = I_weights - Eta * fwd_I*(Delta_O*H_weights).sum(axis=1)*out_fwd_H*(1-out_fwd_H)
            H_weights = H_weights - Eta * out_fwd_H * Delta_O

    # print("I_weights", I_weights)
    # print("H_weights", H_weights)
    return("Final Out:", out_fwd_O)


print(run_network(input_data, 1000))