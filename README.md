# Raster-BoundingBox-GeoJSON

## Overview

This code is part of a research project titled "Monitoring Vessel Movements Near North Korea's Kangson Nuclear Facility: Object Detection of Sentinel-1 Imagery Using Yolov5 and Integration with Open Source GIS." The project, named Raster-BoundingBox-GeoJSON, was developed to convert raster data bounding boxes into GeoJSON format. It includes scripts that can transform bounding box information into centroid and vector formats, making it useful for various GIS applications. This tool enhances the flexibility of representing and analyzing bounding boxes, thereby improving efficiency in GIS-based visualization and analysis tasks.

This research was conducted without external funding, as a personal study. In this context, instead of uploading all Yolov5 model code, I implemented certain functions using general OpenCV-based Python code to achieve the research objectives. This choice allowed me to maintain essential object detection capabilities while improving the efficiency of code sharing and execution.
## Author

Bongjae Kwon  
Civil and Environmental Engineering GIS/LBS Lab  
Seoul National University

bongjae.kwon@snu.ac.kr

## Features

- Convert raster bounding boxes to GeoJSON format.
- Generate centroid points from bounding boxes.
- Create vector representations of bounding boxes in GeoJSON.

## Installation

To use this project, you need to have the following prerequisites:

- Python 3.x
- Required Python packages:
  - `geopandas`
  - `shapely`
  - `rasterio` (if applicable)

You can install the required packages using pip:

```bash
pip install geopandas shapely rasterio
