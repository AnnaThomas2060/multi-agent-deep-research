import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from crewai.tools import BaseTool

class BrowsePageTool(BaseTool):
    name: str = 'Browse Page Tool'
    description: str = 'Scrapes a webpage by URL and returns its content as Markdown.'

    def _run(self, url: str) -> str:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.extract()
            markdown = md(str(soup), strip=['a', 'img'])
            return markdown[:8000] # truncate to avoid huge contexts
        except Exception as e:
            return f"Failed to browse page: {str(e)}"

