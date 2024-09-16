from setuptools import setup, find_packages

# Reading in the requirements from the requirements.txt
with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="video-downloader-transcriber",
    version="1.0",
    description="A tool to download videos, extract audio, and transcribe using faster-whisper.",
    packages=find_packages(),
    install_requires=required,
    entry_points={
        'console_scripts': [
            'video_downloader=your_package_name.main:main',  # Replace with actual module and function names if needed
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
