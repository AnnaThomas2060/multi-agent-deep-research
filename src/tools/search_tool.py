from crewai.tools import BaseTool
from pydantic import Field
from duckduckgo_search import DDGS

class DuckDuckGoSearchTool(BaseTool):
    name: str = 'DuckDuckGo Search'
    description: str = 'Use this tool to search the internet for information. It returns search results with titles, snippets, and URLs.'

    def _run(self, query: str) -> str:
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=5))
                if not results:
                    return "No results found."
                return '\n\n'.join([f"Title: {r.get('title')}\nSnippet: {r.get('body')}\nURL: {r.get('href')}" for r in results])
        except Exception as e:
            return f"Search failed: {str(e)}"

