# Metadata Extractor Script

MetaExtractor is simple Python script designed to extract metadata from image files, including JPEG and PNG formats.

## Prerequisites

```
Python 3.x
Pillow library
Piexif library
```

## Installation

### Clone the Repository:

Download or clone this repository to your local machine.

`git clone https://github.com/deadbyteus/MetaExtractor.git`

### Navigate to the Directory:

Change your working directory to the location of the script.

`cd MetaExtractor`

### Install Dependencies:

Install the required Python dependencies using pip.

```
pip install pillow
pip install piexif
```

## Usage

### Set the Parent Directory:

Open the metaextractor.py script and set the PARENT_DIRECTORY variable to the directory where your image files are located.

```
Set the parent directory where images are located
PARENT_DIRECTORY = r"/path/to/your/image/directory"
```

### Run the Script:

Execute the script using Python.

`python metaextracor.py`

### View Results:

Metadata will be extracted from the images and saved as text files in the same directory as the images. For JPG files, the UserComments will also be saved as text files.

## Example

Suppose you have the following directory structure:

```
/my_images
    /image1.jpg
    /image2.png
    /subdirectory
        /image3.jpg
        /image4.png
```

Set PARENT_DIRECTORY in the script to /my_images, and running the script will extract metadata from all images in the specified directory and its subdirectories.

```
/my_images
    /image1.jpg
    /image1.txt
    /image2.png
    /image2.txt
    /subdirectory
        /image3.jpg
        /image3.txt
        /image4.png
        /image4.txt
```

## Troubleshooting

If you encounter any issues or errors while running the script, ensure that you have the required Python libraries installed and that the paths in the script are correctly configured.

Ensure that the image files you want to process are located in the specified PARENT_DIRECTORY.

Make sure your Python environment is properly set up.

## License

This project is licensed under the GNU GPL License - see the LICENSE file for details.
