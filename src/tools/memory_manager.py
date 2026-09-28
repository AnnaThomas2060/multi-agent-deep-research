from crewai.tools import BaseTool

class CleanMemoryTool(BaseTool):
    name: str = 'Clean Memory Tool'
    description: str = 'Use this tool to summarize past findings and clear up context space. Provide the text you want to compress as input.'

    def _run(self, text: str) -> str:
        # In a real scenario, this could use an SLM to summarize
        # For now, we return a truncated version or prompt the model to summarize
        return f"Compressed representation of {len(text)} characters: {text[:500]}... (truncated)"

