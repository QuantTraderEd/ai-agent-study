import os

from dotenv import load_dotenv

#  OpenAI API를 사용하여 AI 응답을 받아오는 코드
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)  # OpenAI 클라이언트 초기화

# target_model = "gpt-4o-mini"
target_model="gpt-5-nano"
# target_model = "gpt-5-mini"

def get_responses(prompt, model=target_model):
    # 1. 입력된 프롬프트에 대한 AI 응답을 받아오는 함수
    # prompt: 사용자 입력 텍스트
    # model: 사용할 AI 모델 (기본값: gpt-5-mini)
    response = client.responses.create(
        model=model,  # 사용할 모델 지정
        tools=[{"type": "web_search_preview"}],  # 2. 웹 검색 도구 활성화
        input=prompt,  # 사용자 입력 전달
    )

    return response.output_text  # 텍스트 응답만 반환


# 3. 스크립트가 직접 실행될 때 실행
if __name__ == "__main__":
    prompt = """
    https://blogs.nvidia.com/blog/hot-chips-inference-networking/
    를 읽어서 제목과 불릿포인트 3줄 요약을 한글로 작성해주세요. 
    """
    output = get_responses(prompt)
    print(output)  # 결과 출력