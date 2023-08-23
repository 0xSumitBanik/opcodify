import solcx
import json
import matplotlib.pyplot as plt
from solcx.exceptions import SolcError

def get_opcodes(file_path):
    """
    Compiles the Solidity contract file and retrieves opcode information.

    Parameters:
    file_path (str): Path to the Solidity contract file.

    Returns:
    dict: Dictionary containing opcode information.
    """
    try:
        opcodes = solcx.compile_files([file_path], output_values=["opcodes"])
        return opcodes
    except SolcError as e:
        print(f"Error: {e}")
        exit(1)


def load_opcodes(opcodes_data_file):
    """
    Loads opcode information from a JSON file.

    Parameters:
    opcodes_data_file (str): Path to the JSON file containing opcode information.

    Returns:
    dict: Dictionary containing opcode information.
    """
    with open(opcodes_data_file) as file:
        opcodes = json.load(file)
    return opcodes


def generate_opcodes_list(opcodes):
    """
    Generates a list of opcodes from the opcode information.

    Parameters:
    opcodes (dict): Dictionary containing opcode information.

    Returns:
    list: List of opcodes.
    """
    try:
        for v in opcodes.values():
            opcodes_list = v.get("opcodes").split()
        return opcodes_list

    except Exception as e:
        print(f"Error: {e}")
        exit(1)    


def get_opcodes_frequency(opcodes_frequency, opcodes, opcodes_list):
    """
    Calculates the frequency of each opcode category.

    Parameters:
    opcodes_frequency (dict): Dictionary to store opcode category frequency.
    opcodes (dict): Dictionary containing opcode information.
    opcodes_list (list): List of opcodes from the input contract.

    Returns:
    dict: Updated dictionary containing opcode category frequency.
    """
    for opcode in opcodes_list:
        for key, value in opcodes.items():
            if opcode in value:
                opcodes_frequency[key] += 1
    opcodes_frequency = {key: value for key, value in opcodes_frequency.items() if value != 0}
    return opcodes_frequency

