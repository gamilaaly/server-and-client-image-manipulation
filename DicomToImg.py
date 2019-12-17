import numpy as np
import cv2
import pandas as pd
import dicom
import os
import matplotlib.pyplot as plt
#import pydicom
from pydicom.data import get_testdata_files


def HSV_edges_masks(inputImage):
    inputImageHSV = cv2.cvtColor(inputImage, cv2.COLOR_BGR2HSV)
    lower_green = np.array([80, 40, 40])
    upper_green = np.array([100, 255, 255])
    mask = cv2.inRange(inputImageHSV, lower_green, upper_green)
    edges = cv2.Canny(mask, 200, 400)
    return mask, edges


def get_Contour(inputImage):
    ###Contour
    src_gray = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)
    src_gray = cv2.blur(src_gray, (3, 3))
    ## [Canny]
    # Detect edges using Canny
    src_gray = region_of_interest(src_gray)
    threshold = 200
    canny_output = cv2.Canny(src_gray, threshold, threshold * 2)
    cv2.imshow("cannyout", canny_output)
    ## [Canny]
    ## [findContours]
    # Find contours
    contours, _ = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areaArray = []
    ## [findContours]
    # Approximate contours to polygons + get bounding rects and circles
    contours_poly = [None] * len(contours)
    boundRect = [None] * len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(
            contours_poly[i]
        )  # x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        areaArray.append(area)
    ## [zeroMat]
    # print("coor", boundRect[i])
    drawing = np.zeros(
        (canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8
    )
    # first sort the array by area
    sorteddata = sorted(zip(areaArray, contours), key=lambda x: x[0], reverse=True)
    direction = None
    if (len(contours) >= 3):

        # find the nth largest contour [n-1][1], in this case 2
        secondlargestcontour = sorteddata[2][1]

        # draw it
        x, y, w, h = cv2.boundingRect(secondlargestcontour)
        cv2.drawContours(drawing, secondlargestcontour, -1, (255, 0, 0), 2)
        cv2.rectangle(drawing, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print(x, y, w, h)
        if (x < 120):
            direction = 1  #right
        else:
            direction = 2  #left
    return drawing, direction


# inputImage = cv2.imdecode(img_arr, -1)
# mask, edges = HSV_edges_masks(inputImage)
# drawing, direction = get_Contour(inputImage)
# drawing_gray = cv2.cvtColor(drawing, cv2.COLOR_BGR2GRAY)
# # print(edges.shape,"hiiiiiii", drawing_gray.shape)
# combined = cv2.add(drawing_gray, edges)
# combined_pic = cv2.add(drawing, inputImage)

PathDicom = "./MyHead/"
lstFilesDCM = []  # create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            lstFilesDCM.append(os.path.join(dirName, filename))


# Get ref file
RefDs = dicom.read_file(lstFilesDCM[0])

# Load dimensions based on the number of rows, columns, and slices (along the Z axis)
ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), len(lstFilesDCM))

# Load spacing values (in mm)
ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SliceThickness))


x = np.arange(0.0, (ConstPixelDims[0]+1)*ConstPixelSpacing[0], ConstPixelSpacing[0])
y = np.arange(0.0, (ConstPixelDims[1]+1)*ConstPixelSpacing[1], ConstPixelSpacing[1])
z = np.arange(0.0, (ConstPixelDims[2]+1)*ConstPixelSpacing[2], ConstPixelSpacing[2])


# The array is sized based on 'ConstPixelDims'
ArrayDicom = np.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)

# loop through all the DICOM files
for filenameDCM in lstFilesDCM:
    # read the file
    ds = dicom.read_file(filenameDCM)
    # store the raw image data
    ArrayDicom[:, :, lstFilesDCM.index(filenameDCM)] = ds.pixel_array


for i in range(len(lstFilesDCM)):
    plt.figure(dpi=300)
    #plt.axes().set_aspect('equal', 'datalim')
    plt.set_cmap(plt.gray())
    plt.pcolormesh(x, y, np.flipud(ArrayDicom[:, :, i]))
    plt.savefig('img'+str(i)+'.png')
    #plt.show()