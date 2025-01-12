# GitHub 레포지토리 Fork 및 설정하기 🚀

## 목차
1. [Fork란?](#fork란-무엇인가요)
2. [Fork 하는 방법](#단계별-가이드)
3. [Clone 하기](#clone-하기)
4. [Upstream 설정](#upstream-설정하기)
5. [유용한 Git 명령어](#유용한-git-명령어)

## Fork란 무엇인가요? 🤔

Fork는 쉽게 말해서 '복사본 만들기'입니다. 마치 카페에서 친구의 레시피북을 복사해서 내 것으로 만드는 것처럼, 다른 사람의 프로젝트를 내 GitHub 계정으로 복사하는 것입니다.

## 단계별 가이드 📝

### 1단계: 레포지토리 접속하기
- 웹 브라우저를 열고 "git-tutorial" 레포지토리 주소로 이동합니다
- 이것은 마치 원하는 카페의 정확한 주소를 네비게이션에 입력하는 것과 같습니다

### 2단계: Fork 버튼 클릭하기
- 레포지토리 페이지의 오른쪽 상단에서 "Fork" 버튼을 찾습니다
- 이 버튼은 보통 Star 버튼 옆에 있습니다
- "Fork" 버튼을 클릭하면 새로운 화면이 나타납니다
- 화면에서 Owner(소유자)가 본인의 GitHub 계정으로 되어있는지 꼭 확인하세요
- "Create fork" 버튼을 클릭하여 복사 과정을 완료합니다

### 3단계: Fork 완료 확인하기
- 내 GitHub 프로필 페이지로 이동합니다
- 레포지토리 목록에서 방금 Fork한 "git-tutorial"이 잘 복사되었는지 확인합니다

## Clone 하기 💻

Clone은 온라인 상의 레포지토리를 내 컴퓨터로 다운로드받는 과정입니다. 마치 클라우드에 있는 파일을 내 컴퓨터로 다운로드받는 것과 같습니다.

### Clone 단계
1. **터미널(cmd) 열기**
   - Windows: 시작 메뉴에서 'cmd' 검색
   - Mac: Terminal 앱 실행

2. **Clone 명령어 실행**
   ```bash
   git clone https://github.com/본인깃헙아이디/git-tutorial.git
   ```
   - 예시: 깃헙 아이디가 'LEE1026icarus'인 경우
   ```bash
   git clone https://github.com/LEE1026icarus/git-tutorial.git
   ```

3. **프로젝트 폴더로 이동**
   ```bash
   cd git-tutorial
   ```

## Upstream 설정하기 🔄

Upstream 설정은 원본 레포지토리와의 연결을 만드는 과정입니다. 마치 본사(원본 레포지토리)와 지점(Fork된 레포지토리) 간의 통신 라인을 구축하는 것과 같습니다.

### Upstream 설정 단계
1. **원본 레포지토리 연결**
   ```bash
   git remote add upstream https://github.com/git-tutorial/git-tutorial.git
   ```

2. **설정 확인**
   ```bash
   git remote -v
   ```
   - 이 명령어를 실행하면 origin(내 레포지토리)과 upstream(원본 레포지토리) 두 개의 주소가 보여야 합니다

## 유용한 Git 명령어 📚

자주 사용하는 Git 명령어들을 알아보겠습니다:

- **cd 디렉토리명**: 
  - 원하는 폴더로 이동
  - 예: `cd Documents`

- **git branch**: 
  - 현재 브랜치 확인
  - 활성화된 브랜치는 * 표시로 구분됨

- **pwd**: 
  - 현재 위치한 폴더 경로 확인
  - Print Working Directory의 약자

- **ls -al**: 
  - 현재 폴더의 모든 파일/폴더 목록 표시
  - 숨김 파일도 모두 보여줌

## 주의사항 ⚠️
- Fork와 Clone은 처음 한 번만 하면 됩니다
- Upstream 설정도 처음 한 번만 하면 됩니다
- 명령어 입력 시 오타가 없도록 주의하세요

## 도움이 필요하다면? 🆘
문제가 발생했거나 추가 도움이 필요하다면 GitHub 공식 도움말이나 커뮤니티에 문의해보세요!
