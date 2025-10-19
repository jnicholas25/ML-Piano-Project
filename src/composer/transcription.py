from pathlib import Path
from basic_pitch.inference import predict   # imports function that runs transcription
from basic_pitch import ICASSP_2022_MODEL_PATH  # pretrained model path

def mp3toMIDI(audio_path: str, out_dir: str) -> list[str]:  # converts audio file to one or more MIDI paths
  output = Path(out_dir)
  output.mkdir(exist_ok=True)

  predict(
    [audio_path],   # list of audio files to process
    save_midi=True, #wite .mid to disk
    save_model_outputs=False,     # skip raw model dumps 
        model_or_model_path=ICASSP_2022_MODEL_PATH,  # official pretrained model
        output_directory=str(output)     # where to write results
  )

  stem = Path(audio_path).stem
  return [str(p) for p in output.glob(f"{stem}*_basic_pitch.mid")] 
