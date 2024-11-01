import os
import numpy as np
from PIL import Image
import geopandas as gpd
from shapely.geometry import LineString
from scipy.ndimage import label

def png_to_geojson(image_path, output_geojson):
    # 이미지 로드
    img = Image.open(image_path).convert('RGBA')
    data = np.array(img)

    # 초록색 픽셀 찾기
    green_pixels = (data[:, :, 1] > data[:, :, 0]) & (data[:, :, 1] > data[:, :, 2])  # G > R and G > B

    # 연결된 구성 요소 레이블링
    labeled_array, num_features = label(green_pixels)

    # 고유한 경계 라인을 찾기 위한 좌표 저장
    lines = []

    for feature in range(1, num_features + 1):
        # 각 구성 요소의 좌표 찾기
        rows, cols = np.where(labeled_array == feature)
        if len(rows) > 0:
            # 경계선 좌표 계산
            min_row, max_row = np.min(rows), np.max(rows)
            min_col, max_col = np.min(cols), np.max(cols)

            # 라인 생성 (사각형의 경계선)
            line_coords = [
                (min_col, data.shape[0] - min_row - 1),  # 왼쪽 위
                (max_col, data.shape[0] - min_row - 1),  # 오른쪽 위
                (max_col, data.shape[0] - max_row),      # 오른쪽 아래
                (min_col, data.shape[0] - max_row),      # 왼쪽 아래
                (min_col, data.shape[0] - min_row - 1)   # 다시 왼쪽 위로
            ]
            lines.append(LineString(line_coords))

    # GeoDataFrame 생성 및 CRS 설정
    gdf = gpd.GeoDataFrame(geometry=lines, crs='EPSG:3857')

    # GeoJSON으로 저장
    gdf.to_file(output_geojson, driver='GeoJSON')

def convert_directory_png_to_geojson(input_dir):
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.png'):
            image_path = os.path.join(input_dir, filename)
            output_geojson = os.path.join(input_dir, f"{os.path.splitext(filename)[0]}.geojson")
            png_to_geojson(image_path, output_geojson)
            print(f"Converted {filename} to GeoJSON.")

# 사용 예
input_directory = '/home/bongjae/바탕화면/241101 test/test'  # PNG 파일이 있는 디렉토리 경로
convert_directory_png_to_geojson(input_directory)
