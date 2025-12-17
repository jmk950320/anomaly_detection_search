from elpv_dataset.utils import load_dataset

if __name__ == "__main__":
    images, proba, types = load_dataset()
    print("len(image): ", len(images))
    print("len(proba): ", len(proba))
    print("len(types): ", len(types))

    # 첫 번째 이미지의 결함 확률과 모듈 종류 출력
    for image, proba, type_ in zip(images, proba, types):
        print(f"첫 번째 샘플 - 확률: {proba}, 종류: {type_}")
   #print(f"첫 번째 샘플 - 확률: {proba[0]}, 종류: {types[0]}")