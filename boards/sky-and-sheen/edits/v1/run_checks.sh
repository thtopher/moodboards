#!/bin/bash
# usage: run_checks.sh LEAD...
E=/workspace/moodboard/sky-and-sheen/edits
cd /workspace/moodboard/musicsync
for L in "$@"; do
  .venv/bin/python check_render.py $E/sky_sheen_full_v1_lead$L.mp4 $E/v1/sync/cutlist.json $E/song/song.wav --lead $L \
    --panels 0:952,968:1920 --override $E/v1/sync/override.json --out $E/v1/check_lead$L.json 2>&1 | grep -v -i warn > $E/v1/check_lead$L.txt
  tail -1 $E/v1/check_lead$L.txt
done
