# 건강관리 실습 프로젝트 (FastAPI + Jinja + SQLite + Tortoise)

강의 실습용으로 준비된 프로젝트입니다. `complete`는 전체 완성본, `practice`는 일부 백엔드 코드가 미완성인 실습용입니다. 프론트엔드는 두 프로젝트 모두 완성된 형태입니다.

![대시보드 화면](assets/dashboard.png)

## 요구 사항
- Python 3.12
- 가상환경 사용 권장

## 실행 방법 (공통)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 폴더 구성
- `complete/`: 전체 완성 코드
- `practice/`: 실습용 코드 (일부 ORM/백엔드 로직 미완성)

각 폴더에 들어가 실행하세요.

```bash
cd complete
pip install -r requirements.txt
uvicorn app.main:app --reload
```

```bash
cd practice
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 실습 가이드 (practice)
- `WaterLog` 관련 ORM/라우팅은 완성되어 있습니다.
- `Exercise`, `Meal`, `Sleep` 영역은 TODO 주석을 참고해 ORM 및 API를 완성하는 흐름입니다.
- 프론트엔드는 모두 완성되어 있으므로, 백엔드가 연결되면 바로 동작합니다.
- `/report` 페이지는 pandas + matplotlib 예시입니다.
