"""
Written by Eric Curl
The University of Alabama Feb. 2022
"""

# import libraries
import numpy as np
# pull functions from other script
from build_directories import check_if_exists
from build_directories import create_dir
from build_directories import transfer_data_from_hpf5
from build_directories import store_images

# CAMGIAN_DATASET_ROOT
# note: will need to change this data path to where the hpf5 set is located,
#       this is also where the converted data will be stored
data_path='/data/sets/camgian/'

### check for confliciting directories
check_if_exists(data_path) # comment out if directories already exist
### create new directories on local machine
create_dir(data_path) # comment out if directories already exist
### pull lidar data from hpf5 dataset
transfer_data_from_hpf5('hiResTrain.hdf5', data_path)
### pull camera data from hpf5 dataset
store_images('cameraTrain.hdf5', data_path)

