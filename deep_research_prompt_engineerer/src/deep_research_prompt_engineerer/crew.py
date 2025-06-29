# src/deep_research_prompt_engineerer/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class DeepResearchPromptEngineerer():
    """Prompt Engineerer crew for Writing Deep Research Prompts"""

    @agent
    def research_question_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['research_question_analyst'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @task
    def initial_research_question_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['initial_research_question_analysis']
        )

    @task
    def contextualize_and_deconstruct_research_question(self) -> Task:
        return Task(
            config=self.tasks_config['contextualize_and_deconstruct_research_question']
        )
    
    @agent
    def prompt_guideline_integrator(self) -> Agent:
        return Agent(
            config=self.agents_config['prompt_guideline_integrator'],
            verbose=True
        )

    @task
    def synthesize_initial_prompt(self) -> Task:
        return Task(
            config=self.tasks_config['synthesize_initial_prompt'],
        )
    
    @agent
    def prompt_refiner(self) -> Agent:
        return Agent(
            config=self.agents_config['prompt_refiner'],
            verbose=True
        )

    @task
    def review_and_optimize_prompt(self) -> Task:
        return Task(
            config=self.tasks_config['review_and_optimize_prompt'],
        )
    
    @task
    def apply_refinement_suggestions(self) -> Task:
        return Task(
            config=self.tasks_config['apply_refinement_suggestions'],
        )
    
    @agent
    def guideline_compliance_auditor(self) -> Agent:
        return Agent(
            config=self.agents_config['guideline_compliance_auditor'],
            verbose=True
        )

    @task
    def audit_prompt_against_guidelines(self) -> Task:
        return Task(
            config=self.tasks_config['audit_prompt_against_guidelines'],
        )
    
    @agent
    def prompt_finalizer(self) -> Agent:
        return Agent(
            config=self.agents_config['prompt_finalizer'],
            verbose=True
        )

    @task
    def finalize_prompt_format(self) -> Task:
        return Task(
            config=self.tasks_config['finalize_prompt_format'],
            output_file='output/deep_research_prompt.md'
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