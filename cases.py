from typing import Dict, List, Any

CASES = {
    "산업재해": {
        "keywords": ["추락", "안전", "사고", "재해", "산재", "작업", "부상", "끼임", "절단", "감전", "사망", "질병", "직업병"],
        "sub_types": {
            "추락": {
                "keywords": ["추락", "높이", "난간", "사다리", "발판", "떨어짐"],
                "templates": [{
                    "case_summary": """2m 이상 높이에서의 추락사고로 인한 중상해 사례입니다. 산업안전보건법상 사업주의 안전조치의무 위반이 명백하며, 다음과 같은 법적 조치가 가능합니다:

1. 산재보험급여 청구: 치료비, 휴업급여, 장해급여 등
2. 사업주에 대한 민사상 손해배상청구
3. 안전조치의무 위반에 대한 형사고발 검토

특히 안전난간 미설치는 산업안전보건법 위반의 대표적 사례로, 사업주의 100% 책임이 인정될 가능성이 높습니다.""",
                    "related_laws": [
                        {
                            "name": "산업안전보건법 제38조",
                            "description": "사업주는 추락위험이 있는 장소에 안전난간, 덮개, 추락방지망 등 추락방지시설을 설치해야 함"
                        },
                        {
                            "name": "산업재해보상보험법 제37조",
                            "description": "업무상 재해에 대한 보상급여 지급기준"
                        }
                    ],
                    "similar_cases": [
                        {
                            "number": "대법원 2022다31458",
                            "description": "건설현장 추락사고에서 안전시설 미비로 사업주 책임 100% 인정"
                        }
                    ],
                    "compensation": {
                        "medical_cost": "4,800,000",
                        "hospital_cost": "2,250,000",
                        "monthly_salary": "3,500,000",
                        "loss_period": "45",
                        "loss_amount": "5,250,000",
                        "total_amount": "25,300,000"
                    },
                    "next_steps": {
                        "step1": "근로복지공단 산재보험 신청\\n치료비와 휴업급여를 우선적으로 보상받으실 수 있습니다.",
                        "step2": "사업주와 손해배상 협의\\n산재보험 외 추가 보상에 대한 협의를 진행합니다.",
                        "step3": "민사소송 검토\\n협의가 이루어지지 않을 경우, 민사소송을 통해 권리를 구제받을 수 있습니다."
                    },
                    "special_notes": "현재 치료가 진행 중이므로, 향후 장해가 발생할 경우 추가적인 보상을 청구할 수 있습니다. 따라서 섣부른 합의는 피하시고, 치료가 완전히 종결된 후 최종적인 보상을 받는 것이 유리할 것으로 판단됩니다."
                }]
            },
            "끼임": {
                "keywords": ["끼임", "협착", "기계", "설비", "절단"],
                "templates": [{
                    "case_summary": """기계설비 작동 중 발생한 끼임사고 사례입니다. 산업안전보건법상 방호조치 의무 위반이 인정되며, 다음과 같은 권리구제가 가능합니다:

1. 산재보험을 통한 치료비, 휴업급여 신청
2. 신체장해에 따른 장해급여 청구
3. 사업주에 대한 손해배상청구""",
                    "related_laws": [
                        {
                            "name": "산업안전보건법 제33조",
                            "description": "사업주는 기계·기구·설비 등에 대한 방호조치를 하여야 함"
                        }
                    ],
                    "compensation": {
                        "medical_cost": "6,800,000",
                        "hospital_cost": "3,250,000",
                        "monthly_salary": "3,500,000",
                        "loss_period": "60",
                        "loss_amount": "7,250,000",
                        "total_amount": "35,300,000"
                    },
                    "next_steps": {
                        "step1": "산재보험 청구\\n치료비와 휴업급여 신청을 진행합니다.",
                        "step2": "장해급여 신청\\n후유장해가 있는 경우 장해급여를 청구합니다.",
                        "step3": "손해배상 청구\\n사업주의 안전조치의무 위반에 대한 손해배상을 청구합니다."
                    },
                    "special_notes": "기계설비 안전검사 기록과 방호장치 설치 여부 등의 증거수집이 중요합니다.",
                    "similar_cases": [
                        {
                            "number": "대법원 2023다12345",
                            "description": "방호장치 미설치로 인한 끼임사고에서 사업주 책임 인정"
                        }
                    ]
                }]
            }
        }
    },

    "명예훼손": {
        "keywords": ["명예", "허위", "비방", "모욕", "악플", "댓글", "유포", "SNS", "기사"],
        "sub_types": {
            "온라인": {
                "keywords": ["댓글", "SNS", "유튜브", "인터넷", "카페"],
                "templates": [{
                    "case_summary": """온라인 플랫폼에서 발생한 명예훼손 사례입니다. 정보통신망법상 명예훼손죄 및 민사상 손해배상청구가 가능합니다.""",
                    "related_laws": [
                        {
                            "name": "정보통신망법 제70조",
                            "description": "사실 적시 명예훼손의 경우 3년 이하 징역 또는 3천만원 이하 벌금"
                        }
                    ],
                    "compensation": {
                        "medical_cost": "0",
                        "hospital_cost": "0",
                        "monthly_salary": "3,500,000",
                        "loss_period": "30",
                        "loss_amount": "3,500,000",
                        "total_amount": "10,000,000"
                    },
                    "next_steps": {
                        "step1": "증거수집\\n게시물 캡쳐 및 보존",
                        "step2": "형사고소\\n경찰서에 명예훼손 고소장 제출",
                        "step3": "민사소송\\n손해배상청구 소송 제기"
                    },
                    "special_notes": "게시물 증거보전이 매우 중요하므로 즉시 캡쳐하여 보관하시기 바랍니다.",
                    "similar_cases": [
                        {
                            "number": "대법원 2022도4567",
                            "description": "악의적 허위사실 유포로 인한 명예훼손 유죄 판결"
                        }
                    ]
                }]
            }
        }
    },

    "임금체불": {
        "keywords": ["임금", "월급", "체불", "급여", "퇴직금", "체임"],
        "sub_types": {
            "임금체불": {
                "keywords": ["임금", "월급", "체불", "밀림"],
                "templates": [{
                    "case_summary": """3개월 이상 임금이 체불된 사례입니다. 다음과 같은 법적 구제수단이 가능합니다:

1. 고용노동부 진정
2. 임금체불 민사소송
3. 체당금 신청""",
                    "related_laws": [
                        {
                            "name": "근로기준법 제36조",
                            "description": "임금지급 원칙과 지연이자"
                        }
                    ],
                    "compensation": {
                        "medical_cost": "0",
                        "hospital_cost": "0",
                        "monthly_salary": "3,500,000",
                        "loss_period": "90",
                        "loss_amount": "10,500,000",
                        "total_amount": "15,000,000"
                    },
                    "next_steps": {
                        "step1": "고용노동부 진정\\n체불임금확인서 발급",
                        "step2": "체당금 신청\\n근로복지공단에 체당금 신청",
                        "step3": "민사소송\\n지급명령 신청"
                    },
                    "special_notes": "체불임금에 대한 지연이자도 청구 가능합니다.",
                    "similar_cases": [
                        {
                            "number": "서울중앙지법 2023가단56789",
                            "description": "장기 체불 임금 전액 및 지연이자 지급 판결"
                        }
                    ]
                }]
            }
        }
    }
}

default_template = {
    "case_summary": "구체적인 사실관계 확인이 필요한 사례입니다.",
    "related_laws": [{"name": "관련법", "description": "해당 사안과 관련된 법률"}],
    "compensation": {
        "medical_cost": "0",
        "hospital_cost": "0",
        "monthly_salary": "0",
        "loss_period": "0",
        "loss_amount": "0",
        "total_amount": "0"
    },
    "next_steps": {
        "step1": "상담",
        "step2": "증거수집",
        "step3": "법적조치"
    },
    "special_notes": "추가 상담이 필요합니다.",
    "similar_cases": [
        {
            "number": "사례 없음",
            "description": "유사 판례 확인 필요"
        }
    ]
}



