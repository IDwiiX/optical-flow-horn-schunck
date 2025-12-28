# Optical Flow Estimation using the Horn–Schunck Method

## Overview
This project implements the Horn–Schunck variational optical flow algorithm to estimate dense motion fields between two consecutive grayscale images.

## Method
- Spatial and temporal image derivatives computed using finite-difference convolution kernels
- Gaussian smoothing applied to reduce noise prior to optimization
- Iterative optimization of the Horn–Schunck energy functional with global smoothness regularization
- Flow updates computed until convergence based on the L2 norm of successive updates

## Implementation Details
- Image gradients: Ix, Iy, It via convolution
- Regularization parameter α controls smoothness
- Convergence based on update norm threshold or maximum iterations
- Average-neighborhood smoothing applied to flow fields at each iteration

## Visualization
- Optical flow vectors visualized using quiver plots
- Only vectors with magnitude above the global average are displayed to highlight significant motion

## Technologies
Python, NumPy, OpenCV, SciPy, Matplotlib

## Usage
```bash
python horn_schunck.py image1.png image2.png
