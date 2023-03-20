import os

os.chdir('/Users/airforce4593/LearningPython/Learning Python/SolarSystemFiles')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    
    f_course, f_title = (file_name.split('-'))

    f_course = f_course[1:].zfill(2)
    
    new_name = f'{f_course}-{f_title}{file_ext}'
    print(new_name)
    os.rename(f,new_name)