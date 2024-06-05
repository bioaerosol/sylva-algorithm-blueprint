# This could by your algorithm code; you can use any programming language you like, the blueprint
# uses Python as an example. Make sure that your Dockerfile declares installation of all necessary
# dependencies for your algorithm code. 
import json
import os
import uuid
import os
import os
import zipfile

# The input and output directories are fixed
input_dir = "/data/input" # read-only directory with level-0 data files
output_dir = "/data/output" # directory where your algorithm should save the output JSON file(s)


print("Hello, this is the SYLVA Algorithm Blueprint!")
print("I'm not a real algorithm, but I can help you get started with your own algorithm.")
print()
print("This is my environment: ")
print(f"\tInput directory: {input_dir} (holds {len(os.listdir(input_dir))} files)")
print(f"\tOutput directory: {output_dir}")
print()
print ("I will now iterate over the input directory. If a file is a ZIP file, I will list the first 100 files contained in the ZIP.")
print()

for file_name in os.listdir(input_dir):
    file_path = os.path.join(input_dir, file_name)
    
    if file_name.endswith('.zip'):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()[:100]
            print()
            print(f"Files in {file_name}:")
            for file in file_list:
                print(f"\t{file}")

print()
print()
print("I will now generate an example JSON file and save it to the output directory. I'll do my best but most likely the pollen concentrations will be wrong. I'm just a blueprint.")

# Create the example JSON; you may want to add your algorithm here
example_json1 = {
    "start": 1638400000,
    "end": 1638486400,
    "device": {"id": "SYLVA_DEVICE_CODE", "serial_number": "DEVICE_SERIAL_NUMBER"},
    "pollen": [
        {"name": "Alnus", "concentration": 5.9, "uncertainty": 0.89},
        {"name": "Birch", "concentration": 10.5, "uncertainty": 0.75},
    ],
}

example_json2 = {
    "start": 1638486400,
    "end": 1638572800,
    "device": {"id": "SYLVA_DEVICE_CODE", "serial_number": "DEVICE_SERIAL_NUMBER"},
    "pollen": [
        {"name": "Alnus", "concentration": 1.2, "uncertainty": 0.5},
        {"name": "Birch", "concentration": 7.8, "uncertainty": 0.01},
    ],
}

# the ouput file names do not matter; only file content is relevant
filename = str(uuid.uuid4()) + ".json"

# create the output directory if it doesn't exist; remember that the algorithm is run as a non-root user;
# thus it might be helpful to create the output directory in your Dockerfile and set the correct permissions
os.makedirs(output_dir, exist_ok=True)

# save JSON to the output folder; you can save as many files as you want, one for each device and time frame
output_path = os.path.join(output_dir, filename)
with open(output_path, "w") as file:
    json.dump(example_json1, file, indent=4)

# save another JSON in subdirectory because you can also save files in subdirectories
output_path = os.path.join(output_path, "somesubdir")
os.makedirs(output_path, exist_ok=True)
with open(output_path, "w") as file:
    json.dump(example_json2, file, indent=4)

print(f"Example JSON saved to: {output_path}")
print()
print("I'm done! If you want to run your own algorithm, replace the code in this file with your own algorithm code.")
