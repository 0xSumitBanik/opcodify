import matplotlib.pyplot as plt
import squarify
import time
import seaborn as sns
import os

def generate_treemap(opcode_counts, contract_file_path):
    """
    Generates and displays a treemap of opcode distribution.

    Parameters:
    opcode_counts (dict): Dictionary containing opcode category frequency.
    contract_file_path (str): Path to the contract file being visualized.
    """
    # Extract category names and opcode counts
    categories = list(opcode_counts.keys())

    # Format the label string to include opcode count
    label_strings = [f"{category}\n({count})" for category, count in opcode_counts.items()]

    # Create a treemap
    plt.figure(figsize=(30, 30))
    squarify.plot(sizes=opcode_counts.values(), 
                label=label_strings, 
                alpha=0.8,
                color=sns.color_palette("dark", len(categories)),
                text_kwargs={'fontsize': 20,
                             'fontweight': 'semibold',
                             'color': 'white',
                             'mouseover': True})

    # Set title
    plt.title(f"Opcode Distribution: [{contract_file_path}] \n")

    # Display the treemap without axes
    plt.axis('off')
    plt.tight_layout(pad=3)
    filename = os.getcwd()+f"/treemap-{int(time.time())}.png"
    plt.savefig(filename)
