import os
import numpy as np
from PIL import Image
import geopandas as gpd
from shapely.geometry import Point
from scipy.ndimage import label

def png_to_geojson(image_path, output_geojson):
    # 이미지 로드
    img = Image.open(image_path).convert('RGBA')
    data = np.array(img)

    # 초록색 픽셀 찾기
    green_pixels = (data[:, :, 1] > data[:, :, 0]) & (data[:, :, 1] > data[:, :, 2])  # G > R and G > B

    # 연결된 구성 요소 레이블링
    labeled_array, num_features = label(green_pixels)

    # 고유한 점을 저장하기 위한 리스트
    points = []

    for feature in range(1, num_features + 1):
        # 각 구성 요소의 좌표 찾기
        rows, cols = np.where(labeled_array == feature)
        if len(rows) > 0:
            # 바운딩 박스의 좌표 계산
            min_row, max_row = np.min(rows), np.max(rows)
            min_col, max_col = np.min(cols), np.max(cols)

            # 중심 좌표 계산
            center_x = (min_col + max_col) / 2
            center_y = (data.shape[0] - min_row - 1 + data.shape[0] - max_row) / 2
            
            # 중심 점 생성
            points.append(Point(center_x, center_y))

    # GeoDataFrame 생성 및 CRS 설정
    gdf = gpd.GeoDataFrame(geometry=points, crs='EPSG:3857')

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
input_directory = '/home/bongjae/바탕화면/Kangson_Nu_Monitoring_bongjae/최종 산출물 준비/input/output'  # PNG 파일이 있는 디렉토리 경로
convert_directory_png_to_geojson(input_directory)
