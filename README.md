# TaskTrackerCLI

roadmap.sh 에서 추천한 node.js 관련 기초 프로젝트.
CLI(Command Line Interface) 환경에서 실행하여, 할 일 목록을 create, update, delete, check하는 간단한 프로그램임.

이 프로젝트는 [roadmap.sh](https://roadmap.sh/projects/task-tracker)의 가이드를 참고하여 개발되었음을 밝힘.

## 주요 기능

- 새로운 할 일 생성(create)
- 전체 할 일 목록 조회(show)
- 기존 할 일 내용 수정(update)
- 특정 할 일 삭제(delete)
- 할 일 완료/미완료 상태 변경(check)

## 요구 사항

- Python 3.x
- python 표준 라이브러리 외 다른 의존성 없음

## 설치

1. 리포지토리 클론:
   ```bash
   git clone https://github.com/lazyjsh03/TaskTrackerCLI.git
   ```
2. 프로젝트 디렉토리로 이동:
   ```bash
   cd TaskTrackerCLI
   ```

## 실행

1. 다음 명령어로 어플리케이션 실행:
   ```bash
   python TaskTracker.py
   ```
2. 프롬프트('TaskCLI>> ')가 나타나면 명령어 입력:
   - `create`: 새로운 할 일 생성.
   - `show`: 저장된 할 일 목록을 출력
   - `update <id>`: 지정한 `<id>`의 할 일 내용 수정
   - `delete <id>`: 지정한 `<id>`의 할 일 삭제
   - `check <id>`: 지정한 `<id>`의 완료 상태 변경
   - `help`: 사용 가능한 명령어 표시시
   - `help <command>`: 특정 `<command>`의 상세 도움말 표시
   - `exit`: 어플리케이션 종료

## 추후 개발 예정

- 셸 스크립트 처럼 셸 명령행에서 입력받는 기능
- 클론하여 설치하는 것이 아닌 `<npm install>` 등으로 설치되는 기능
- 사용자 별로 독립적인 데이터를 갖는 프로그램
- 실행 시 `<tasks.json>` 파일이 자동으로 생성되는 기능
