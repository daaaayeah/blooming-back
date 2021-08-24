import speech_recognition as sr


def _STT(file_path):
    r = sr.Recognizer()
    harvard = sr.AudioFile(file_path)
    with harvard as source:
        audio = r.record(source)
    return r.recognize_google(audio, language='ko-KR')