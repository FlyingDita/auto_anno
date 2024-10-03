import tkinter as tk
from tkinter import filedialog
import cv2
import os

# 全局变量
drawing = False  # 鼠标按下标志
ix, iy = -1, -1  # 起始坐标
rectangles = []  # 存储矩形坐标
origin_folder_paths = []
output_folder_paths = []

# 获取鼠标标注结果
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, rectangles

    if event == cv2.EVENT_LBUTTONDOWN:  # 鼠标左键按下
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:  # 鼠标移动
        if drawing:
            img_copy = img.copy()  # 复制图像
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 1)
            cv2.imshow('Image', img_copy)

    elif event == cv2.EVENT_LBUTTONUP:  # 鼠标左键抬起
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
        rectangles.append((ix, iy, x, y))  # 保存矩形坐标

# # 设置键盘事件
# def on_key_press(event):
#     if event.char == 'w':
#         function1()
#     if event.char == 'e':
#         function2()
#     if event.char == 'q':
#         function3()


def select_folder(folder_path):
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    folder_path = filedialog.askdirectory()  # 弹出文件夹选择对话框

    print(folder_path)
    return folder_path


def function1():
    global origin_folder_paths
    print("Function 1 is called")
    origin_folder_paths = select_folder(origin_folder_paths)
    # print(origin_folder_paths)

def function2():
    global output_folder_paths
    print("Function 2 is called")
    output_folder_paths = select_folder(output_folder_paths)


def function3():
    print("Function 3 is called")
    global origin_folder_paths
    print(origin_folder_paths)
    if (origin_folder_paths!=[]) and (output_folder_paths!=[]):
        global img, rectangles
        file_paths = []
        for root, dirs, files in os.walk(origin_folder_paths):
            for file in files:
                # 拼接文件的完整路径
                full_path = os.path.join(root, file)
                file_paths.append(full_path)
        

        # print(file_paths)
        for index,img_path in enumerate(file_paths):
            img_name = img_path.split("\\")[1]
            # print(img_name)
            save_img_path = output_folder_paths + '/' + img_name
            txt_path = output_folder_paths + '/' + img_name.replace('.jpg','.txt')
            img = cv2.imread(img_path)
            # resize
            img = cv2.resize(img,(960,540))
            cv2.namedWindow('Image')
            cv2.imshow('Image',img)
            cv2.setMouseCallback('Image', draw_rectangle)
            while True:
                key = cv2.waitKey(1) & 0xFF
                if key == ord('d'):  
                    # print("yesyes")
                    with open(txt_path, 'w') as f:
                        for rect in rectangles:
                            f.write(f"{rect}\n")
                    print(f"Annotations saved to {txt_path}")
                    cv2.imwrite(save_img_path,img)
                    break
            cv2.imshow('Image',img)
            cv2.waitKey(1)
            if index == len(file_paths)-1:
                finnal_img = cv2.imread('finnal.png')
                cv2.imshow('Image',finnal_img)
                cv2.waitKey(0)
    else:
        print("origin and output folder select is essential !!! ")



if __name__  == "__main__":

    file_list = []

    # 创建主窗口
    root = tk.Tk()
    root.title("按钮功能示例")

    # 设置界面大小
    root.geometry('300x200')

    # 创建按钮，并将其与相应的函数绑定
    button1 = tk.Button(root, text="读取文件夹", command=function1)
    button1.pack(pady=10)

    button2 = tk.Button(root, text="选择输出标注文件路径", command=function2)
    button2.pack(pady=10)

    button3 = tk.Button(root, text="读取图片", command=function3)
    button3.pack(pady=10)

    # 进入主循环
    # root.bind('<Key>', on_key_press)
    root.mainloop()
