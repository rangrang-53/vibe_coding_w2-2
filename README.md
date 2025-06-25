# Vibe Coding W2-1

AI Agent를 활용한 채팅 인터페이스 프로젝트입니다.

## 📋 프로젝트 구조

```
vibe_coding_w2-1/
├── backend/                    # FastAPI 백엔드
│   ├── app/
│   │   ├── models/            # 데이터 모델
│   │   └── routers/           # API 라우터
│   ├── tests/                 # 테스트 코드
│   └── requirements.txt
├── frontend/                   # Streamlit 프론트엔드
│   ├── app.py
│   └── requirements.txt
└── docs/                      # 문서
```

## 🚀 시작하기

### 환경 설정

1. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

2. 백엔드 의존성 설치
```bash
cd vibe_coding_w2-1/backend
pip install -r requirements.txt
```

3. 프론트엔드 의존성 설치
```bash
cd ../frontend
pip install -r requirements.txt
```

### 실행

1. 백엔드 서버 실행
```bash
cd vibe_coding_w2-1/backend
uvicorn main:app --reload
```

2. 프론트엔드 실행
```bash
cd vibe_coding_w2-1/frontend
streamlit run app.py
```

## 🧪 테스트

```bash
cd vibe_coding_w2-1/backend
python -m pytest tests/ -v
```

## 🤝 기여하기

### PR 및 이슈 가이드라인

이 프로젝트는 자동화된 GitHub Actions를 사용하여 PR과 이슈를 관리합니다:

#### 🔄 자동화된 기능들

**Pull Request 자동화:**
- 🏷️ 파일 변경 사항에 따른 자동 라벨링
- 👥 리뷰어 자동 할당
- 💬 환영 댓글 및 체크리스트 자동 생성
- 🤖 기본 코드 리뷰 가이드라인 제공
- 🧪 자동 테스트 실행

**Issue 자동화:**
- 🏷️ 이슈 내용 분석을 통한 자동 라벨링
- 👥 컴포넌트별 담당자 자동 할당
- 💬 이슈 타입별 맞춤 응답 댓글
- 📋 처리 프로세스 안내

#### 📝 PR 제출 가이드

1. **브랜치 네이밍**: `타입/간단한-설명`
   - 예: `feat/chat-interface`, `fix/agent-bug`

2. **PR 제목**: `[타입] 간단한 설명`
   - feat: 새로운 기능 추가
   - fix: 버그 수정
   - docs: 문서 수정
   - test: 테스트 코드 추가/수정
   - refactor: 코드 리팩토링

3. **개발 프로세스 (TDD)**:
   - 테스트 코드 작성 → 기능 구현 → 테스트 통과 확인

#### 🐛 이슈 제출 가이드

1. **적절한 템플릿 사용**:
   - 버그 리포트: Bug Report 템플릿
   - 기능 요청: Feature Request 템플릿

2. **제목 규칙**: `[타입] 구체적인 문제/요청 설명`

### 📋 라벨 체계

- **Priority**: critical, high, medium, low
- **Type**: bug, feature, enhancement, documentation, question
- **Component**: backend, frontend, agent, test
- **Status**: in-progress, review-needed, blocked, ready-to-merge

## 🔧 기술 스택

- **Backend**: FastAPI, Python 3.11
- **Frontend**: Streamlit
- **AI Agent**: LangGraph with Gemini-2.5-flash
- **Tools**: DuckDuckGo Search
- **Testing**: pytest
- **CI/CD**: GitHub Actions

## 📚 문서

- [UX Wireframes](docs/ux-wireframes.md)
- [GitHub 관리 룰](.cursor/rules/github-rules.md)

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 있습니다. 