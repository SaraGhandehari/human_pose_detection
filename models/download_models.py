#!/usr/bin/env python3
"""
OpenPose Model Downloader
"""

import os
import urllib.request
import sys
import ssl

def main():
    print("=" * 60)
    print("OpenPose Model Downloader")
    print("=" * 60)
    
    # Create directories
    os.makedirs("models/caffe", exist_ok=True)
    
    # Download prototxt file
    print("\n📥 Downloading prototxt file...")
    prototxt_url = "https://raw.githubusercontent.com/CMU-Perceptual-Computing-Lab/openpose/master/models/pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt"
    prototxt_path = "models/caffe/pose_deploy_linevec_faster_4_stages.prototxt"
    
    try:
        # Create SSL context
        context = ssl._create_unverified_context()
        
        # Download
        urllib.request.urlretrieve(prototxt_url, prototxt_path, context=context)
        print(f"✅ Downloaded: {prototxt_path}")
        
        # File size
        size = os.path.getsize(prototxt_path) / 1024
        print(f"📊 File size: {size:.1f} KB")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n📝 Manual download required.")
        print(f"URL: {prototxt_url}")
        return
    
    print("\n" + "=" * 60)
    print("⚠️  IMPORTANT: Manual download required for weights file")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Download weights from:")
    print("   https://drive.google.com/file/d/1N3WYdeeZmbkpY2gLzhnaM7peF8W0bB6G/view")
    print("2. Save file as: models/caffe/pose_iter_160000.caffemodel")
    print("3. File size: ~200MB")
    print("\n✅ Ready to run the notebook!")
    print("=" * 60)

if __name__ == "__main__":
    main()