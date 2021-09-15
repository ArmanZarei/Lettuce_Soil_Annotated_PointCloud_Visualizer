import tkinter as tk
import argparse
import os
from utils import visualize


def btn_clicked(btns, btn_idx, path_dir, file_name):
    btns[btn_idx].configure(foreground='green', activeforeground='green')
    visualize(args.dir_path, f)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir_path', type=str, required=True)
    args = parser.parse_args()

    if not os.path.isdir(args.dir_path):
        raise Exception('Invalid path!')

    files = []
    for f in os.listdir(args.dir_path):
        if f.endswith('.npy'):
            files.append(f.replace('.npy', ''))

    window = tk.Tk(className="Lettuce-Soil Annotated PointCloud Visualizer")
    # window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

    btns = []
    for idx, f in enumerate(files):
        button = tk.Button(
            text=f,
            foreground='red',
            activeforeground='red',
            command=lambda idx=idx: btn_clicked(btns, idx, args.dir_path, f)
        )
        button.pack()
        btns.append(button)

    window.mainloop()