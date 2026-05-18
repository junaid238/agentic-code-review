from app.services.llm_service import generate_review


def load_prompt():

    with open(
        "app/prompts/security_prompt.txt",
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def review_code(code: str):

    prompt_template = load_prompt()

    final_prompt = prompt_template.format(code=code)

    review = generate_review(final_prompt)

    return review