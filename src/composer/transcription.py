from pathlib import Path
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH

def mp3toMIDI(audio_path: str, out_dir: str) -> list[str]:
  output = Path(out_dir)
  out.mkdir(exist_ok=True)

