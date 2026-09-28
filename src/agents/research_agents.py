from crewai import Agent
from src.tools.search_tool import DuckDuckGoSearchTool
from src.tools.browse_page_tool import BrowsePageTool
from src.tools.memory_manager import CleanMemoryTool

def create_orchestrator():
    return Agent(
        role='Research Orchestrator',
        goal='Deconstruct the main query into sub-questions and manage the research workflow.',
        backstory='You are a lead researcher responsible for breaking down complex topics and planning the research strategy.',
        allow_delegation=True,
        verbose=True
    )

def create_search_agent():
    return Agent(
        role='Web Search Specialist',
        goal='Find the most relevant URLs and sources for the given sub-questions.',
        backstory='You are an expert at querying search engines to find high-quality information.',
        tools=[DuckDuckGoSearchTool()],
        allow_delegation=False,
        verbose=True
    )

def create_reading_agent():
    return Agent(
        role='Content Synthesizer',
        goal='Read web pages and extract key facts, claims, and data points.',
        backstory='You excel at reading long documents and extracting the most salient information accurately.',
        tools=[BrowsePageTool(), CleanMemoryTool()],
        allow_delegation=False,
        verbose=True
    )

def create_citation_agent():
    return Agent(
        role='Citation Manager',
        goal='Track sources and generate proper citations for all claims.',
        backstory='You are meticulous about academic integrity and ensure every fact is properly cited.',
        allow_delegation=False,
        verbose=True
    )

def create_report_generator():
    return Agent(
        role='Lead Report Generator',
        goal='Compile synthesized findings into a cohesive, well-structured narrative.',
        backstory='You are an expert technical writer capable of weaving complex facts into an accessible report.',
        allow_delegation=False,
        verbose=True
    )

