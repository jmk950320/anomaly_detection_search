#!/bin/bash
# 아나콘다 환경 설정 스크립트

echo "아나콘다 환경 설정을 시작합니다..."

# 환경이 이미 존재하는지 확인
if conda env list | grep -q "anomaly-dataset-analysis"; then
    echo "환경 'anomaly-dataset-analysis'가 이미 존재합니다."
    read -p "기존 환경을 삭제하고 새로 만드시겠습니까? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "기존 환경을 삭제합니다..."
        conda env remove -n anomaly-dataset-analysis
    else
        echo "기존 환경을 사용합니다."
        conda activate anomaly-dataset-analysis
        exit 0
    fi
fi

# 새 환경 생성
echo "새 conda 환경을 생성합니다..."
conda env create -f environment.yml

# 환경 활성화
echo "환경을 활성화합니다..."
conda activate anomaly-dataset-analysis

echo "환경 설정이 완료되었습니다!"
echo ""
echo "사용법:"
echo "1. 환경 활성화: conda activate anomaly-dataset-analysis"
echo "2. PNG 분석 실행: python utils/mpdd.py"
echo "3. 환경 비활성화: conda deactivate"