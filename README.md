# ML-Piano-Project

## What is this project?

The user gives the system 2-5 short piano clips (MP3/WAV or MIDI)
It learns the statistical summary of the melodic motion of the rhythm, not the harmony itself. Based on this, it then generates two short melodies:
- Major version: Happy, and bright feel
- Minor version: ominous and melancholy

## Project Pipeline
### 1. Input
   - Upload clip files
### 2. Transcription
   - Converts clips to MIDI format
   - Tool used: music21 (https://www.music21.org/music21docs/about/what.html)
     
