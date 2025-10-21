import google.generativeai as genai

# --- 1. 여기에 API 키를 붙여넣으세요 ---
GEMINI_API_KEY = "YOUR_API_KEY_HERE"
# ------------------------------------

try:
    # API 키로 제미나이 설정
    genai.configure(api_key=GEMINI_API_KEY)

    # 사용할 모델 선택
    model = genai.GenerativeModel('gemini-1.5-flash')

    # --- 2. 제미나이에게 물어볼 내용을 여기 쓰세요 ---
    prompt = "파이썬 코드로 챗봇 만드는 간단한 예시 보여줘"
    # ---------------------------------------------

    print(f"'{prompt}' 라고 물어보는 중...")

    # 모델에 프롬프트 전송
    response = model.generate_content(prompt)

    # 응답 출력
    print("\n--- 🤖 제미나이 응답 ---")
    print(response.text)
    print("------------------------")

except Exception as e:
    print(f"\n!!! 오류 발생 !!!")
    if "API_KEY_INVALID" in str(e):
        print("API 키가 잘못되었습니다. 키를 다시 복사해서 붙여넣으세요.")
    else:
        print(f"오류 상세 내용: {e}")