# Human Pose Detection: Sitting vs Standing Classification

A computer vision project that detects human posture (sitting or standing) in video streams using OpenPose and geometric analysis of joint angles.

## 🎯 Project Overview
This project implements a **real-time human posture detection system** that classifies whether a person is **sitting** or **standing** using computer vision techniques. It leverages the **OpenPose** deep learning model for human pose estimation and performs geometric analysis of joint angles for robust, scale-invariant classification.

**Key Innovation:** The system uses frame skipping optimization to achieve real-time performance without sacrificing accuracy, making it suitable for practical applications like ergonomic monitoring, healthcare, and human-computer interaction.

## ✨ Features
- **Real-time Posture Detection**: Classifies sitting/standing states in video streams
- **OpenPose Integration**: Accurate 15-point human skeleton extraction
- **Geometric Analysis**: Scale-invariant angle calculation using knee joints
- **Performance Optimization**: Frame skipping for real-time processing
- **Visual Feedback**: Real-time skeleton overlay and posture labels
- **Easy Configuration**: Adjustable parameters for different scenarios
- **Video Processing**: Support for various video formats (MP4, AVI, etc.)
- **Export Capabilities**: Save processed videos with visualizations
- **Robust to Scale**: Geometric approach ensures scale invariance


## 🛠️ Technologies Used
- **Python 3.8+**
- **OpenCV** - Computer vision operations
- **OpenPose** - Human pose estimation
- **NumPy** - Mathematical operations
- **Jupyter Notebook** - Interactive development
