import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.utils import make_chunks
from dotenv import load_dotenv
import os


r = sr.Recognizer()

def get_key():
    return os.getenv('WIZ_API_KEY')


def segment_audio(path, file):
    '''
        segment the speech into 20s snippets
    '''
    read_path = path+'/original/'+file+'.wav'

    audio = AudioSegment.from_file(read_path, 'wav')
    chunk_length_ms = 10000 #ms
    #chunks = split_on_silence(audio, min_silence_len=400)
    chunks = make_chunks(audio, chunk_length_ms)
    for i, chunk in enumerate(chunks):
        chunk_name = path+"/clips/{}_chunk{}.wav".format(file, i)
        chunk.export(chunk_name, bitrate='256k', format="wav")

    return len(chunks)


def recognize_speech(filename):
    '''
        recognize a certain speech given a .wav file
    '''
    global api_key
    with sr.AudioFile(filename) as source:
        audio = r.record(source)  

    return r.recognize_wit(audio, get_key())


load_dotenv()

if __name__ == "__main__":
    r = sr.Recognizer()
    path = '../'
    file = 'rec2'
    length = segment_audio(path, file)
    for i in range(length):
        print(recognize_speech(path+"clips/{}_chunk{}.wav".format(file, i)))
    print('audio file ran')

