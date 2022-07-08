import cv2
from pathlib import Path
import imutils

STATIC_FILES = Path(__file__).parent / "static"


def main() -> None:
    img = cv2.imread(str(STATIC_FILES / "dungeon_tiles.png"))
    (img_height, img_width) = img.shape[:2]
    # print((height, w))

    # img = imutils.resize(img, 500)
    padding = 32
    tile_size = 16
    gap = 4

    #img[start_row:end_row, start_col:end_col]
    # tile = img[padding:w-padding, padding:]#[padding:padding]

    # crop_tiles(img, image_copy, img_height, img_width, padding, tile_size)
    find_columns(img, gap, padding, tile_size)

    cv2.imwrite("tile_divided.jpg", img)
    cv2.imshow("", img)
    cv2.waitKey(0)

def find_columns(img, gap, padding, tile_size):
    (img_height, img_width) = img.shape[:2]
    image_copy = img.copy()
    for y in range(padding, img_width - padding):
        
    

def crop_tiles(img, padding, tile_size):
    (img_height, img_width) = img.shape[:2]
    image_copy = img.copy()
    x1 = 0
    y1 = 0
    for y in range(padding, img_height - padding, tile_size):
        for x in range(padding, img_width - padding, tile_size):
            if (img_height - y) < tile_size or (img_width - x) < tile_size:
                break

            y1 = y + tile_size
            x1 = x + tile_size

            # check whether the patch width or height exceeds the image width or height
            if x1 >= img_width and y1 >= img_height:
                x1 = img_width - 1
                y1 = img_height - 1
                # Crop into patches of size MxN
                tiles = image_copy[y:y+tile_size, x:x+tile_size]
                # Save each patch into file directory
                cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
                cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
            elif y1 >= img_height:  # when patch height exceeds the image height
                y1 = img_height - 1
                # Crop into patches of size MxN
                tiles = image_copy[y:y+tile_size, x:x+tile_size]
                # Save each patch into file directory
                cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
                cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
            elif x1 >= img_width:  # when patch width exceeds the image width
                x1 = img_width - 1
                # Crop into patches of size MxN
                tiles = image_copy[y:y+tile_size, x:x+tile_size]
                # Save each patch into file directory
                cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
                cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
            else:
                # Crop into patches of size MxN
                tiles = image_copy[y:y+tile_size, x:x+tile_size]
                # Save each patch into file directory
                cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
                cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
    # print(str(STATIC_FILES))


if __name__ == "__main__":
    main()
