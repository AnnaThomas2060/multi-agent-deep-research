import os
from crewai import Crew, Process, Task
from src.agents.research_agents import (
    create_orchestrator,
    create_search_agent,
    create_reading_agent,
    create_citation_agent,
    create_report_generator
)

def run_research(query: str):
    orchestrator = create_orchestrator()
    search_agent = create_search_agent()
    reading_agent = create_reading_agent()
    citation_agent = create_citation_agent()
    report_generator = create_report_generator()

    # Define tasks
    plan_task = Task(
        description=f'Analyze this query: {query}. Break it down into 2-3 specific sub-questions to research.',
        expected_output='A list of sub-questions for research.',
        agent=orchestrator
    )

    search_task = Task(
        description='For each sub-question, find 2 relevant URLs using the search tool.',
        expected_output='A list of URLs relevant to the sub-questions.',
        agent=search_agent,
        context=[plan_task]
    )

    read_task = Task(
        description='Scrape the URLs provided by the search agent. Read the content and summarize key findings.',
        expected_output='Summarized findings extracted from the URLs.',
        agent=reading_agent,
        context=[search_task]
    )

    citation_task = Task(
        description='Review the findings and ensure they are paired with their source URLs to generate proper citations.',
        expected_output='Findings with properly formatted inline citations and a reference list.',
        agent=citation_agent,
        context=[read_task]
    )

    report_task = Task(
        description='Compile the cited findings into a final, cohesive research report. Structure it with headings.',
        expected_output='A comprehensive research report in Markdown.',
        agent=report_generator,
        context=[citation_task]
    )

    # Instantiate Crew
    crew = Crew(
        agents=[orchestrator, search_agent, reading_agent, citation_agent, report_generator],
        tasks=[plan_task, search_task, read_task, citation_task, report_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == '__main__':
    print("Starting Autonomous Multi-Agent Deep Research System...")
    final_report = run_research("Latest advancements in CRISPR-based therapies for sickle cell disease")
    print("\n\n### FINAL REPORT ###\n")
    print(final_report)

