from pathlib import Path
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH

def mp3toMIDI(audio_path: str, out_dir: str) -> list[str]:
  output = Path(out_dir)
  output.mkdir(exist_ok=True)

  predict(
    [audio_path],
    save_midi=True,
    save_model_outputs=False,     # skip raw model dumps 
        model_or_model_path=ICASSP_2022_MODEL_PATH,  # official pretrained model
        output_directory=str(output)     # where to write results
  )
