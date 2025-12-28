# Optical Flow Estimation using the Horn–Schunck Method

## Overview
This project implements the Horn–Schunck variational optical flow algorithm for motion estimation in image sequences.

## Method
- Brightness constancy constraint
- Global smoothness regularization
- Iterative optimization of flow fields

## Experiments
- Tested on synthetic and real image sequences
- Analysis of sensitivity to noise and regularization parameters
- Evaluation of smoothness–accuracy trade-offs

## Key Observations
- Strong regularization improves smoothness but reduces motion detail
- Noise significantly affects flow accuracy without proper smoothing

## Technologies
Python, NumPy, OpenCV

## Purpose
The project explores foundational techniques in computer vision and variational optimization.
