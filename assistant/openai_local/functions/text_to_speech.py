from openai import OpenAI
from utils.date_time_handling import *
from utils.file_handling import *
from terminal.components.system_messages import *
from terminal.components.assistant_output import print_text_to_speech


def text_to_speech(prompt):
    try:
        client = OpenAI()
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=prompt,
        )

    except Exception as e:
        print(e)
        error_openai()
        return None


    response.stream_to_file(find_path_to_data_file("tts.mp3"))

    print_text_to_speech(find_path_to_data_file("tts.mp3"))
