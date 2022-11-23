from lib.audio import recognize_speech, segment_audio
from lib.GPT_3 import prompting
from os import path



filename = path.join(path.dirname(path.realpath(__file__)), "rec2.wav")

path = path.dirname(path.realpath(__file__)) + '/recordings/'
file = "rec2"


# segmenting and recoginizing audio
length = segment_audio(path, file)

print("recognizing...")
print('-' * 40)


with open('transcriptions/{}.txt'.format(file), 'w') as f:
    for i in range(length):
        f.write(recognize_speech(path+"clips/{}_chunk{}.wav".format(file, i)))
        f.write('\n')
    f.close()

print("speech recognized, transcribing...")
print('-' * 40)


with open('transcriptions/{}.txt'.format(file), 'r') as f:
    contents = f.readlines()
    f.close()
text = " ".join(contents)

print("transcription finished, summarizing...")
print('-' * 40)


prompt = "summarize the following: \n" + text
result = prompting(prompt)

with open('summaries/{}_summary.txt'.format(file), 'w') as f:
    f.write(result)
    f.close()

print("summarization successful!")
print('-' * 40)

print(result)
