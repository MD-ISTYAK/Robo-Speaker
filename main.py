#This Robo Speaker works on window  and win32com is from PyWin32 Python Package
import win32com.client as wincom
#selecting voice
speak= wincom.Dispatch("SAPI.SpVoice")
print("Robo Speaker 1.1 Created By MD ISTYAK")

speak.Speak("Hello, I am Ricco")
while True:
    text=input("Enter the text you want to Speak : ")
    if text=="q":
        speak.Speak("OK, BYE, BYE")
        break
    speak.Speak(text)

