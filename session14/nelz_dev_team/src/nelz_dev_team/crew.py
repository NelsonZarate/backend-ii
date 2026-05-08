from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from .llm import llm
from .tools.file_writer import FileWriterTool

@CrewBase
class NelzDevTeam():

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def developer(self) -> Agent:
        return Agent(
            config=self.agents_config["developer"],
            llm=llm,
            tools=[FileWriterTool()],
            verbose=True
        )

    @agent
    def designer(self) -> Agent:
        return Agent(
            config=self.agents_config["designer"],
            tools=[FileWriterTool()],
            llm=llm,
            verbose=True
        )

    @task
    def build_landing_page(self) -> Task:
        return Task(
            config=self.tasks_config["build_landing_page"],
            agent=self.developer(),
            llm=llm
        )

    @task
    def design_dashboard(self) -> Task:
        return Task(
            config=self.tasks_config["design_dashboard"],
            agent=self.designer()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )