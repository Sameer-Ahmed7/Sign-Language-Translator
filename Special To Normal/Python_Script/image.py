import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
print(ap.parse_args())
args = vars(ap.parse_args())
print(args)
image = cv2.imread(args["image"])
cv2.imshow("image", image)
cv2.waitKey(0)

#python load_image.py --image doge.jpg