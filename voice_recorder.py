import sounddevice as sd
import wavio
import numpy as np
import time
import threading

# Parameters
fs = 44100  # Sample rate in Hz
filename = "output.wav"  # Output filename
channels = 2  # Number of audio channels (2 for stereo)

# Global variables to manage recording state
recording = False  # Indicates if recording is active
paused = False  # Indicates if recording is paused
recorded_data = []  # List to store recorded audio chunks
recording_thread = None  # Thread to manage the recording process

def callback(indata, frames, time, status):
    """
    Callback function that gets called by sounddevice during recording.
    Appends recorded data to the list if recording is active and not paused.
    """
    if recording and not paused:
        recorded_data.append(indata.copy())

def record_audio():
    """
    Manages the audio recording process in a separate thread.
    """
    global recording
    with sd.InputStream(samplerate=fs, channels=channels, callback=callback):
        while recording:
            time.sleep(0.1)  # Check every 0.1 seconds to update recording state

def start_recording():
    """
    Starts the audio recording session.
    """
    global recording, paused, recorded_data, recording_thread
    if not recording:
        recording = True
        paused = False
        recorded_data = []
        print("Recording started...")
        recording_thread = threading.Thread(target=record_audio)
        recording_thread.start()
    else:
        print("Already recording.")

def pause_recording():
    """
    Pauses the audio recording session.
    """
    global paused
    if recording and not paused:
        paused = True
        print("Recording paused.")
    else:
        print("Cannot pause. Recording is either not active or already paused.")

def resume_recording():
    """
    Resumes the audio recording session if it was paused.
    """
    global paused
    if recording and paused:
        paused = False
        print("Recording resumed.")
    else:
        print("Cannot resume. Recording is either not active or not paused.")

def stop_recording():
    """
    Stops the audio recording session.
    """
    global recording
    if recording:
        recording = False
        if recording_thread:
            recording_thread.join()  # Wait for the recording thread to finish
        print("Recording stopped.")
    else:
        print("Cannot stop. Recording is not active.")

def save_recording():
    """
    Saves the recorded audio to a WAV file.
    """
    global recorded_data
    if recorded_data:
        # Convert list of arrays to a single numpy array
        audio_data = np.concatenate(recorded_data, axis=0)
        # Save the audio data to a WAV file
        wavio.write(filename, audio_data, fs, sampwidth=2)
        print(f"Recording saved to {filename}")
    else:
        print("No audio data to save.")

# Main program loop
if __name__ == "__main__":
    while True:
        command = input("Enter command (start, pause, resume, stop, save, exit): ").strip().lower()
        
        if command == "start":
            start_recording()
        
        elif command == "pause":
            pause_recording()
        
        elif command == "resume":
            resume_recording()
        
        elif command == "stop":
            stop_recording()
            save_recording()
        
        elif command == "save":
            if not recording:
                save_recording()
            else:
                print("Cannot save while recording is active.")
        
        elif command == "exit":
            if recording:
                stop_recording()
                save_recording()
            print("Exiting program.")
            break
        
        else:
            print("Invalid command. Please enter one of the following: start, pause, resume, stop, save, exit.")
