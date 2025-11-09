import os

# Go to test_folder
os.chdir('test_folder')

# List of files to create
files = [
    'photo1.jpg', 'photo2.png', 'vacation.gif',
    'report.pdf', 'notes.txt', 'resume.docx',
    'song.mp3', 'podcast.wav',
    'movie.mp4', 'video.mkv',
    'backup.zip', 'code.py', 'random.xyz'
]

# Create empty files
for filename in files:
    open(filename, 'w').close()
    print(f'✓ Created: {filename}')

print(f'\n Created {len(files)} test files!')