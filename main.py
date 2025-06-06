import os
from typing import Tuple

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

import linkedin

from agents.linkedIn_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import summary_parser, Summary


def agent_with(name: str) -> Tuple[Summary, str]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = linkedin.scrape_linkedin_profile(
        linkedin_profile_url= linkedin_username,
        mock=True
    )

    summary_template = """
            given the Linkedin information {information} about a person from I want you to create:
            1. a short summary
            2. two interesting facts about them
            
            
            \n{format_instructions}
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()})

    llm = ChatOpenAI(temperature=0, model_name="gpt-4.1-nano")

    chain = summary_prompt_template | llm | summary_parser

    res: Summary = chain.invoke(input={"information": linkedin_data})

    return res, linkedin_data.get("photoUrl")


if __name__ == "__main__":
    load_dotenv()

    print("Look up Agent Start Working")
    agent_with(name="Muhammad Saad Majeed")