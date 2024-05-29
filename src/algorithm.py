# This could by your algorithm code; you can use any programming language you like, the blueprint
# uses Python as an example. Make sure that your Dockerfile declares installation of all necessary
# dependencies for your algorithm code. 
import json
import os
import uuid
import os
import os

# The input and output directories are fixed
input_dir = "/data/input" # read-only directory with level-0 data files
output_dir = "/data/output" # directory where your algorithm should save the output JSON file(s)


print("Hello, this is the SYLVA Algorithm Blueprint!")
print()
print("This is my environment: ")
print(f"\tInput directory: {input_dir} (holds {len(os.listdir(input_dir))} files)")
print(f"\tOutput directory: {output_dir}")
print()
print("I will now generate an example JSON file and save it to the output directory.")

# Create the example JSON; you may want to add your algorithm here
example_json = {
    "start": 1638400000,
    "end": 1638486400,
    "device": {"id": "SYLVA_DEVICE_CODE", "serial_number": "DEVICE_SERIAL_NUMBER"},
    "pollen": [
        {"name": "Alnus", "concentration": 5.9, "uncertainty": 0.89},
        {"name": "Birch", "concentration": 10.5, "uncertainty": 0.75},
    ],
}

# the ouput file names do not matter; only file content is relevant
filename = str(uuid.uuid4()) + ".json"

# create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# save JSON to the output folder; you can save as many files as you want, one for each device and time frame
output_path = os.path.join(output_dir, filename)
with open(output_path, "w") as file:
    json.dump(example_json, file, indent=4)

print(f"Example JSON saved to: {output_path}")
