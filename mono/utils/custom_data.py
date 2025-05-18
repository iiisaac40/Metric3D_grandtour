import glob
import os
import json
import cv2

def load_from_annos(anno_path):
    with open(anno_path, 'r') as f:
        annos = json.load(f)['files']

    datas = []
    for i, anno in enumerate(annos):
        rgb = anno['rgb']
        depth = anno['depth'] if 'depth' in anno else None
        depth_scale = anno['depth_scale'] if 'depth_scale' in anno else 1.0
        intrinsic = anno['cam_in'] if 'cam_in' in anno else None
        normal = anno['normal'] if 'normal' in anno else None

        data_i = {
            'rgb': rgb,
            'depth': depth,
            'depth_scale': depth_scale,
            'intrinsic': intrinsic,
            'filename': os.path.basename(rgb),
            'folder': rgb.split('/')[-3],
            'normal': normal
        }
        datas.append(data_i)
    return datas

def load_data(txt_path: str, test_data_path: str):


    with open(txt_path, 'r') as f:
        filelist = f.read().splitlines()
    
    rgb_filelist = [os.path.join(test_data_path, line.split()[0]) for line in filelist]
    depth_filelist = [os.path.join(test_data_path, line.split()[1]) for line in filelist]
    print(f"rgb_filelist: {rgb_filelist[0]}")
    
    # rgbs = glob.glob(path + '/*.jpg') + glob.glob(path + '/*.png')
    intrinsic =  [813.6196057549352, 813.7790107465929, 916.8001833432365, 641.1931876301182] #[721.53769, 721.53769, 609.5593, 172.854]
    data = [{'rgb': rgb, 'depth': depth, 'depth_scale': 1000.0, 'intrinsic': intrinsic, 'filename': os.path.basename(rgb), 'folder': rgb.split('/')[-3]} for (rgb, depth) in zip(rgb_filelist, depth_filelist)]
    return data