#!/usr/bin/env bash
# Creates the two environments musicsync needs (idempotent).
#  .venv    : Python 3.13 + torch(cpu) + Beat This! + Demucs + librosa  (beats/moments/cutlist/check)
#  .venv-mm : Python 3.11 + madmom (needs numpy<2, so it lives in its own env; called as a subprocess)
set -euo pipefail
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
  uv venv -q -p 3.13 .venv
  VIRTUAL_ENV=$PWD/.venv uv pip install -q torch torchaudio --index-url https://download.pytorch.org/whl/cpu
  VIRTUAL_ENV=$PWD/.venv uv pip install -q "git+https://github.com/CPJKU/beat_this.git" demucs soundfile librosa scipy matplotlib
fi
if [ ! -x .venv-mm/bin/python ]; then
  uv venv -q -p 3.11 .venv-mm
  VIRTUAL_ENV=$PWD/.venv-mm uv pip install -q "numpy<2" cython setuptools wheel scipy mido
  VIRTUAL_ENV=$PWD/.venv-mm uv pip install -q --no-build-isolation "git+https://github.com/CPJKU/madmom.git"
fi
echo ok
