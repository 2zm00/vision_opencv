import cv2

#이미지 읽기
img= cv2.imread('nasa.jpg')

#이미지 표시

# 그레이스케일 변환 << 일반적으로 감지 할 때 그레이스케일로 진행.
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Canny edge detection 적용
edges = cv2.Canny(image=gray_img, threshold1=100, threshold2=200)
# 경계가 감지된 이미지 표시
cv2.imshow('Edge Detected Image', edges)
cv2.imshow('It\'s a NASA IMG',img)

cv2.waitKey(0) #0은 시간 무한, 연상태로 대기
cv2.destroyAllWindows() #창 닫기 << 이걸 꼭 해줘야 함 왜냐면 waitkey로 인해 계속 열려있으니까
