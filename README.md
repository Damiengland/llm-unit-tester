# **LLM Unit Tester**

## **Description**

This project leverages the power of Large Language Models (LLMs) to automatically generate unit tests for Python code. You provide a Python function or class, and it uses the OpenAI API (specifically, the gpt-4o model) to generate corresponding test cases. The application features a simple web interface built with Gradio for easy interaction.

## **Features**

* **Automated Unit Test Generation**: Simply paste your Python code and get unit tests back.  
* **Powered by GPT-4o**: Utilizes OpenAI's latest model for high-quality, relevant test case generation.  
* **Simple Web Interface**: An intuitive UI built with Gradio allows you to input your code and see the generated tests in real-time.  
* **Streamed Responses**: Test cases are streamed from the API for a responsive user experience.  
* **File Output**: The generated tests are automatically saved to a unit\_tests.py file.

## **Installation**

1. **Clone the repository:**  
   git clone \<your-repository-url\>  
   cd \<your-repository-name\>

2. Create and activate the conda environment:  
   Use the requirements.yml file (included in the project) to create the new environment:  
   conda env create \-f requirements.yml

   Then activate it:  
   conda activate llm-tester

3. Set up your environment variables:  
   Create a .env file in the root of the project and add your API keys:  
   OPENAI\_API\_KEY="your\_openai\_api\_key"

## **Usage**

1. **Start the Jupyter Notebook:**  
   jupyter notebook unit\_tester.ipynb

2. Run the cells:  
   Execute the cells in the notebook sequentially.  
3. **Use the Gradio Interface:**  
   * The last cell will launch a Gradio web interface.  
   * Enter your Python code into the "Raw Python code" textbox.  
   * Click the "Build Tests" button.  
   * The generated unit tests will appear in the "Commented Python Code" textbox and will also be saved to a file named unit\_tests.py in your project directory.

## **Author**

* Damien

## **License**

This project is licensed under the MIT License.