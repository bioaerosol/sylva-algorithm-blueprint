# SYLVA Algorithm Blueprint
The SYLVA IT Infrastructure allows to run  recognition algorithms that read level-0 data and produce aeroallergen classifications. 

This is a blueprint for SYLVA algorithms. It shows how a algorithm must be packaged and how input and output contracts look like in order to run the algorithm in SYLVA IT Infrastructure. Although it does not containa real algorithm it has all parts and assets to actually run with level-0 data.

# Algorithm Packaging
An algorithm can be developed in any way as long as it runs in an OCI compliant (see https://opencontainers.org/) container. As a algorithm developer you need to define an image specification (Dockerfile), expect level-0 data in folder ```/data/input``` and write recognition output to ```/data/output```. Provisioning of level-0 data, creation of image and execution of container is orchestrated by SYLVA IT Infrastructure.

# Algorithm Input
The input are level-0 files from devices. Input files are provided automatically in ```/data/input```

_TODO Specifiy how one can define which data should be provided._


## Algorithm Output
The algorithm needs to write it output to files in folder ```/data/output``` by creating one file for each analysed time frame and device.

The following JSON schema is to be used:

- `start`: The date and time of the time frame start, including, epoch timestamp in seconds at UTC.
- `end`: The date and time of the time frame end, excluding, epoch timestamp in seconds at UTC.
- `device`: An object with device properties:
    - `id`: The SYLVA instrument name (as listed at https://sylva.atlassian.net/wiki/x/AYAzB)
    - `serialNumber` (optional): The serial number of the device.
- `pollen`: An array of pollen types, each represented by an object with the following properties. The key of each object is the latin pollen name in snake case; each word starting with capital letter.
    - `concentration`: The concentration of the pollen type in count per cubic meter.
    - `uncertainty`: The uncertainty of classification, ranging from 0 to 1.

Here's an example of the JSON structure:
```json
{
    "start": 1709294400,
    "end": 1709298000,
    "device": {
        "id": "FIHELS-JUPITER-1",
        "serial_number": "123"
    },
    "pollen": [
        {
            "name": "abies",
            "concentration": 5.9,
            "uncertainty": 0.89
        },
        {
            "name": "betula",
            "concentration": 15.9,
            "uncertainty": 0.99
        },
        {
            "name": "olive",
            "concentration": 13.9,
            "uncertainty": 0.4
        }
    ]
}
```

This structure is required to allow automatical testing of the algorithm's quality and for further data processing.
