import cv2

#동영상 캡처
cap = cv2.VideoCapture("earth.mp4") #웹캠 = VideoCapture(0)

#Bool 값 넣기 
edge_bool= False


#기본 포맷임. 거의 고정으로 쓰는 포맷
while cap.isOpened():
	ret, frame = cap.read() #ret = 잘 불러왔는지, frame = 영상화면
	if not ret: #if ret==False 랑 같은 말
		break

	#그레이스케일 변환
	gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	#Canny detection
	edges = cv2.Canny(image=gray_img, threshold1=100, threshold2=200)

	if edge_bool:
		image = edges
	else:
		image = frame

	cv2.imshow("Video", image)
	key = cv2.waitKey(1) #속도 조정
	if key == ord("q"):break #키보드 q를 누르면 꺼짐. q의 경우 ord로 정수로 반환되는데, 그 정수가 키보드 입력되면 꺼진다는 이야기.
	elif key == ord("b"):
		edge_bool = not edge_bool


cap.release() #외부 자원은 반환
cv2.destroyAllWindows()