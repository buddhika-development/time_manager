from src.factories.llm_factory import LLMFactory

input = "hello"

llm = LLMFactory.create("mistral")

print(llm.invoke(input).content)