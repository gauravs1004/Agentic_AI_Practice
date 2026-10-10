def mock_llm_call(
        prompt,
        model,
        max_tokens,
        **params # keyword arguments
):
    print("hello world")
    print(prompt,model,max_tokens)
    print(params)
    if model=="gemini":
        print(params.get("gemini_id"))
        print(params.get("gemini_api_url"))
    elif model=="claude":
        print(params.get("claude_user_id"))
    elif model=="openai":
        print(params.get("account_id"))
        print(params.get("openai_key_id"))


mock_llm_call("What is Python?", "gemini", 1000, gemini_id="wddea", gemini_api_url="https//gemini.com")

mock_llm_call("What is Python?", "claude", 1000, claude_user_id="abhinav1234")

mock_llm_call("What is Python?", "openai", 1000, account_id="abhinav1234", openai_key_id="erfwe4")

# gemini - gemini_id, gemini_api_url
# claude - claude_user_id
# openai - account_id, openai_key_id