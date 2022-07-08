# Quiz-Tech
기술 면접 대비 퀴즈 사이트로 Backend, Frontend의 다양한 면접 질문을 연습해 볼 수 있습니다.
<br>
- 시연 영상: 
- 프론트엔드 깃헙 주소:
- API Documentation:

## 버전
- 0.1.0

## 업데이트 내역


## 개발 기간 및 인원
- 개발 기간: 2022년 6월 20일 ~ 2022년 7월
- 개발 인원: 백엔드 2명, 프론트엔드 3명
- 개발자 : Back end  : 고현영, 황정현
         Front end : 노규현, 문혜성, 홍두현


## 사용 기술
- Python, Django Rest Framework
  - 빠른 Rest API 구현을 위한 도구로써 DRF를 사용하였고, generics를 활용하여 CRUD를 
- JWT
  - 유저의 인가 권한을 인식하기위해 토큰방식을 채택 하였고 도구로는 JWT를 택하였고,
    기존에 JWT를 사용하여 인증인가 방식을 구현해 보았기 때문에 조금더 친숙하고 구현하기 쉬운 Json Web token을 채택하였고  짧은 유지 시간을 보완하기 위해 Refresh toekn 을 발급하였다.
    알고리즘은 HS256을 채택하였다.
- AWS EC2, RDS, Router 53
  - AWS 부분의 EC2, RDS의 경우 배포를 위하여 사용하였고
  - Router 53의 경우 DNS를 위한 탄력적 IP구성 및 DNS 서비스를 위해 사용을 하였다.
- Docker
  - image build를 위해 사용 
- Locust
  - 부하테스트를 위하여 사용하였으며 현재 상황의 경우 유저 100 명 이하로 받아야한다.
  (추가로 redis 서버를 다는것을 생각중에 있다.  추후 업데이트 예정)

## 구현 기능
- 구글 소셜 로그인
  - Frontend 에서 구글에서 받아오는 토큰의 정보를 우리 DB에 정리하여 보관하고 access 토큰및 refresh 토큰을 리턴해준다.
- 대시보드
  - Google에서 받아오는 정보를 기반으로 유저의 프로필을 리턴해준다.
- 퀴즈 카테고리 리스트 및 디테일 페이지
  - 백엔드/프론트엔드에 해당하는 대 카테고리 리스트 및 각 카테고리에 해당하는 소 카테고리를 나타 낸다.
- 퀴즈 진행 페이지
  - 퀴즈 진행에 관련된 로직으로 DB에 저장되어있는 문제중 Random하게 10문제를 받아오는 API
- 퀴즈 결과 저장 기능
  - 프론트에서 POST를 통한 정보를 주는경우 User Rank에 데이터를 저장
- 문의 사항을 저장할 수 있는 Support 페이지
  - 문의사항을 저장 POST로 저장
  - get의 경우 모든 문의사항 리스트를 보여준다.
  - 상세보기의 경우 해당유저및 is_staff권한이 있는 유저만 접근이 가능하다.
  
- AWS EC2, RDS, Router53 및 Docker를 이용한 배포
- Locust를 이용한 부하테스트


## 기여 방법
1. (https://github.com/yourname/yourproject/fork)을 포크합니다.
2. (git checkout -b feature/fooBar) 명령어로 새 브랜치를 만드세요.
3. (git commit -am 'Add some fooBar') 명령어로 커밋하세요.
4. (git push origin feature/fooBar) 명령어로 브랜치에 푸시하세요. 
5. 자신의 이메일을 pr에 포함해서 풀리퀘스트를 보내주세요.


### Contact
문의 사항이 있으신 분은 gusdud3890@gmail.com 또는 auddwd19@naver.com으로 연락주세요.
