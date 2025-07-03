This repository contains the updated ISMIR DeepSalience codebase for automatic music transcription, changes include preprocessing, updated Keras patch, replaced replicate.yaml with environment.yml file and pre-trained weight integration. Also updated main python file for MIDI file handling. The purpose of these udpates are for testing and benchmarking for AMT performance in research settings. 

 Prerequisites

Git (to clone this repo and your Keras fork)
Conda (version ≥ 4.8) for environment management
Python 3.8 (as specified in the environment)

git clone git@github.com:skum156/ismir-deepsalience.git

conda env create -f environment.yml
conda activate ismir-deepsalience
Create the conda environment and link it to environment.yml file. 

Replaced replicate.yaml with environment.yml. Not using certain dependencies

After creating conda environment navigate to envs folder and navigate to keras directory. Navigate to site packages and go to keras/engine/saving.py Replace this file with updated saving.py file given in this repository to fix keras patch. 

# First locate the real path:
python - <<'EOF'
import keras, os
print(os.path.join(os.path.dirname(keras.__file__), "engine", "saving.py"))
EOF

# Suppose it prints /…/site-packages/keras/engine/saving.py, then do:
cp updated_saving.py /…/site-packages/keras/engine/saving.py


Run Inference: 
python predict_on_audio.py \
  <path_to_audio_file> \
  <model_name> \
  <output_directory> \
  --weights <path_to_model_weights> \
  -f <inference_mode>

e.g python predict_on_audio.py /scratch/gilbreth/kumar809/projects/ismir2017-deepsalience/inputs/evaluation_mp3_1._0_40_70.mp3 melody1 /scratch/gilbreth/kumar809/projects/ismir2017-deepsalience/outputs -f singlef0







