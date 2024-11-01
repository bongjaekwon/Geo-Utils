import cv2
import numpy as np
import os

def detect_white_and_gray_dots(image_path, max_width=100, max_height=100):
    # 1. 이미지 읽기
    img = cv2.imread(image_path)

    # 2. 이미지를 흑백으로 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. 회색 점 검출을 위한 임계값 설정 (150 이상으로 설정)
    _, thresholded = cv2.threshold(gray, 145, 255, cv2.THRESH_BINARY)

    # 4. 모폴로지 연산 (침식 후 팽창)
    kernel = np.ones((3, 3), np.uint8)  # 커널 크기 조정
    morphed = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)

    # 5. 흰색 점의 외곽선을 검출
    contours, _ = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 6. 흰색 및 회색 점에 바운딩 박스를 그림
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)  # 바운딩 박스의 좌표와 크기
        
        # 크기 제한을 체크
        if w <= max_width and h <= max_height:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 초록색 바운딩 박스 그리기

    # 7. 결과 파일 이름 생성 (원본 파일 이름 유지)
    base_name = os.path.basename(image_path)  # 파일 이름만 추출
    name, ext = os.path.splitext(base_name)  # 이름과 확장자 분리
    output_path = os.path.join(os.path.dirname(image_path), f"{name}_output.png")  # 출력 파일 경로

    # 8. 결과 이미지 저장 및 출력
    cv2.imwrite(output_path, img)  # 결과 이미지 저장
    cv2.imshow('Detected White and Gray Dots', img)  # 이미지 창으로 출력
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 사용자에게 이미지 경로를 입력받음
image_path = input("안녕하세요 봉재님, 이미지 파일의 경로를 입력하세요: ")

# 사용 예시
detect_white_and_gray_dots(image_path)
