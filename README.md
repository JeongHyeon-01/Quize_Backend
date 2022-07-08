# Quiz-Tech
기술 면접 대비 퀴즈 사이트로 Backend, Frontend의 다양한 면접 질문을 문제은행 식으로 테스트해 볼 수 있다.
Backend 카테고리 : Python, Django, NetWork, DataBase, OS(준비중)
Frontend 카테고리 : React, JavaScript
(CS 관련 카테고리 ex) Network, OS 신설예정)
<br>
- 시연 영상: 
- 프론트엔드 깃헙 주소: 
- API Documentation: https://documenter.getpostman.com/view/20078012/UzJMrFgZ

## 버전
- 0.1.0

## 업데이트 내역
- 0.1.0 : 초기 배포 및 MVP기능 배포

## 개발 기간 및 인원
- 개발 기간: 2022년 6월 20일 ~ 2022년 7월 8일
- 개발 인원: Backend 2명, Frontend 3명
  - Backend  : 고현영, 황정현
  - Frontend : 노규현, 문혜성, 홍두현


## 사용 기술
- Python, Django Rest Framework
  - 빠른 Rest API 구현을 위한 도구로써 DRF를 사용하였고, generics를 활용하여 CRUD를 구성했다.
  
- JWT
  - 유저의 인가 권한을 인식하기위해 토큰방식을 채택 하였고 도구로는 JWT를 선택했다. 짧은 유지 시간을 보완하기 위해 access token과 refresh toekn을 같이 제공하고 알고리즘은 HS256을 사용했다.
    
- AWS EC2, RDS, Router 53
  - AWS 부분의 EC2와 RDS의 경우 배포를 위하여 사용하였고, Router 53의 경우 DNS를 위한 탄력적 IP구성 및 DNS 서비스를 위해 사용했다.
  
- Docker
  - EC2에서 추가적인 작업 없이 배포하기 위하여 사용했다.
  
- Locust
  - 부하테스트를 위하여 사용하였으며 현재 상황의 경우 유저 100명 이하로 받아야 한다.
  -(추가로 redis 서버를 다는것을 생각 중에 있으며 추후 업데이트 예정.)

## 구현 기능
- 구글 소셜 로그인
  - Frontend가 구글에서 받아오는 토큰의 정보를 DB에 정리하여 보관하고, access 토큰 및 refresh 토큰을 리턴한다.
- 대시보드
  - Google에서 받아 오는 정보를 기반으로 유저의 프로필을 리턴한다.
- 퀴즈 카테고리 리스트 및 디테일 페이지
  - Backend/Frontend에 해당하는 카테고리 리스트 및 각 카테고리에 해당하는 카테고리 디테일 페이지를 보여준다.
- 퀴즈 진행 페이지
  - 퀴즈 진행에 관련된 로직으로, DB에 저장되어있는 문제 중 질문과 답을 랜덤하게 보여준다.
- 퀴즈 결과 저장 기능
  - 퀴즈를 제출하면, 퀴즈 패스 여부, 사용 시간, 시도 횟수, 맞은 갯수 등의 퀴즈 정보를 DB에 저장한다.
- 문의 사항을 저장할 수 있는 Support 페이지( 프론트 준비중 )
  - 유저가 문의사항이 있는 경우 해당 페이지에서 작성 후 저장한다.
  - 문의 사항 리스트를 GET을 통해 보여준다.
  - 상세보기의 경우 해당 유저 및 is_staff 권한이 있는 유저만 접근이 가능하다.
  
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
