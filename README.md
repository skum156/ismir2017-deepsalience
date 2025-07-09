ISMIR2017-DeepSalience
This repository contains the implementation and experiments related to DeepSalience, a deep learning model for multi-pitch and multi-instrument transcription, originally presented at ISMIR 2017.

Overview
DeepSalience performs simultaneous transcription of multiple pitches and instruments from audio input using advanced neural architectures. This repository hosts:

Core model and training scripts

Data preprocessing and augmentation pipelines

Evaluation and inference scripts

Support for SLakh dataset loading

Custom patches for compatibility with Keras and other dependencies

What’s New / Updates by Me
Improved preprocessing scripts for better data pipeline management

Refactored and updated transcription-related scripts (transcription.py, predict_on_audio.py)

Added slakh_loader repository integration to support SLakh dataset processing

Applied patches to Keras dependencies to ensure smooth compatibility and reproducibility

    - To make keras patch after creating conda environment navigate to site-packages/keras/engine/saving.py variations depend on        OS and replace file named saving.py with updated_saving.py file. 

Enhanced evaluation metrics and output handling

Cleaned up experiment scripts and datasets handling for easier use

Repository Structure
deepsalience/ — Core source code and model definitions

predict/ — Scripts and utilities for inference and prediction on audio inputs

outputs/ — Output files such as transcription results, evaluation metrics

envs — Environment setup files and necessary patches for dependencies

requirements.txt / environment.yml — Dependency listings for environment setup

Setup and Installation
Create and activate a Python environment (e.g., with Conda or venv)

Install dependencies:

bash
Copy
pip install -r requirements.txt
# or
conda env create -f environment.yml
conda activate deepsalience
Apply any necessary patches in the patches/ directory (if applicable).

Usage
Preprocessing: Run scripts in deepsalience/ to prepare training data.

Training: Use provided training scripts to train the DeepSalience model.

Prediction: Use predict/predict_on_audio.py to transcribe audio files.

Evaluation: Scripts to evaluate transcription quality on test sets.

Example command for prediction:

bash
Copy
python predict/predict_on_audio.py --input <audio_file> --output <result_path>




