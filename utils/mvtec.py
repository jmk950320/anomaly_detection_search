
"""
PNG 파일 읽기 및 픽셀 값 출력 유틸리티

이 모듈은 PNG 이미지 파일을 읽고 픽셀 값들을 다양한 형태로 출력하는 기능을 제공합니다.
"""
import numpy as np
import cv2
import argparse, os
import matplotlib.pyplot as plt

# ... (앞부분 import는 동일)

def generate_grayscale_histogram(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) # 흑백으로 읽기
    
    if img is None:
        print(f"오류: 이미지를 로드할 수 없습니다. 경로를 확인하세요: {image_path}")
        return

    # 히스토그램 계산 (채널은 하나(0), 마스크 없음, 256개의 BIN)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray') # 흑백 이미지 표시를 위해 cmap='gray' 사용
    plt.title('Grayscale Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.plot(hist, color='black') # 검은색 선으로 플로팅
    plt.title('Grayscale Histogram')
    plt.xlabel('Pixel Intensity Value (0-255)')
    plt.ylabel('Frequency (Pixel Count)')
    plt.xlim([0, 256])
    
    plt.show()

def generate_masking_img(img_path, gt_path):
    img = cv2.imread(img_path)
    gt_img = cv2.imread(gt_path, cv2.IMREAD_GRAYSCALE) 
    print(np.sum(gt_img==1))
    masked_img = cv2.bitwise_and(img, img, mask=gt_img)
    cv2.imshow("masked_img : ", masked_img)
    cv2.imshow("image", img)
    cv2.imshow("gt_img", gt_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return masked_img

def main():
   

   image_path= "/home/kjm/anomaly_dataset/datasets/mvtec_anomaly_detection/bottle/test/broken_large/000.png"
   gt_path = "/home/kjm/anomaly_dataset/datasets/mvtec_anomaly_detection/bottle/ground_truth/broken_large/000_mask.png"
   _ = generate_grayscale_histogram(image_path)
   _ = generate_masking_img(img_path=image_path, gt_path=gt_path)


if __name__ == "__main__":
    main()