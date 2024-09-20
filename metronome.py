import time
import pygame
import numpy as np

def p_func(n_beat, threshold_l = 16, threshold_h = 32):
    if n_beat <= threshold_l:
        p = 1
    elif n_beat > threshold_l and n_beat <= threshold_h:
        p = 1/2 * (1 + np.cos(np.pi * (n_beat - threshold_l) / (threshold_h - threshold_l + 1)))
    else:
        p = 0 
    return p


def interval_calc(bpm_i, bpm_f, p):
    c_start = 60 / bpm_i
    c_end = 60 / bpm_f
    c_i = p * c_start + (1 - p) * c_end
    return c_i


def metronome(bpm_i, bpm_f, max_beats = 48, threshold_l = 16, threshold_h = 32): # Max beats needs to be higher than threshold_h
      
    n_beats = 1

    # Initialize pygame and load sound
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("beep.wav")  # Load a short beep sound file
    
    print(f"Metronome started at {bpm_i} BPM and ends at {bpm_f}. Press cmd + C to stop.")

    while n_beats < max_beats:
        try:

            p = p_func(n_beats, threshold_l, threshold_h)
            interval = interval_calc(bpm_i, bpm_f, p)

            pygame.mixer.music.play()  # Play the beep sound
            time.sleep(interval)  # Wait for the interval duration

            n_beats += 1


        except KeyboardInterrupt:
            print("\nMetronome stopped.")
            break

    pygame.quit()

