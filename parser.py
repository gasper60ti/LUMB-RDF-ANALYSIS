import os
from rdflib import Graph

# Function to combine OWL files
def combine_owl_files(input_directory, output_file):
    # Create an empty graph
    combined_graph = Graph()

    # Loop through all OWL files in the input directory
    for file_name in os.listdir(input_directory):
        if file_name.endswith(".owl"):
            file_path = os.path.join(input_directory, file_name)
            print(f"Loading {file_name}...")
            
            # Load each OWL file into a new graph
            graph = Graph()
            graph.parse(file_path, format="xml")  # OWL files are usually in RDF/XML format
            
            # Add the graph's triples to the combined graph
            combined_graph += graph

    # Serialize the combined graph to an OWL file
    combined_graph.serialize(destination=output_file, format="xml")
    print(f"Combined OWL file saved to {output_file}")

# Specify the directory containing the OWL files and the output file name
input_directory = "./OWL"
output_file = "combined.owl"

# Combine the OWL files
combine_owl_files(input_directory, output_file)
