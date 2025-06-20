# src/jd_summarizer/crew.py
from urllib.parse import urljoin, urlparse
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool


search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()


@CrewBase
class JDSummarizerCrew():
    """JD Summarizer crew for comprehensive job analysis and reporting"""

    @agent
    def job_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['job_researcher'],
            verbose=True,
            tools=[search_tool]
        )

    @agent
    def job_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['job_scraper'],
            verbose=True,
            tools=[scrape_tool]
        )
    
    @agent
    def job_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['job_analyzer'],
            verbose=True
        )
    
    @agent
    def job_summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['job_summarizer'],
            verbose=True
        )

    @task
    def job_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_research_task']
        )

    @task
    def job_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_extraction_task'],
        )
    
    @task
    def job_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_analysis_task']
        )

    @task
    def job_summarization_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_summarization_task'],
            output_file='output/report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the research crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )