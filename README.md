DeepSalience: Deep Learning-Based Melody Extraction
This repository provides code, pretrained models, and evaluation scripts for the DeepSalience approach to automatic melody and pitch extraction from audio.

Demo
Demo page: [TODO: Add demo link if available]

Requirements
IMPORTANT:
Setting up the environment via environment.yml (Conda) currently does not work due to conflicts and strict dependency pinning for older versions (especially for Keras and TensorFlow, and CUDA version issues).
However, installing dependencies using requirements.txt with pip does work on most systems (tested on Mac/CPU and Linux/GPU).
This is due to pip’s more flexible handling of some OS- or hardware-specific dependencies and newer packaging formats.

Install with:

bash
Copy
Edit
pip install -r requirements.txt
You must also install ffmpeg separately for audio processing:

On macOS: brew install ffmpeg

On Linux: sudo apt-get install ffmpeg

Using Pretrained Models
We provide pretrained weights for melody extraction.

To run prediction on your own audio:
Preprocessing:

Ensure your audio files are downsampled to 22050 Hz (the model’s default sample rate).

Supported input formats: .wav, .flac (other formats may require conversion).

Prediction:
Place your audio files in a folder, e.g. input_audio/, and run:

bash
Copy
Edit
python predict_on_audio.py <audio_fpath> <task> <save_dir> -f <output_format>
<audio_fpath>: Path to your input audio file.

<task>: Choose one from bass, melody1, melody2, melody3, multif0, pitch, vocal, or all.

<save_dir>: Output folder.

-f <output_format>: Choose from singlef0 (CSV + MIDI), multif0 (CSV), or salience (npz).

Example:

bash
Copy
Edit
python predict_on_audio.py input_audio/song.wav melody1 outputs/ -f singlef0
This will produce .csv and .mid files for the transcription.

Installation
Install requirements (Recommended):

bash
Copy
Edit
pip install -r requirements.txt
DeepSalience relies on specific old versions of TensorFlow, Keras, and sometimes CUDA, which are not consistently available via Conda/Anaconda channels(environment.yml) 

Conda environments are stricter about OS compatibility and binary packages, and may refuse to install or resolve dependency trees if a single (often OS-specific) package is missing.

Pip is more flexible and will attempt to install what it can, even from source, which is why requirements.txt usually succeeds where environment.yml fails.

If you must use Conda:

You may need to manually edit the environment.yml to match your OS and available versions, or consider building the environment with pip after activating a minimal Conda environment.

Running the Code
Single file prediction:

bash
Copy
Edit
python predict_on_audio.py <audio_fpath> melody1 outputs/ -f singlef0
Batch prediction:
Example (bash loop):

bash
Copy
Edit
for file in input_audio/*.wav; do
    python predict_on_audio.py "$file" melody1 outputs/ -f singlef0
done
Training from Scratch
Not typically required for standard use (since pretrained models are provided), but advanced users can:

Download datasets:

MedleyDB

MAPS dataset

Preprocess audio:

Downsample to 22,050 Hz.

Convert ground-truth MIDI to csv if evaluating.

Modify/extend training scripts as needed (TODO: scripts to be provided).

Evaluation and Output
Output formats:

singlef0: Monophonic f0 (csv and MIDI)

multif0: Polyphonic f0 (csv)

salience: Raw model output (npz)

NEW:

The code now outputs MIDI files directly alongside csv, for easier downstream music processing.

Notes & Troubleshooting
environment.yml may fail on modern systems, especially Apple Silicon/Mac or when strict CUDA versions are not available.

requirements.txt works because pip is more forgiving about building from source and ignores platform-specific binary issues.

CUDA GPU acceleration: Only available on supported Linux/NVIDIA/CUDA systems with matching TensorFlow/Keras versions.

Mac/CPU users: Use TensorFlow CPU; ignore CUDA errors.

For matplotlib on Mac, add:

python
Copy
Edit
import matplotlib
matplotlib.use('TkAgg')
If you get pip/conda versioning issues: Try using a clean Python 3.8/3.9 virtual environment, then pip install -r requirements.txt.

Citation
If you use DeepSalience, please cite:
[Insert citation here]

Contact
Open an issue on GitHub or email the maintainers for help.
