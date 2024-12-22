
## 프로젝트 구조 

david/
├── src/                         # 소스 코드 디렉토리
│   ├── project_name/            # 실제 패키지 1 
│   │   ├── __init__.py
│   │   ├── module1.py
│   │   └── module2.py
│   ├── project_name_2/          # 실제 패키지 2
│   │   ├── __init__.py
│   │   ├── module1.py
│   │   └── module2.py
│   └── utils/                   # 유틸리티 코드
│       ├── __init__.py
│       └── helpers.py
├── tests/                       # 테스트 코드
├── docs/                        # 문서
├── requirements.txt             # 의존성 관리
├── setup.py                     # 설치 스크립트
└── README.md                    # 프로젝트 설명
