import metronome as mt
import time

low = 80
mid = 130
high = 180

max_beats = 48
threshold_l = 16
threshold_h = 32

# 3x3 bpm matrix
bpm = [[(low, low), (low, mid), (low, high)],
       [(mid, low), (mid, mid), (mid, high)],
       [(high, low), (high, mid), (high, high)]]
# set diag = 0
for i in range(3):
    bpm[i][i] = (0, 0)



mt.metronome(*bpm[0][1], max_beats, threshold_l, threshold_h)
