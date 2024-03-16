from setuptools import find_packages, setup

setup(
    name = 'mcqgenerator',
    version='0.0.1',
    author='Kaustubh More',
    author_email='kaustubh.mor@gmil.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","pandas"],
    packages=find_packages()
)