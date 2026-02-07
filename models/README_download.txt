OPENPOSE MODEL DOWNLOAD INSTRUCTIONS
=====================================

REQUIRED FILES:
---------------
1. pose_deploy_linevec_faster_4_stages.prototxt
   Size: ~25 KB
   Download automatically using: python scripts/download_models.py

2. pose_iter_160000.caffemodel
   Size: ~200 MB
   Manual download required

DOWNLOAD METHODS:
----------------

METHOD 1: Automatic (prototxt only)
-----------------------------------
Run: python scripts/download_models.py

METHOD 2: Manual Download
-------------------------
1. PROTOTXT FILE:
   URL: https://raw.githubusercontent.com/CMU-Perceptual-Computing-Lab/openpose/master/models/pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt
   Save to: models/caffe/pose_deploy_linevec_faster_4_stages.prototxt

2. WEIGHTS FILE:
   URL: https://drive.google.com/file/d/1N3WYdeeZmbkpY2gLzhnaM7peF8W0bB6G/view
   Save to: models/caffe/pose_iter_160000.caffemodel

VERIFICATION:
------------
After download, check:
- models/caffe/pose_deploy_linevec_faster_4_stages.prototxt
- models/caffe/pose_iter_160000.caffemodel

TROUBLESHOOTING:
---------------
If download fails:
1. Check internet connection
2. Download manually using URLs above
3. Ensure files are in correct location

CONTACT:
--------
For issues: SaraGhandehari
Repository: https://github.com/SaraGhandehari/human_pose_detection