import metronome as mt
import time

low = 80
mid = 120
high = 160

max_beats = 72
threshold_l = 24
threshold_h = 48

# 3x3 bpm matrix
bpm = [[(low, low), (low, mid), (low, high)],
       [(mid, low), (mid, mid), (mid, high)],
       [(high, low), (high, mid), (high, high)]]
# set diag = 0
for i in range(3):
    bpm[i][i] = (0, 0)


mt.metronome(*bpm[2][0], max_beats, threshold_l, threshold_h)
