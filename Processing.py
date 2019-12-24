import dicom
import numpy as np
import cv2
import pandas as pd
#import dicom
import os
import matplotlib.pyplot as plt
import pydicom
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


def dicom_files(PathDicom):
    lstFilesDCM = []  # create an empty list
    for dirName, subdirList, fileList in os.walk(PathDicom):
        for filename in fileList:
            if ".dcm" in filename.lower():  # check whether the file's DICOM
                lstFilesDCM.append(os.path.join(dirName, filename))
    return lstFilesDCM


def get_dicom_dimensions(lstFilesDCM):
    # Get ref file
    RefDs = pydicom.read_file(lstFilesDCM[0])
    # Load dimensions based on the number of rows, columns, and slices (along the Z axis)
    ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), len(lstFilesDCM))

    # Load spacing values (in mm),  resolution of pixels
    ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SliceThickness))


    x = np.arange(0.0, (ConstPixelDims[0]+1)*ConstPixelSpacing[0], ConstPixelSpacing[0])
    y = np.arange(0.0, (ConstPixelDims[1]+1)*ConstPixelSpacing[1], ConstPixelSpacing[1])
    #z = np.arange(0.0, (ConstPixelDims[2]+1)*ConstPixelSpacing[2], ConstPixelSpacing[2])
    return RefDs, ConstPixelDims, x, y


def create_array_dicom(lstFilesDCM, ConstPixelDims, RefDs):
    # The array is sized based on 'ConstPixelDims'
    ArrayDicom = np.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)

    # loop through all the DICOM files
    for filenameDCM in lstFilesDCM:
        # read the file
        ds = dicom.read_file(filenameDCM)
        # store the raw image data
        ArrayDicom[:, :, lstFilesDCM.index(filenameDCM)] = ds.pixel_array
    return ArrayDicom


def extract_metadata(data): #data is the reference, first file in the folder
    pat_name = data.PatientName
    display_name = pat_name.family_name + ", " + pat_name.given_name
    text_file = open("Patient_Data.txt", "w+")
    text_file.write("Patient's name...:%s\r\n" % display_name)
    text_file.write("Patient id.......:%s\r\n" % data.PatientID)
    text_file.write("Modality.........:%s\r\n" % data.Modality)
    text_file.write("Study Date.......:%s\r\n" % data.StudyDate)

    if 'PixelData' in data:
        rows = int(data.Rows)
        cols = int(data.Columns)
        text_file.write("Image size.......: {rows:d} x {cols:d}, {size:d} bytes\n".format(
            rows=rows, cols=cols, size=len(data.PixelData)))
        if 'PixelSpacing' in data:
            text_file.write("Pixel spacing....:" + str(data.PixelSpacing) + "\n")

    # use .get() if not sure the item exists, and want a default value if missing
    text_file.write("Slice location...:%d\r\n" % data.get('SliceLocation', "(missing)"))
    text_file.close()

def dicom_to_img(lstFilesDCM, ArrayDicom, x, y):
    for i in range(len(lstFilesDCM)):
        plt.figure(dpi=300)
        plt.set_cmap(plt.gray())
        plt.pcolormesh(x, y, np.flipud(ArrayDicom[:, :, i]))
        plt.savefig('./Images/img'+str(i)+'.png')

def contour():
    inputImage = cv2.imread('Images/img100.png')
    scale_percent = 40  # percent of original size
    width = int(inputImage.shape[1] * scale_percent / 100)
    height = int(inputImage.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(inputImage, dim, interpolation=cv2.INTER_AREA)
    cv2.rectangle(resized, (300, 305), (500, 150), (0, 0, 255), 5)
    cv2.imwrite('Tumor_Contour.png', resized)

def process(path):
    PathDicom = path + "/"
    #PathDicom = "./MyHead/"
    lstFilesDCM = dicom_files(PathDicom)
    RefDs, ConstPixelDims, x, y = get_dicom_dimensions(lstFilesDCM)
    extract_metadata(RefDs)
    Dicom_Array = create_array_dicom(lstFilesDCM, ConstPixelDims, RefDs)
    dicom_to_img(lstFilesDCM, Dicom_Array, x, y)
    contour()