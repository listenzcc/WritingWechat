## image

---

-   [image](#image)
-   [Image folder document](#image-folder-document)

## Image folder document

The image folder contains sub-folders. The sub-folders are images.

The image folders are named as the image. The one of them contains

---

-   Image
    -   [name], the raw image, the extent name is as the same as the image;
    -   raw.jpg, the raw image with jpeg format;
    -   resize.jpg, the well formatted image;
    -   thumb.jpg, the small thumb version of the image.

---

-   label
    -   objects.jpg, the boxes of objects;
    -   objects.json, the json of objects;

---

-   depth
    -   depth.jpg, the depth map of the image;

---

-   segment
    -   segment.jpg, the image segmentation;
    -   segment.json, the json of segmentation;
    -   segment/, the folder of segmentation detail;
        -   mask-[%1]-[%2]-[%3].jpg, the 255 mask of the segments;
            -   %1: the idx of the segment;
            -   %2: the name of the segment;
            -   %3: the score of the segment.
        -   cover-[%1]-[%2]-[%3].png, the png cover of the segment, only the inside segment is displayed, the others are transparent.

---

-   inpaint
    -   mask-[%1]-[%2]-[%3].jpg, the inpainted image using the mask in segment folder
