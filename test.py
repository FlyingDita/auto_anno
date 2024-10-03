import cv2
import os

# 全局变量
drawing = False  # 鼠标按下标志
ix, iy = -1, -1  # 起始坐标
rectangles = []  # 存储矩形坐标

# 鼠标回调函数
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, rectangles

    if event == cv2.EVENT_LBUTTONDOWN:  # 鼠标左键按下
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:  # 鼠标移动
        if drawing:
            img_copy = img.copy()  # 复制图像
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 1.5)
            cv2.imshow('Image', img_copy)

    elif event == cv2.EVENT_LBUTTONUP:  # 鼠标左键抬起
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1.5)
        rectangles.append((ix, iy, x, y))  # 保存矩形坐标

# 标注多张图片的函数
def annotate_images(image_folder):
    global img, rectangles
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png'))]

    for image_file in image_files:
        img = cv2.imread(os.path.join(image_folder, image_file))
        rectangles = []  # 每张图片清空标注
        cv2.namedWindow('Image')
        
        key = cv2.waitKey(1) & 0xFF
        # if key == ord('q'):
            
        cv2.setMouseCallback('Image', draw_rectangle)

        while True:
            cv2.imshow('Image', img)
            key = cv2.waitKey(1) & 0xFF
            # 按 'Esc' 键进入下一张
            if key == 27:
                break
            # 按 's' 键保存标注
            elif key == ord('w'):  
                with open(f'{image_file}_annotations.txt', 'w') as f:
                    for rect in rectangles:
                        f.write(f"{rect}\n")
                print(f"Annotations saved to {image_file}_annotations.txt")
            elif key == ord('q'):
                rectangles = rectangles[-1]
        cv2.imshow('Image', img)
        cv2.destroyAllWindows()

# 调用标注函数，替换为你的图片文件夹路径
origin_path = r'D:\repo\database\Test\origin/'
annotate_images(origin_path)
