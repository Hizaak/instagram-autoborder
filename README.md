# Autoborder for Instagram
## A Python script to make 1080x1080 images with a white border out of a base image

- How does it work :

1. Go to the folder where the script is  
2. Make sure extensions are '.png', '.jpg' or '.jpeg' (caps allowed)  
The script will not break anything if it isn't the case, but you'll lose some time plus generate only few images in certain cases...
3. Execute the script  
Use `python script.py path/image1 path/image2 ... path/imageX` in the command line to generate the images with their border.  
Images are generated as `path/imageX_instagram.jpg`

- Notes
	- I could implement more complex arguments, as this script only makes what I need, but the code is still very easy to understand and you'll have no difficulties to change anything.
	- The images are exported as the highest Instagram post resolution (1080px wide and 1080px high), thus exporting in an higher resolution would result in a compression, and make your images even more blurry. **Don't do it**.
