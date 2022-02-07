# watch_ssunel(개발중)
  > 쑤넬이를 지키기 위한 모니터링 시스템

### 요람에 있는 쑤넬이가 혹시 모를 사고 예방 또는 깨어났을 때 우리 부부가 기민하게 대처하기 위하여 Vision등 몇가지 기술을 활용하여 개발 함.
- CCTV: Amcrest IP3M-941W
- 5초마다 쑤넬이 상태 확인
- 쑤넬이의 상태를 분류하기
  * 울고 있을 때: Face Detection / Emotion Classification
  * 깨어 났을 때: Face Detection / Emotion Classification
  * 엎드려 있을 때: Pose Estimation / Face Detection
  * 기타: 소리 활용
- 이전 상태와 비교하기
  * 안울고 있다가(자고있거나 깨어있거나) 울기 시작
  * 자고있다가 깨어났을 때
  * 뒤척이다 엎드려 있게될 때
  * 기타
- 비교해서 달라진 경우 카카오톡(kakaotalk)으로 전송

### 작업목록
* 아이 상태 분류기
  - AIP 사용하여 아이가 울음/엎드려 있음/자고 있음등 분류하고 상태 알림 발송 
  - 아이 있는지 확인: 얼굴 있는 확인하는 방법 적용(https://github.com/GangYuanFan/Closed-Eye-Detection-with-opencv)
  - 얼굴인식기 완료 
  - 표정인식기 진행중 
  - 자세인식기 진행중 https://github.com/sithu31296/pose-estimation 
  - 아이인식기 진행중 
  - 눈 인식기 진행중 https://github.com/GangYuanFan/Closed-Eye-Detection-with-opencv 
