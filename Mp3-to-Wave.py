import os
import glob
# for filename in os.listdir('C:/Users/HP/Music/wavfile/recordings/recordings'):
#     s=filename[:-4]
#     path='C:/Users/HP/Music/wavfile/recordings/recordings/'+filename
#     fpath='C:/Users/HP/Music/test/'+s+'.wav'
#     res='ffmpeg -i '+path+' -ac 2 -ar 48000 '+fpath
#     print(res)
for filename in os.listdir('C:/Users/HP/Music/stereo_audio'):
    s=filename[:-4]
    path='C:/Users/HP/Music/stereo_audio/'+filename
    print(path)
    fpath='C:/Users/HP/Music/16k_48k/'+filename
    if (filename.endswith(".wav")): #or .avi, .mpeg, whatever.
        os.system("ffmpeg -i "+path+" -ac 2 -ar 48000 "+fpath)
        print('yues')