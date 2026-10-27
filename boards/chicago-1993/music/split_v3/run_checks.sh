#!/bin/bash
cd /workspace/moodboard/musicsync
for L in 0 1 2; do (.venv/bin/python check_render.py /workspace/moodboard/chicago-1993/edits/music_split_v3_lead$L.mp4 /workspace/moodboard/chicago-1993/edits/v3/sync/cutlist.json /workspace/moodboard/chicago-1993/edits/music/v3/music_edit_v3.wav --lead $L --splices /workspace/moodboard/chicago-1993/edits/v3/sync/splices.json --panels 0:952,968:1920 --out /workspace/moodboard/chicago-1993/edits/v3/check_lead$L.json 2>&1 | grep -v -i warn > /workspace/moodboard/chicago-1993/edits/v3/check_lead$L.txt) & done; wait; echo ALLDONE
