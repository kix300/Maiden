import speech_recognition as sr
import random
import time


def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("'recognizer' must be 'Recognizer' instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("'microphone' must be 'Microphone' instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {"success": True, "error": None, "transcription": None}

    try:
        response["transcription"] = recognizer.recognize_whisper(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unvailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"
    return response


if __name__ == "__main__":
    WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    word = random.choice(WORDS)

    instruction = (
        "Find the good word in these words:\n"
        "{words}\n"
        "You have {n} tries to guess which one.\n"
    ).format(words=", ".join(WORDS), n=NUM_GUESSES)

    print(instruction)
    time.sleep(3)
