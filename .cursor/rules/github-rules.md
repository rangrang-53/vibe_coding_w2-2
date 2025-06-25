# GitHub PR 및 이슈 관리 룰

## Pull Request (PR) 관리 룰

### PR 생성 시 필수 사항
1. **제목 규칙**: `[타입] 간단한 설명`
   - feat: 새로운 기능 추가
   - fix: 버그 수정
   - docs: 문서 수정
   - style: 코드 스타일 변경 (로직 변경 없음)
   - refactor: 코드 리팩토링
   - test: 테스트 코드 추가/수정
   - chore: 빌드, 설정 파일 수정

2. **브랜치 네이밍**: `타입/간단한-설명`
   - 예: `feat/chat-interface`, `fix/agent-bug`

3. **PR 설명 템플릿**:
   ```markdown
   ## 변경 사항
   - 주요 변경 내용 설명

   ## 테스트
   - [ ] 테스트 코드 작성 완료
   - [ ] 모든 테스트 통과 확인

   ## 체크리스트
   - [ ] 코드 리뷰 완료
   - [ ] 문서 업데이트 완료 (필요한 경우)
   - [ ] 브레이킹 체인지 확인
   ```

### PR 리뷰 규칙
1. **필수 리뷰어**: 최소 1명 이상의 코드 리뷰 필요
2. **자동 할당**: 팀 멤버 중 랜덤으로 자동 할당
3. **자동 라벨링**: 파일 변경 경로에 따라 자동 라벨 부여

## Issue 관리 룰

### Issue 생성 시 필수 사항
1. **제목 규칙**: `[타입] 구체적인 문제/요청 설명`
   - bug: 버그 리포트
   - feature: 새로운 기능 요청
   - enhancement: 기존 기능 개선
   - question: 질문
   - documentation: 문서 관련

2. **Issue 템플릿**:
   ```markdown
   ## 설명
   문제나 요청 사항에 대한 구체적인 설명

   ## 재현 방법 (버그인 경우)
   1. 단계별 재현 방법
   2. 예상 결과
   3. 실제 결과

   ## 추가 정보
   - 환경 정보
   - 스크린샷 (필요한 경우)
   ```

### Issue 처리 규칙
1. **자동 할당**: 이슈 타입에 따라 담당자 자동 할당
2. **자동 라벨링**: 이슈 내용 분석하여 적절한 라벨 자동 부여
3. **자동 댓글**: 이슈 생성 시 처리 프로세스 안내 댓글 자동 등록

## 라벨 체계

### Priority 라벨
- `priority: critical` - 즉시 처리 필요
- `priority: high` - 높은 우선순위
- `priority: medium` - 보통 우선순위
- `priority: low` - 낮은 우선순위

### Type 라벨
- `type: bug` - 버그
- `type: feature` - 새로운 기능
- `type: enhancement` - 기능 개선
- `type: documentation` - 문서
- `type: question` - 질문

### Component 라벨
- `component: backend` - 백엔드 관련
- `component: frontend` - 프론트엔드 관련
- `component: agent` - Agent 관련
- `component: test` - 테스트 관련

### Status 라벨
- `status: in-progress` - 진행 중
- `status: review-needed` - 리뷰 필요
- `status: blocked` - 블로킹됨
- `status: ready-to-merge` - 머지 준비 완료 