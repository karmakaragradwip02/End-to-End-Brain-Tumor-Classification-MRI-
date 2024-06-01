import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-End-Brain-Tumor-Classification-MRI-"
AUTHOR_USER_NAME = "karmakaragradwip02" 
SRC_REPO = "Brain Tumor Classification (MRI)"
AUTHOR_EMAIL = "karmakaragradwip02@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="CNN APP FOR BRAIN TUMOR CLASSIFICATION(MRI)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug_Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)