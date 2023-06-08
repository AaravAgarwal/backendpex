from fastapi import FastAPI
from pydantic import BaseModel
import serial

app = FastAPI()
serial_port = "motorORG"  
serial_port2 = "motorMIR"

ser = serial.Serial(serial_port, 115200, timeout=1)
ser2 = serial.Serial(serial_port2, 115200, timeout=1)

class SliderValue(BaseModel):
    value: int

class PlayPauseState(BaseModel):
    isPlaying: int

@app.post("/api/slider")
async def set_slider_value(slider_value: SliderValue):
    value = slider_value.value
    value = value * 50
    ser.write(str(value))
    ser2.write(str(value))

@app.post("/api/play-pause")
async def set_play_pause_state(play_pause_state: PlayPauseState):
    is_playing = play_pause_state.isPlaying

    command = 1 if is_playing else 0
    ser.write(str(command))
    ser2.write(str(command))
