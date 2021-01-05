import librosa
import glob
from pydub import AudioSegment
import os

def voice_normalization(wav, normal_db):
    wav1 = AudioSegment.from_file(wav)

    # Peak Normalization
    max_db1 = wav1.max_dBFS
    if max_db1 > 0:
        wav1 -= abs(max_db1)
    if max_db1 < 0:
        wav1 += abs(max_db1)

    db1 = wav1.dBFS
    # Loudness Normalization
    dbplus = db1 - normal_db
    if dbplus < 0:
        wav1 += abs(dbplus)
    elif dbplus > 0:
        wav1 -= abs(dbplus)

    path, name = os.path.split(wav)
    os.makedirs('normalization wav', exist_ok=True)
    wav1.export('./normalization wav/'+name, format="wav")

def total_wav_time(path):
    """
    e.g :total_wav_time('./autovc-master/wavs/H*/*.wav')
    :param path: search similar file name
    :return:
    """
    wav_list = glob.glob(path)
    print(len(wav_list))
    total_duration = 0
    for wav in wav_list:
        time = librosa.get_duration(filename=wav)
        total_duration+=time
    print(total_duration)


if __name__ == '__main__':

    print('Done')
