import argparse
from opcodify.contract_ops import load_opcodes,get_opcodes,generate_opcodes_list,get_opcodes_frequency
from opcodify.visualiser import generate_treemap

def main():
    """
    Main function that processes command line arguments and generates the treemap.
    """
    parser = argparse.ArgumentParser(description="Opcode Treemap Visualizer")
    parser.add_argument("-c", "--contract", help="the contract to visualise")
    args = parser.parse_args()
    contract_file_path = args.contract
    opcodes = load_opcodes("./data/opcodes.json")
    input_opcodes = get_opcodes(contract_file_path)
    input_opcodes_list = generate_opcodes_list(input_opcodes)
    opcodes_frequency = dict.fromkeys(["arithmetic", "bitwise", "comparison", "keccak256", "environment", "blockInfo", "storage", "memory", "controlFlow", "stack", "duplication", "exchange", "logging", "system"], 0)
    opcodes_frequency = get_opcodes_frequency(opcodes_frequency, opcodes, input_opcodes_list)
    generate_treemap(opcodes_frequency, contract_file_path)


if __name__ == "__main__":
    main()
