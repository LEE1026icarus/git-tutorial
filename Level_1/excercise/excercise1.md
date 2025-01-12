# Git 연습 문제 상세 가이드

## 1. 새로운 브랜치 생성 및 병합 실습

### 1.1 브랜치 생성 및 전환
```bash
# feature 브랜치 생성
git branch feature/update-readme

# 생성한 브랜치로 전환
git checkout feature/update-readme
# 또는 한 번에 생성하고 전환
git checkout -b feature/update-readme

# 현재 브랜치 확인
git branch
```

### 1.2 파일 수정 및 커밋
```bash
# README.md 파일 수정
echo "## New Feature" >> README.md
echo "This is a new feature branch" >> README.md

# 변경사항 커밋
git add README.md
git commit -m "Add new feature section in README"
```

### 1.3 메인 브랜치에 병합
```bash
# main 브랜치로 전환
git checkout main

# feature 브랜치 병합
git merge feature/update-readme

# 병합 완료 후 feature 브랜치 삭제
git branch -d feature/update-readme
```

## 2. 이전 커밋으로 되돌리기 실습

### 2.1 커밋 히스토리 생성
```bash
# 테스트용 파일 생성
echo "Version 1" > test.txt
git add test.txt
git commit -m "First version"

echo "Version 2" > test.txt
git add test.txt
git commit -m "Second version"

echo "Version 3" > test.txt
git add test.txt
git commit -m "Third version"
```

### 2.2 다양한 되돌리기 방법 실습

#### a. reset 사용 (이전 커밋으로 완전히 되돌리기)
```bash
# 커밋 히스토리 확인
git log --oneline

# soft reset (파일은 스테이징 영역에 유지)
git reset --soft HEAD^

# mixed reset (파일은 워킹 디렉토리에 유지)
git reset --mixed HEAD^

# hard reset (모든 변경사항 제거)
git reset --hard HEAD^
```

#### b. revert 사용 (새로운 커밋으로 되돌리기)
```bash
# 특정 커밋 되돌리기
git revert [커밋해시]

# 최근 커밋 되돌리기
git revert HEAD
```

## 3. 충돌 해결 시나리오

### 3.1 충돌 상황 만들기
```bash
# 1. main 브랜치에서 파일 수정
echo "Main branch content" > conflict.txt
git add conflict.txt
git commit -m "Add content in main"

# 2. 새로운 브랜치 생성 및 전환
git checkout -b feature/conflict

# 3. 같은 파일 다르게 수정
echo "Feature branch content" > conflict.txt
git add conflict.txt
git commit -m "Add content in feature"

# 4. main 브랜치로 전환
git checkout main

# 5. 병합 시도
git merge feature/conflict
```

### 3.2 충돌 해결하기
```bash
# 1. 충돌된 파일 확인
git status

# 2. 충돌 파일 수정
# conflict.txt 파일을 열어서 충돌 부분 수정
# <<<<<<< HEAD
# Main branch content
# =======
# Feature branch content
# >>>>>>> feature/conflict

# 3. 수정된 파일 커밋
git add conflict.txt
git commit -m "Resolve merge conflict"
```

## 실습 체크리스트 ✅

### 브랜치 생성 및 병합
- [ ] 새로운 브랜치를 성공적으로 생성했는가?
- [ ] 브랜치에서 파일을 수정하고 커밋했는가?
- [ ] main 브랜치로 성공적으로 병합했는가?
- [ ] 사용이 끝난 브랜치를 삭제했는가?

### 커밋 되돌리기
- [ ] 여러 개의 테스트 커밋을 생성했는가?
- [ ] reset으로 커밋을 되돌렸는가?
- [ ] revert로 커밋을 되돌렸는가?
- [ ] 각 되돌리기 방식의 차이점을 이해했는가?

### 충돌 해결
- [ ] 의도적으로 충돌 상황을 만들었는가?
- [ ] 충돌된 파일을 확인했는가?
- [ ] 충돌을 성공적으로 해결했는가?
- [ ] 충돌 해결 후 커밋을 완료했는가?

## 추가 도전 과제 🚀

1. **브랜치 전략 연습**
   - feature/, hotfix/, release/ 등 다양한 브랜치 네이밍 컨벤션 적용
   - Git Flow 워크플로우 따라해보기

2. **태그 관리**
   ```bash
   # 태그 생성
   git tag v1.0.0
   git tag -a v1.0.0 -m "First release"
   
   # 태그 푸시
   git push origin v1.0.0
   ```

3. **Stash 활용**
   ```bash
   # 작업 중인 변경사항 임시 저장
   git stash
   
   # 저장한 작업 복원
   git stash pop
   ```

