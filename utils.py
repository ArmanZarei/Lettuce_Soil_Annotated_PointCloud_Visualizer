import open3d as o3d
import numpy as np
import os

green = (.0, 0.5, .0)
brown = (0.45, 0.16, 0.16)


def visualize(path_dir, file_name):
    ply_path, npy_path = [os.path.join(path_dir, f'{file_name}.{ext}') for ext in ['ply', 'npy']]
    
    pcd = o3d.io.read_point_cloud(ply_path)

    points = np.array(pcd.points)
    mean = points.mean(axis=0)
    points = points - mean
    points /= np.linalg.norm(points, axis=1).max()

    pcd.points = o3d.utility.Vector3dVector(points)

    pcd.colors = o3d.utility.Vector3dVector(np.array([green if label == 1 else brown for label in np.load(npy_path)]))

    o3d.visualization.draw_geometries([pcd])