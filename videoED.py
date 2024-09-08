import os 
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip 
 
def get_desktop_path(): 
    return os.path.join(os.path.expanduser("~"), "Desktop") 
 
def get_full_path(file_name): 
    desktop_path = get_desktop_path() 
    return os.path.join(desktop_path, file_name) 
 
def crop_video(input_file, output_filename, start_time, end_time): 
    input_file = input_file + ".mp4" 
    output_filename = output_filename + ".mp4" 
    video_clip = VideoFileClip(input_file).subclip(start_time, end_time) 
    video_clip.write_videofile(output_filename, codec='libx264') 
 
def concatenate_videos(video1, video2, output_filename): 
    video1 = video1 + ".mp4" 
    video2 = video2 + ".mp4" 
    clip1 = VideoFileClip(video1) 
    clip2 = VideoFileClip(video2) 
    final_clip = concatenate_videoclips([clip1, clip2]) 
    output_filename = output_filename + ".mp4" 
    final_clip.write_videofile(output_filename, codec='libx264') 
 
def overlay_audio(video_file, audio_file, audio_start_time, audio_end_time, output_filename):     
    video_file = video_file + ".mp4" 
    audio_file = audio_file + ".mp3" 
    video_clip = VideoFileClip(video_file) 
    audio_clip = AudioFileClip(audio_file).subclip(audio_start_time, audio_end_time) 
 
    # Наложение аудио на видео 
    video_clip = video_clip.set_audio(audio_clip) 
 
    output_filename = output_filename + ".mp4" 
    video_clip.write_videofile(output_filename, codec='libx264') 
 
def crop_audio(input_audio, output_filename, start_time, end_time): 
    input_audio = input_audio + ".mp3" 
    output_filename = output_filename + ".mp3" 
    audio_clip = AudioFileClip(input_audio).subclip(start_time, end_time) 
    audio_clip.write_audiofile(output_filename, codec='mp3') 
 
def print_menu(): 
    print("Выберите действие:") 
    print("1. Обрезать видео") 
    print("2. Склеить два видео") 
    print("3. Наложить аудио на видео") 
    print("4. Обрезать аудио") 
    print("5. Выйти") 
 
def main(): 
    while True: 
        print_menu() 
        choice = input("Введите номер действия: ") 
 
        if choice == '1': 
            input_file = input("Введите имя видеофайла на рабочем столе: ") 
            output_filename = input("Введите название для нового видеофайла: ") 
            start_time = float(input("Введите начальное время (в секундах): ")) 
            end_time = float(input("Введите конечное время (в секундах): ")) 
            crop_video(input_file, output_filename, start_time, end_time) 
 
        elif choice == '2': 
            video1 = input("Введите имя первого видеофайла на рабочем столе: ") 
            video2 = input("Введите имя второго видеофайла на рабочем столе: ") 
            output_filename = input("Введите название для нового видеофайла: ") 
            concatenate_videos(video1, video2, output_filename) 
 
        elif choice == '3': 
            video_file = input("Введите имя видеофайла на рабочем столе: ") 
            audio_file = input("Введите имя аудиофайла на рабочем столе: ") 
            audio_start_time = float(input("Введите начальное время аудио (в секундах): ")) 
            audio_end_time = float(input("Введите конечное время аудио (в секундах): ")) 
            output_filename = input("Введите название для нового видеофайла: ") 
            overlay_audio(video_file, audio_file, audio_start_time, audio_end_time, output_filename) 
 
        elif choice == '4': 
            audio_file = input("Введите имя аудиофайла на рабочем столе: ") 
            output_filename = input("Введите название для нового аудиофайла: ") 
            start_time = float(input("Введите начальное время (в секундах): ")) 
            end_time = float(input("Введите конечное время (в секундах): ")) 
            crop_audio(audio_file, output_filename, start_time, end_time) 
 
        elif choice == '5': 
            print("Выход из программы.") 
            break 
 
        else: 
            print("Неверный ввод. Пожалуйста, введите число от 1 до 5.") 
 
if __name__ == "__main__": 
    main()