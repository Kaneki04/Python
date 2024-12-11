from pydub import AudioSegment
import os


def convert(input_file, output_file, type):
    

    if type == "0":
        audio = AudioSegment.from_file(input_file, format="webm")
    else:
        audio = AudioSegment.from_file(input_file, format="m4a")

    audio.export(output_file, format="mp3")
    print("**********************************************")
    print(f"Converted '{input_file}' to '{output_file}'")
    print("**********************************************\n")


def convert_all_files(inputDir, outputDir):
    for filename in os.listdir(inputDir):
        input_file = os.path.join(inputDir, filename)
        output_file = os.path.join(outputDir, f"{os.path.splitext(filename)[0]}.mp3")
        if filename.endswith(".webm"):
            convert(input_file, output_file, "0")

        else:
            convert(input_file, output_file, "1")


input_directory = "C:\\Users\\vicke\\Downloads\\SpotiMusic\\"
output_directory = "C:\\Users\\vicke\\Downloads\\ConvertedMusic\\"

convert_all_files(input_directory, output_directory)
