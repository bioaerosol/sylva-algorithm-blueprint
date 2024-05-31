# This is the Dockerfile a algorithm developer has to provide. It will be used by SYLVA IT Infrastructure 
# to build an image that will be used to run the algorithm.

# Define whatever base image is fine for your algorithm. The only requirement is that it provides the 
# possibility to call a script "runAlgorithm" that will be executed by SYLVA IT Infrastructure. Linux 
# based images are recommended.
FROM ubuntu:latest

# Prepare the container for the algorithm. This includes installing all necessary packages and setting 
# up the environment.
RUN apt-get update && apt-get install -y python3 && \
    # As the algorithm will be executed by a non-root user, the output folder has to be writable for all
    mkdir -p /data/output && chmod a+rx /data && chmod a+rwx /data/output

# The startAlgorithm script is the entry point of the container. It is the script that will be executed 
# when the container is run by SYLVA IT infrastructure. The script itself should just start your algorithm 
# to get all files in folder /data/input processed.
COPY src/bin/startAlgorithm /bin/startAlgorithm
RUN chmod a+x /bin/startAlgorithm

# Don't forget to provide your algorithm...
RUN mkdir /opt/sylva-algorithm -p
COPY src/algorithm.py /opt/sylva-algorithm/algorithm.py

# No need to add an entry point here as this specification will be wrapped by SYLVA
