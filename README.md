# OpCodify

[![PyPI Version](https://img.shields.io/pypi/v/opcodify.svg)](https://pypi.org/project/opcodify/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

<!-- Will re-enable soon -->
<!-- [![Downloads](https://static.pepy.tech/badge/opcodify)](https://pepy.tech/project/opcodify) -->

opcodify is a command-line tool that helps visualize Opcodes for Solidity Smart Contracts. It generates a treemap visualization to provide insights into the distribution of Opcodes within a contract.

## Installation

You can install `opcodify` using pip:

```bash
pip install opcodify
```

## Usage

After installation, you can use the `opcodify` command to visualize Opcodes for a Solidity Smart Contract:

```bash
opcodify --contract Contract.sol
```

Replace `Contract.sol` with the path to your Solidity Smart Contract file.

You should see the opcode treemap getting created in the working directory.

The image below is an example of a Smart Contract:

![TreeMap](assets/treemap-1692811755.png)

## Prerequisites

- Python

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/0xSumitBanik/opcodify/issues) or submit a pull request.

